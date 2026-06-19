from BookShala import app,db,bcrypt,mail,s
from flask import render_template,redirect,url_for,abort,request
from BookShala.forms import SellForm, LoginForm,SignUpForm, BuyForm, Reset_pwd_form
from BookShala.models import Books,Users,Orders
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(uname=form.uname.data).first()
        if(user and bcrypt.check_password_hash(user.pwd_hash, form.pwd.data)):
            login_user(user)
            n=request.args.get(next)
            return redirect(f'/{n}') if n else redirect('/home')
    return render_template('login.html',form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form =SignUpForm()
    if form.validate_on_submit():
        user=Users(uname=form.uname.data,
                    email=form.email.data,
                    addr=form.addr.data,
                    pwd_hash=bcrypt.generate_password_hash(form.pwd.data).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('signup.html',form=form)
    
@app.route('/')
@app.route('/home')
def home():
    books=Books.query.all()
    return render_template('home.html',books=books)

@app.route('/sell',methods=['GET', 'POST'])
@login_required
def sell():
    form= SellForm()
    if form.validate_on_submit():
        book=Books(bname=form.bname.data,
                   isbn=form.isbn.data,
                   dop=form.dop.data,
                   cond=form.cond.data,
                   price=form.price.data,
                   seller=current_user
                   )
        if (form.opt.data=='Sell'):
            book.exchange=0
        elif (form.opt.data=='Exchange'):
            book.sell=0
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('sell.html',form=form)

@app.route('/buy/<int:bid>', methods=['GET', 'POST'])
@login_required
def buy(bid):
    book=Books.query.get(bid)
    form=BuyForm()
    if form.validate_on_submit():
        order=Orders(bid=book.id,
                     seller=book.owner,
                     buyer=current_user.id,
                     del_to=form.addr.data,
                     mop=form.mop.data,
                     del_from=book.seller.addr)
        db.session.add(order)
        
        # db.session.delete(book)
        # book.sold=1
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('buy.html', form=form, book=book)

@app.route('/books/<int:bid>')
def view_book(bid):
    book=Books.query.get(bid)
    return render_template('view_book.html', book=book)

@app.route('/books/<int:bid>/update', methods=['GET', 'POST'])
def update_book(bid):
    book=Books.query.get(bid)
    if not(current_user==book.seller):
        abort(403)
    form= SellForm()

    if (request.method=='GET'):
        form.isbn.data=book.isbn
        form.price.data=book.price
        form.dop.data=book.dop
        form.cond.data=book.cond
        form.bname.data=book.bname
        if (book.sell==1 and book.exchange==1):
            form.opt.data='Any'
        elif (book.sell==1):
            form.opt.data='Sell'
        else:
            form.opt.data='Exchange'

    if form.validate_on_submit():
        book.isbn=form.isbn.data
        book.price=form.price.data
        book.dop=form.dop.data
        book.cond=form.cond.data
        book.bname=form.bname.data
        if (form.opt.data=='Sell'):
            book.exchange=0
            book.sell=1
        elif (form.opt.data=='Exchange'):
            book.sell=0
            book.exchange=1
        db.session.commit()
        return redirect(url_for('view_book',bid=book.id))
    
    return render_template('update_book.html', book=book,form=form)

@app.route('/account')
@login_required
def account():
    return render_template('account.html', user=current_user)

@app.route('/account/update', methods=['GET', 'POST'])
@login_required
def update_account():
    user=current_user
    form=SignUpForm()
    if (request.method=='GET'):
        form.email.data=user.email
        form.addr.data=user.addr
        form.uname.data=user.uname
    
    if form.validate_on_submit():
        user.email=form.email.data
        user.addr=form.addr.data
        user.uname=form.uname.data
        db.session.commit()
        return redirect(url_for('account'))
    return render_template('update_account.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/delete_account/<int:id>')
def del_acc(id):
    if(current_user!=Users.query.get(id)):
        abort(403)
    db.session.delete(Users.query.get(id))
    db.session.commit()

@app.route('/delete_book/<int:id>', methods=['GET','POST'])
@login_required
def del_book(id):
    if(current_user!=Books.query.get(id).seller):
        abort(403)
    db.session.delete(Books.query.get(id))
    db.session.commit()
    return redirect('/home')

@app.route('/reset_password', methods=['GET','POST'])
def reset_link():
    form=Reset_pwd_form()
    user=None
    if(current_user.is_authenticated):
        email=current_user.email
        user=current_user
    else:
        if (form.validate_on_submit()):
            email=form.email.data
            user=Users.query.filter_by(email=email).first()
    if(user):
        msg=Message('Password Reset Email', sender=app.config['MAIL_USERNAME'], recipients=[email])
        user=Users.query.filter_by(email=email).first()
        token=s.dumps(user.id)
        # token='qdwafes'
        msg.body=(url_for('reset_pwd', token=token, _external=True))
        mail.send(msg)
    return render_template('reset_link.html',form=form)

@app.route('/reset_password/<token>',methods=['GET','PUT','POST'])
def reset_pwd(token):
    try:
        uid=s.loads(token)
    except:
        return redirect(url_for('reset_link'))
    user=Users.query.get(uid)
    form=SignUpForm()
    if(form.validate_on_submit()):
        user.pwd_hash=bcrypt.generate_password_hash(form.pwd.data).decode('utf-8')
        db.session.commit()
        if(current_user.is_authenticated):
            logout_user()
        return redirect(url_for('login'))
    return render_template('reset_pwd.html',form=form)
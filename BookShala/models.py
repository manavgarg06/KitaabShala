from BookShala import db,lm
from flask_login import UserMixin


@lm.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Orders(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    bid=db.Column(db.Integer(), db.ForeignKey('books.id'), nullable=False)
    seller=db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    buyer=db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    del_to=db.Column(db.String)
    del_from=db.Column(db.String)
    mop=db.Column(db.String())

    
class Books(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    bname=db.Column(db.String(),nullable=False)
    isbn=db.Column(db.String(),nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    dop=db.Column(db.DateTime(),nullable=False)
    cond=db.Column(db.String(),nullable=False)
    sell=db.Column(db.Integer(), default=1)
    exchange=db.Column(db.Integer(), default=1)
    # sold=db.Column(db.Integer(),default=0)
    owner=db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    # owner=db.Column(db.Integer(), db.ForeignKey('user.id'))
    orders=db.relationship("Orders", backref='book', lazy=True)

# class Transactions(db.Model):
#     id=db.Column(db.Integer(), primary_key=True)
#     bname=db.Column(db.String(),nullable=False)
#     isbn=db.Column(db.String(),nullable=False)
#     price=db.Column(db.Integer(),nullable=False)
#     dop=db.Column(db.DateTime(),nullable=False)
#     cond=db.Column(db.String(),nullable=False)
#     sell=db.Column(db.Integer(), default=1)
#     exchange=db.Column(db.Integer(), default=1)
#     # sold=db.Column(db.Integer(),default=0)
#     owner=db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
#     # owner=db.Column(db.Integer(), db.ForeignKey('user.id'))
#     orders=db.relationship("Orders", backref='book', lazy=True)


class Users(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    uname=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)
    addr=db.Column(db.String(),nullable=False)
    pwd_hash=db.Column(db.String(),nullable=False)
    # dp=db.Column(db.String())
    books=db.relationship("Books", backref='seller', lazy=True)
    sold=db.relationship("Orders", backref='bseller', foreign_keys='Orders.seller', lazy=True)
    bought=db.relationship("Orders", backref='bbuyer', foreign_keys='Orders.buyer', lazy=True)
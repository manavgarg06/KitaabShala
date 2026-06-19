from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField,SubmitField,SearchField,DateField,FileField,RadioField, BooleanField
# from wtforms.validators import ValidationError


class BuyForm(FlaskForm):
    addr=StringField('Enter Address: ')
    mop=RadioField('Payment Method: ', choices=['Cash On Delivery', 'UPI'])
    submit=SubmitField('Buy')

class SellForm(FlaskForm):
    isbn=StringField(label='Enter ISBN Code')
    bname=StringField(label='Enter Name of Book')
    dop=DateField(label='Enter Original Date of Purchase')
    opt=RadioField(label='Enter Choice:', choices=['Sell', 'Exchange', 'Any'])
    cond=RadioField(label='Enter Condition of Book:', choices=['Brand New', 'Fair Enough', 'Poor'])
    # photo=FileField('Upload Photo')
    price=IntegerField(label='Enter Price')
    submit=SubmitField(label='Sell')

class LoginForm(FlaskForm):
    uname=StringField(label='Enter Username: ')
    pwd=PasswordField(label='Enter Password: ')
    # rem=BooleanField(label='Remember User?')
    submit=SubmitField(label='Log In')
    # raise ValidationError('Error check')

class SignUpForm(FlaskForm):
    uname=StringField(label='Enter Username: ')
    email=StringField(label='Enter email address: ')
    addr=StringField(label='Enter Addr of Residence: ')
    pwd=PasswordField(label='Enter Password: ')
    submit=SubmitField(label='Sign Up')

class Reset_pwd_form(FlaskForm):
    email=StringField(label='Enter email linked with account')
    submit=SubmitField('Get Password Reset Link')
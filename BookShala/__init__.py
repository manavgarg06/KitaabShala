from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer as Serialiser
# import razorpay

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///bookshala.db'
app.config['SECRET_KEY']='1234h'
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= 1
app.config['MAIL_USERNAME']='manavgarg188@gmail.com'
app.config['MAIL_PASSWORD']= 'YOUR_APP_PASSWORD'
app.config['RAZORPAY_KEY_ID']="key daaldo yaha pe"
app.config['RAZORPAY_KEY_SECRET']='1234'

db=SQLAlchemy(app)
bcrypt=Bcrypt()
lm=LoginManager(app)
lm.login_view='login'
s=Serialiser(app.config['SECRET_KEY'])
mail=Mail(app)
# lm.login_message = "Please log in to access this page."
# lm.login_message_category = "info"  # Bootstrap alert class, if using

# login_manager.init_app(app)

from BookShala import routes
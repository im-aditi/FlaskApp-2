from flask import Flask
#url_for finds the exact routes for us so that we don't worry about it in main
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#We need to set a secret key which protects against modifying cookies and cross-site requests and forgery attacks
app.config['SECRET_KEY'] = '7186bfb3da5c04264f9216cf0ba12cf99812977d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'     #Relative path with /// from current file
db = SQLAlchemy(app)        #Creating an database instance

from flask_blog import routes
from api import *
from itsdangerous import JSONWebSignatureSerializer as Serialize
from flask_login import AnonymousUserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, ForeignKey, String, Column
from datetime import datetime

class Admin(dbase.Model):
	__tablename__ = 'admin'
	username = dbase.Column(dbase.String(50), primary_key=True, nullable=False)
	password = dbase.Column(dbase.String(100), nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = generate_password_hash(password, method='sha256')

class Employee(dbase.Model):
	__tablename__ = 'employee'
	id = dbase.Column(dbase.Integer, primary_key = True , autoincrement = True )
	fname = dbase.Column(dbase.String(50))
	mname = dbase.Column(dbase.String(50))
	lname = dbase.Column(dbase.String(50))
	position = dbase.Column(dbase.String(30))
	code = dbase.Column(dbase.String(15))
	contact = dbase.Column(dbase.String(15))
	email = dbase.Column(dbase.String(30))

	def __init__(self,fname, mname, lname, position, code, contact, email):
		self.fname = fname
		self.mname = mname
		self.lname = lname
		self.position = position
		self.code = code
		self.contact = contact
		self.email = email

class Logs(dbase.Model):
    __tablename__ = "logs"
    logID = dbase.Column(dbase.Integer, primary_key=True, autoincrement=True)
    details = dbase.Column(dbase.String(60))
    log_date =dbase.Column(dbase.DateTime)

    def __init__(self, details, log_date):
        self.details = details
        self.log_date = log_date







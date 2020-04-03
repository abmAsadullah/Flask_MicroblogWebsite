import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = 'random_string_here'
	SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'masum.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
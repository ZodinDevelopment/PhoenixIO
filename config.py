import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret-to-everyone'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'phoenix.db')
    ADMINS = ['michael.landon@zodin.dev']
    POSTS_PER_PAGE = 15


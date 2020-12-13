import os

BASE_PATH = os.path.split(__file__)[0]

DATABASE_URL = 'sqlite:///{}'.format(os.path.join(BASE_PATH, 'database.sqlite'))
#DATABASE_URL = 'mysql+mysqlconnector://root:123@localhost/database_editor?charset=utf8'

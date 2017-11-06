#配置文件
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_DB = 'test'

DEBUG = True
PORT = 3333
# HOST = "192.168.1.141"
HOST = "localhost"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
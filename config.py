DB_CONFIG = {

    'DB_CONNECT_TYPE': 'pymongo',  # 'pymongo'sqlalchemy;redis
    'DB_CONNECT_STRING':'mongodb://username:password@ip:port/authdb'
    # 'DB_CONNECT_STRING': 'sqlite:///' + os.path.dirname(__file__) + '/data/accounts.db'
    # DB_CONNECT_STRING : 'mysql+mysqldb://root:root@localhost/accounts?charset=utf8'
    # 'DB_CONNECT_TYPE': 'redis',  # 'pymongo'sqlalchemy;redis
    # 'DB_CONNECT_STRING': 'redis://localhost:6379/8',

}

MONGO_DB = 'mydb'
MONGO_COLL = 'accounts'
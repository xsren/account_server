import pymongo
from config import DB_CONFIG, MONGO_DB, MONGO_COLL, TOKEN_COLL

from db.ISqlHelper import ISqlHelper
import time

from utils import md5

class MongoHelper(ISqlHelper):
    def __init__(self):
        self.client = pymongo.MongoClient(DB_CONFIG['DB_CONNECT_STRING'], connect=False)

    def init_db(self):
        self.db = self.client[MONGO_DB]
        self.coll = self.db[MONGO_COLL]

    def drop_db(self):
        self.client.drop_database(self.db)

    def find_token(self, token):
        if self.db[TOKEN_COLL].find_one({'token':token}):
            return True
        else:
            return False

    def select(self, site, count=1):
        items = self.coll.find({'site':site}).limit(count).sort([('last_use_time',pymongo.ASCENDING)])
        results = []
        for item in items:
            self.coll.update_one({'uid':item['uid']},{'$set':{'last_use_time':time.time()}})
            result = {'uid':item['uid'],
                    'site':item['site'],
                    'uname':item['uname'],
                    'passwd':item['passwd'],
                    'cookie':item['cookie'],
                    'email':item.get('email',None),
                    'extra':item.get('extra',None)}
            results.append(result)
        return results

    def insert(self, site, uname, passwd, cookie, email, extra):
        data = {'site':site,
                'uname':uname,
                'passwd':passwd,
                'cookie':cookie,
                'email':email,
                'extra':extra,
                'last_use_time':time.time(),
                'uid':md5(site+uname)}
        self.coll.insert_one(data)
        return 'ok'

    def delete(self, uid):
        self.coll.delete_one({'uid':uid})
        return 'ok'


if __name__ == '__main__':
    pass

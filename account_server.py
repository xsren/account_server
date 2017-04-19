#coding:utf8
from flask import Flask
from flask import request
from flask import jsonify

from config import DB_CONFIG

app = Flask(__name__)



def get_db():
    if DB_CONFIG['DB_CONNECT_TYPE'] == 'pymongo':
        from db.MongoHelper import MongoHelper as SqlHelper
    elif DB_CONFIG['DB_CONNECT_TYPE'] == 'redis':
        from db.RedisHelper import RedisHelper as SqlHelper
    else:
        from db.SqlHelper import SqlHelper as SqlHelper
    sqlhelper = SqlHelper()
    sqlhelper.init_db()
    return sqlhelper

db = get_db()

@app.route('/delete')
def delete():
    uid = request.args.get('uid',None)
    if uid:
        data = db.delete(uid)
        return jsonify({'status':0,'info':'ok','data':data})
    else:
        return jsonify({'status':1,'info':'param not enough'})

@app.route('/insert')
def insert():
    site = request.args.get('site',None)
    uname = request.args.get('uname',None)
    passwd = request.args.get('passwd',None)
    cookie = request.args.get('cookie',None)
    email = request.args.get('email',None)
    extra = request.args.get('extra',None)
    if site and uname and passwd:
        data = db.insert(site,uname,passwd,cookie,email,extra)
        return jsonify({'status':0,'info':'ok','data':data})
    else:
        return jsonify({'status':1,'info':'param not enough'})

@app.route('/select')
def select():
    site = request.args.get('site',None)
    count = int(request.args.get('count',1))
    if site:
        data = db.select(site,count)
        return jsonify({'status':0,'info':'ok','data':data})
    else:
        return jsonify({'status':1,'info':'param not enough'})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

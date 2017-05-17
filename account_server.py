#coding:utf8
from flask import Flask, request, jsonify, Response

from functools import wraps

from config import DB_CONFIG

app = Flask(__name__)

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL, need token.\n', 403,
    {'WWW-Authenticate': 'Basic realm="token Required"'})

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

def auth(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        token = request.args.get("token",None)
        if db.find_token(token):
            return fun(*args, **kwargs)
        else:
            return authenticate()
    return wrapper_fun

@auth
@app.route('/delete')
def delete():
    uid = request.args.get('uid',None)
    if uid:
        data = db.delete(uid)
        return jsonify({'status':0,'info':'ok','data':data})
    else:
        return jsonify({'status':1,'info':'param not enough'})

@auth
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

@auth
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
    app.run(host='0.0.0.0', port=5002, debug=False)

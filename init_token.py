#coding:utf8
import time
import click
from config import DB_CONFIG, TOKEN_COLL

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

@click.command()
@click.option('--tolen', default='4cc5fbe69e2a93d48bef68319b763541', help='add')
def main(token):
    click.echo('start to insert token:%s'%token)
    if not db[TOKEN_COLL].find_one({'token':token}):
        db[TOKEN_COLL].insert({'token':token,'date':time.strftime()})
        click.echo('success to insert token:%s'%token)
    else:
        click.echo('already has token:%s'%token)

if __name__ == '__main__':
    main()
SRF_ENABLED = True
SECRET_KEY = 'iwnids-sdf-sdfeg-erewr'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DBUSERNAME='root'
DBPASSWD='123456'
DBHOST='localhost'
DBNAME='sqlalchemy_test'


SQLALCHEMY_DATABASE_URI = 'mysql://'+DBUSERNAME+':'+DBPASSWD+'@'+DBHOST+'/'+DBNAME
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

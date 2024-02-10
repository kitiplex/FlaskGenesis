import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbport=os.environ['DBPORT'],
    dbname=os.environ['DBNAME']
)

TIME_ZONE = 'Asia/Manila'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'


# postgresql://host:port/database
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
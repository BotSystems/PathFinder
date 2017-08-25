import datetime
import os
from os.path import join, dirname

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, IntegerField, CharField, DateTimeField

if os.path.isfile('.env.settings'):
    dotenv_path = join(dirname(__file__), '.env.settings')
    load_dotenv(dotenv_path)

DATABASE_CREDENTIALS = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host ': os.getenv('DB_HOST'),
    'port ': os.getenv('DB_PORT')
}

db = PostgresqlDatabase(os.getenv('DB_NAME'), **DATABASE_CREDENTIALS)


class Chanel(Model):
    chanel_id = IntegerField(unique=True)

    first_name = CharField(null=True)
    last_name = CharField(null=True)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def update_me(self):
        self.updated_at = datetime.datetime.now()
        self.save()

    class Meta:
        database = db

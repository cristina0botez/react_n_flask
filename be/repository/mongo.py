import os
from pymongo import MongoClient

COLLECTION_NAME = 'kudos'

class MongoRepository:
    def __init__(self):
        self.db = MongoClient('mongodb://user:secret@127.0.0.1:27017/').kudos

    def find_all(self, selector):
        return self.db.kudos.find(selector)

    def find(self, selector):
        return self.db.kudos.find_one(selector)

    def create(self, kudo):
        return self.db.kudos.insert_one(kudo)

    def update(self, selector, kudo):
        return self.db.kudos.replace_one(selector, kudo).modified_count

    def delete(self, selector):
        return self.db.kudos.delete_one(selector).deleted_count

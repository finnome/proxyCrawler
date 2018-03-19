import pymongo
from proxyCrawler import settings

class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.MONGO_DATABASE]

    def close(self):
        self.client.close()
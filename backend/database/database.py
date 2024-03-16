from pymongo import MongoClient
from config import AppConfig

client = MongoClient({AppConfig.mongo_url})

db = client['which-img']
collectionResult = db['feedback']
collectionMeta = db['metaData']

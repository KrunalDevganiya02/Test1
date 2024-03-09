from pymongo import MongoClient

client = MongoClient('mongodb+srv://which-img:cialabsintern@atlascluster.mytwvuv.mongodb.net/')
db = client['which-img']
collectionResult = db['feedback']
collectionMeta = db['metaData']

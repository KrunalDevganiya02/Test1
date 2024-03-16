from typing import List

class AppConfig:
    ORIGINS = ["*"] 
    STORAGE_BASE_URL = "https://storage.cialabs.tech"

    #URL of the Model As Service to fetch the result for the Test Model👇
    
    MAS_SERVICE_URL = "https://cia-mas.cialabs.tech/"
    MAS_SERVICE_ENDPOINT = "upload/"


    # url for connect mongoDB 👇
    mongo_url= 'mongodb+srv://which-img:cialabsintern@atlascluster.mytwvuv.mongodb.net/'

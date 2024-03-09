from fastapi import HTTPException, UploadFile
from config import AppConfig
import base64
import json
import requests
from pydantic import BaseModel
from typing import List 
from database.database import client,db,collectionMeta,collectionResult
# from models.models import Metadata,Feedback

from pydantic import BaseModel
from typing import List 

class QuestionAnswer(BaseModel):
    questionID:str
    answer : str

class Metadata(BaseModel):
    type: str
    value: str

class Feedback(BaseModel):
    modelName : str
    imageKey : str
    qa : List[QuestionAnswer]


def test_model_v1(base64_str: str, model_name: str):
    if not all([base64_str, model_name]):
        raise HTTPException(status_code=400, detail="Missing required parameters: base64 and model_name")

    try:
        image_data = base64.b64decode(base64_str)
        data = {"image": ("image", image_data), "model_name": model_name}
        response = requests.post(f"{AppConfig.MAS_SERVICE_URL}{AppConfig.MAS_SERVICE_ENDPOINT}", data=data) 
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except (ValueError, requests.exceptions.RequestException) as e:
        raise HTTPException(status_code=500, detail=f"Error sending request to MAS service: {str(e)}")

def test_model_v2(file: UploadFile):
    try:
        files = {'file': (file.filename, file.file.read(), file.content_type)}
        response = requests.post(f"{AppConfig.MAS_SERVICE_URL}{AppConfig.MAS_SERVICE_ENDPOINT}", files=files)
        
        if response.status_code == 200:
            try:
                result = response.json()
                return "No" if result == 0 else "Yes"
            except ValueError:
                return {"error": "Failed to parse JSON response"}
        else:
            return {"error": "Failed to get response from API"}
        
    except Exception as e:
        return {"error": f"Failed to complete the request: {str(e)}"}

def create_metadata(metadata: Metadata):
    try:
        metadata_dict = metadata.dict()
        inserted_metadata = collectionMeta.insert_one(metadata_dict)
        return {"message": "Metadata created successfully", "metadata_id": str(inserted_metadata.inserted_id)}
        
    except Exception as e:
        return {"error": f"Failed to send metaFeedback the request: {str(e)}"}

def create_feedback(feedback: Feedback):
    try:
        feedback_id = collectionResult.insert_one(feedback.dict()).inserted_id
        return {"message": "Feedback submitted successfully", "feedback_id": str(feedback_id)}

    except Exception as e:
        return {"error": f"Failed to send feedback the request: {str(e)}"}



def read_model_data():
    try:
        with open('./models/models.json', 'r') as file:
            data = json.load(file)
            
            print(data1)
        return data[0]
    except Exception as e:
        print("errro krunal")



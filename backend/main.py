from fastapi import FastAPI, Query, HTTPException, Form, UploadFile, File
from service.service import test_model_v1, test_model_v2 ,create_metadata,create_feedback,Metadata,Feedback,read_model_data
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
from config import AppConfig  
from ciaos import save,get
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=AppConfig.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfiles/")
async def update_file(category: Optional[str] = Form(None), image: List[str] = Form(...)):
    try:
        save(AppConfig.STORAGE_BASE_URL, category, image)
        return JSONResponse(content={"message": f"Image saved locally at: {category}"}, status_code=200)
    except HTTPException as e:
        return JSONResponse(content={"error": str(e.detail)}, status_code=e.status_code)

@app.get("/get_images/{category}")
async def get_images(category: str):
    try:
        images = get(AppConfig.STORAGE_BASE_URL, category)
        return images
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/test_model")
async def test_model(base64: str = Query(..., description="Base64-encoded image data"), model_name: str = Query(..., description="Name of the model to use")):
   return test_model_v1(base64, model_name)

@app.post("/test_model_v2")
async def upload_file(file: UploadFile = File(...)):
    return test_model_v2(file)

@app.post("/metaFeedback")
async def create_metadata(metadata: Metadata):
    return create_metadata(metadata)

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    return create_feedback(feedback)

@app.get("/models")
async def read_models():
    return read_model_data()
    # models = read_model_data()
    # return JSONResponse(content=models)

import os
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from helpers.configs import get_settings, Settings
from controllers import ProjectController, DataController
from .schemes import ProcessRequest
from aiofile import async_open


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api-v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):
   
    if not DataController().validate_file(file):
        raise HTTPException(status_code=400, detail="Invalid file type or size.")

    file_path = ProjectController.get_project_path(project_id)  

    try:
        async with async_open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.CHUNK_SIZE): 
                await out_file.write(chunk)

        return {"message": f"File '{file.filename}' uploaded successfully for project '{project_id}'."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

    
# @data_router.post("/process/{project_id}")
# async def process_data(project_id: str, request: ProcessRequest): 
    
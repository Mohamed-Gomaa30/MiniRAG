from fastapi import UploadFile, HTTPException
from helpers.configs import get_settings
from .BaseController import BaseController 

class DataController(BaseController): 
    def __init__(self):
        super().__init__()

    def validate_file(self, file: UploadFile) -> bool:
        if file.content_type not in self.ALLOWED_FILE_TYPES:
            raise HTTPException(status_code=400, detail=f"Invalid file type. Allowed types: {self.ALLOWED_FILE_TYPES}")

        if file.size > self.FILE_MAX_SIZE:
            raise HTTPException(status_code=400, detail=f"File size exceeds the maximum limit of {self.FILE_MAX_SIZE} bytes.") 
            
        return True

    
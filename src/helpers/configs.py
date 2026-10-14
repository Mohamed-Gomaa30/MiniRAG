from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): 

    # APP SETTINGS 
    APP_NAME:str
    APP_VERSION:str

    # UPLOAD FILES SETTINGS
    ALLOWED_FILE_TYPES: list[str] = []
    FILE_MAX_SIZE: int = "10485760"  

    # uploaded files will be saved in this directory 
    UPLOAD_DIR: str = "assets/uploads"
    CHUNK_SIZE :int = 512000 
    
    model_config = SettingsConfigDict(
        env_file=".env",
    )


def get_settings(): 
    return Settings()


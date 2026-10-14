from .BaseController import BaseController 
from helpers.configs import get_settings  

class ProjectController(BaseController): 
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str) -> str:  
        
        project_dir_path = os.path.join(self.app_settings.UPLOAD_DIR, project_id)
        os.makedirs(project_dir_path, exist_ok=True)
        return project_dir_path



from helpers.configs import get_settings

class BaseController:
    def __init__(self):   
        self.ALLOWED_FILE_TYPES = get_settings().ALLOWED_FILE_TYPES
        self.FILE_MAX_SIZE = get_settings().FILE_MAX_SIZE
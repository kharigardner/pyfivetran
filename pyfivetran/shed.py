from typing import TypedDict, Dict, Any, Optional

BASE_API_URL = 'https://api.fivetran.com'
API_VERSION = "v1"

class GeneralApiResponse(TypedDict):
    code: str
    message: Optional[str]
    data: Optional[Dict[str, Any]]
    
class ApiError(Exception):
    def __inti__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class PaginatedApiResponse(GeneralApiResponse):
    next_cursor: Optional[str]
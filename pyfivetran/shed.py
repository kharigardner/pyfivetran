from __future__ import annotations # for | union syntax

from typing import TypedDict, Dict, Any, Optional

BASE_API_URL = 'https://api.fivetran.com'
API_VERSION = "v1"

class GeneralApiResponse(TypedDict):
    code: str | int
    message: Optional[str]
    data: Optional[Dict[str, Any]]
    
class ApiError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class PaginatedApiResponse(GeneralApiResponse):
    next_cursor: Optional[str]
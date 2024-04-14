from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import pytz

class REQUEST(BaseModel):
    item_id: int = 0
    
def date_time():
    utc_now = datetime.utcnow()
    utc_timezone = pytz.timezone('UTC')
    utc_now = utc_timezone.localize(utc_now)
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    thailand_now = utc_now.astimezone(thailand_timezone)
    thailand_now_str = thailand_now.strftime('%Y-%m-%d %H:%M:%S')
    return thailand_now_str

class USER_TEST(BaseModel):
    USERID: int = 0
    EMPID: int = 0
    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None
    DATETIME_LOGIN: datetime = date_time()

    class Config:
        alias_generator = lambda string: string.lower()
        allow_population_by_field_name = True

class RESPONSE_TEST(BaseModel):
    USERID: int = 0
    EMPID: int = 0
    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None
    DATETIME_LOGIN: datetime = date_time()

    class Config:
        alias_generator = lambda string: string.lower()
        allow_population_by_field_name = True

from datetime import datetime
from pydantic import BaseModel

class BookModel(BaseModel):
    name : str = '창세기'
    chapter: int = 1

class DateModel(BaseModel):
    start_date: datetime
    end_date: datetime

class PlanRequestModel(BaseModel):
    start_book: BookModel
    end_book: BookModel
    date_option: DateModel

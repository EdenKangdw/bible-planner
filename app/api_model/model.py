from pydantic import BaseModel

class PlanRequestModel(BaseModel):
    start_date = str
    end_date = str
    start_bible_idx = int
    end_bible_idx = int
    
    
from typing import Union
from fastapi import FastAPI

from api_model.model import PlanRequestModel

import logging

app = FastAPI()

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get plan
@app.get('/plan')
def plan(request: PlanRequestModel):
    logger.info('start request')

# book of bible list
@app.get('/bible/list')
def bible_list():
    return "BOOBKE"
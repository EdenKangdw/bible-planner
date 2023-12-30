from typing import Union
from fastapi import FastAPI, Query

from api_model.model import PlanRequestModel

import logging
import json 

app = FastAPI()
with open("bible_books.json", "r") as json_file:
    bible_books = json.load(json_file)

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get plan
@app.get('/plan')
def plan(request: PlanRequestModel):
    logger.info('start request')

def get_total_chapters(book_name: str) -> int:
    """
    성경 책의 총 장 수를 반환합니다.
    """
    book_info = next((info for info in bible_books if info["name"] == book_name), None)
    return book_info["chapters"] if book_info else 0

from fastapi import FastAPI, Query

app = FastAPI()
with open("bible_books.json", "r") as json_file:
    bible_books = json.load(json_file)

def get_total_chapters(book_name: str) -> int:
    """
    성경 책의 총 장 수를 반환합니다.
    """
    book_info = next((info for info in bible_books if info["name"] == book_name), None)
    return book_info["chapters"] if book_info else 0

@app.get("/bible/index")
def get_chapter_index(book: str = Query(..., title="Book Name", description="The name of the book"), chapter: int = Query(..., title="Chapter Number", description="The chapter number")):
    """
    Get the total chapter number of a specific book and the overall chapter number.
    """
    book = book.capitalize()  # 입력된 book을 소문자로 변환하여 일관성 부여

    # 입력된 book이 성경에 있는지 확인
    total_chapters = get_total_chapters(book)

    if total_chapters:
        if 1 <= chapter <= total_chapters:
            # 직접 반복문을 사용하여 인덱스 찾기
            index = 0
            for i, info in enumerate(bible_books):
                if info["name"] == book:
                    index = i
                    break
            
            # 각 책의 총 장 수를 합하여 전체 장 번호 계산
            total_chapter_number = sum(info["chapters"] for info in bible_books[:index]) + chapter
            return {"book": book, "chapter": chapter, "total_chapters": total_chapters, "total_chapter_number": total_chapter_number}
        else:
            return {"error": "Invalid chapter number. Please provide a valid chapter number."}
    else:
        return {"error": "Book not found. Please provide a valid book name."}

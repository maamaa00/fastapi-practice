from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

memos = []

class Memo(BaseModel):
    id: int
    text: str

class MemoCreate(BaseModel):
    text: str

next_id = 0

@app.get("/")
def read_root():
    return {"message": "Memo API"}

@app.get("/memos")
def get_memos():
    return memos

@app.post("/memos")
def create_memo(memo: MemoCreate):
    global next_id

    new_memo = {
        "id": next_id,
        "text": memo.text
    }

    memos.append(new_memo)
    next_id += 1
    return new_memo

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    for i, memo in enumerate(memos):
        if memo["id"] == memo_id:
            return memos.pop(i)

    raise HTTPException(status_code=404, detail="Memo not found")
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

memos = []

class Memo(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Memo API"}

@app.get("/memos")
def get_memos():
    return memos

@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return memo

# 最低限
# @app.delete("/memos/{memo_id}")
# def delete_memo(memo_id: int):
#     delete_memo = memos.pop(memo_id)
#     return delete_memo

# 存在チェック
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    if memo_id >= len(memos):
        raise HTTPException(status_code=404, detail="Memo not found")
    
    delete_memo = memos.pop(memo_id)
    return delete_memo
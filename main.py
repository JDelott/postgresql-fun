from typing import Union
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jacobdelott:postgres@localhost:5432/postgres-fun", echo=True
)


from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

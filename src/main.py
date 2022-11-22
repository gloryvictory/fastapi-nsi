from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: intgender: str


with open('people.json','r') as f:
    people = json.load(f)


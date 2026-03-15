from pydantic import BaseModel

class UserCreate(BaseModel):

    username: str
    password: str


class Login(BaseModel):

    username: str
    password: str


class DocumentCreate(BaseModel):

    title: str
    company_name: str
    document_type: str
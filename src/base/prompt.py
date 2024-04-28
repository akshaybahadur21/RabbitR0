from pydantic import BaseModel


class Prompt(BaseModel):
    id: str
    text: str
    retry: str

    def __hash__(self):
        return hash(tuple(self))
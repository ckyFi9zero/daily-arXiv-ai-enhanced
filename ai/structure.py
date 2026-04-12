from pydantic import BaseModel, Field

class Structure(BaseModel):
    tldr: str = Field(description="A brief TL;DR summary, written in the required language")
    motivation: str = Field(description="The motivation of this paper, written in the required language")
    method: str = Field(description="The method of this paper, written in the required language")
    result: str = Field(description="The result of this paper, written in the required language")
    conclusion: str = Field(description="The conclusion of this paper, written in the required language")

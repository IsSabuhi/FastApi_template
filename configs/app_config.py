
from pydantic.fields import Field
from pydantic_settings import BaseSettings

class Envs(BaseSettings):
    TITLE_APP: str
    DESCRIPTION_APP: str
    HOST: str = Field(default='0.0.0.0')
    PORT: int = Field(default=8080)

    class Config:
        env_file = ".env"

envs = Envs()
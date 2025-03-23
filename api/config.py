from dataclasses import dataclass

from dotenv import load_dotenv, find_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv(find_dotenv())


class Config(BaseSettings):
    FAKE_PERSONAL_GRPC_ADDRESS: str = Field(..., env="FAKE_PERSONAL_GRPC_ADDRESS")
    HOST: str = Field(..., env="HOST")
    PORT: int = Field(..., env="PORT")


config = Config()

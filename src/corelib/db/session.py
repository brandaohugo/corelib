from typing import Annotated
from typing import Generator

from corelib.engine import engine
from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import create_engine



def get_engine(db_uri: str):
    return create_engine(db_uri)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]




from sqlalchemy import create_engine


def get_engine(sqlalchemy_db_url: str):
    return create_engine(
        sqlalchemy_db_url
    )
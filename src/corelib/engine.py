from sqlalchemy import create_engine

from corelib.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
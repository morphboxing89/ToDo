from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config

engine = create_engine(config.SQLA_DB_URI)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

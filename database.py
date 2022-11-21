from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./buffet_db_sql.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

# Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_models():
    with engine.begin() as conn:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_models()
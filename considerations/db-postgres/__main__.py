from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = "myuser"
DB_PASS = "mypassword"
DB_HOST = "localhost" # use localhost when running outside docker
DB_PORT = "5432"
DB_NAME = "mydb" # match docker-compose database name

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(engine)


def main():
    session = SessionLocal()
    new_user = User(name="Alice", email="alice@example.com")
    session.add(new_user)
    session.commit()

    users = session.query(User).all()
    for u in users:
        print(u.id, u.name, u.email)

    session.close()


if __name__ == "__main__":
    main()

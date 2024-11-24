from typing import Annotated
from database import get_db_uri_sqlalchemy, get_db_uri
from fastapi import Depends, FastAPI, APIRouter, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str


# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# connect_args = {"check_same_thread": False}
db_uri = get_db_uri()
engine = create_engine(db_uri)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# yielding a database session allows FastAPI to inject the session into endpoint functions, 
# ensuring that the session is properly managed and closed after use
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
router = APIRouter(prefix="/api")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Create
@router.post("/heroes/")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    # "session" is a dependency-injected parameter. It's a Session object that we can use to interact with the database.
    session.add(hero) # Adds the new hero object to the session
    session.commit() # Commits the transaction, saving the new hero to the database.
    session.refresh(hero) # Refreshes the hero object with the latest data from the database, including any auto-generated fields like id.
    return hero

# Read
@router.get("/heroes/")
def read_heroes(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100,) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

# Read
@router.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# Delete
@router.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}

app.include_router(router)
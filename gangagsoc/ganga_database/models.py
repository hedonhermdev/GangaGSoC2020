from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary


Base = declarative_base()

# Model object to store a Job in the database.
class JobModel(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    data = Column("data", LargeBinary)

    def __repr__(self):
        return f"Job({self.id}, name={self.name})"

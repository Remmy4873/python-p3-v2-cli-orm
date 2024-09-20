from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure the engine to not output SQL statements (echo=False)
engine = create_engine('sqlite:///management.db', echo=False)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

# Base class for declarative models
Base = declarative_base()

# Uncomment to initialize database tables (if needed)
def init_db():
     import models.region
     import models.personnel
     Base.metadata.create_all(bind=engine)

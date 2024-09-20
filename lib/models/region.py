from sqlalchemy import Column, Integer, String
from database import Base, session

class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    constituency = Column(String, nullable=False)
    county = Column(String, nullable=False)

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(constituency=name).first()

    @classmethod
    def find_by_id(cls, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def create(cls, constituency, county):
        region = cls(constituency=constituency, county=county)
        session.add(region)
        session.commit()
        return region

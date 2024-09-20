from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
from models.region import Region

class Personnel(Base):
    __tablename__ = 'personnel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    profession = Column(String, nullable=False)
    contacts = Column(String, nullable=False)
    email = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    
    region = relationship("Region")

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def get_all_by_region(cls, region_id):
        return session.query(cls).filter_by(region_id=region_id).all()

    @classmethod
    def get_all_by_county(cls, county):
        regions = session.query(Region).filter_by(county=county).all()
        personnel = []
        for region in regions:
            personnel.extend(cls.get_all_by_region(region.id))
        return personnel

    @classmethod
    def get_all_by_constituency(cls, constituency):
        regions = session.query(Region).filter_by(constituency=constituency).all()
        personnel = []
        for region in regions:
            personnel.extend(cls.get_all_by_region(region.id))
        return personnel

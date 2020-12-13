from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Family(Base):
    """
    Родственники
    """
    __tablename__ = 'family'
    id = Column(Integer, primary_key=True)
    famName1 = Column(String(150))
    famName2 = Column(String(150))
    famName3 = Column(String(150))
    BirthDay = Column(Integer)
    BirthPlace = Column(String(150))
    Education = Column(String(150))
    FamilyStatus = Column(String(150))
    Machine = Column(String(150))
    Residence = Column(String(150))
    Registration = Column(String(150))
    CountryHouse = Column(String(150))
    PhoneHome = Column(Integer)
    PhoneMobile = Column(Integer)
    PhoneWork = Column(Integer)
    Position = Column(String(150))
    Rank = Column(String(150))
    Passport = Column(Integer)
    MilitaryIdentification = Column(Integer)
    SanitarTicket = Column(Integer)
    OfficialTicket = Column(Integer)
    Weight = Column(Integer)
    Height = Column(Integer)
    Photo = Column(String(150))
    
    id_worker = Column(Integer, ForeignKey('workers.id'))
    relate = Column(String(150))
    
    #description = Column(Text())
    #items = relationship('Item', backref='items')
    
    def __repr__(self):
        return '<Family> {}'.format(self.famName1)

    def __str__(self):
        return '<Family> {}'.format(self.famName1)


class Workers(Base):
    """
    Сотрудники
    """
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    WorkerName1 = Column(String(150))
    WorkerName2 = Column(String(150))
    WorkerName3 = Column(String(150))
    BirthDay = Column(Integer)
    BirthPlace = Column(String(150))
    Education = Column(String(150))
    FamilyStatus = Column(String(150))
    Machine = Column(String(150))
    Residence = Column(String(150))
    Registration = Column(String(150))
    CountryHouse = Column(String(150))
    PhoneHome = Column(Integer)
    PhoneMobile = Column(Integer)
    PhoneWork = Column(Integer)
    Position = Column(String(150))
    Rank = Column(String(150))
    Passport = Column(Integer)
    MilitaryIdentification = Column(Integer)
    SanitarTicket = Column(Integer)
    OfficialTicket = Column(Integer)
    Weight = Column(Integer)
    Height = Column(Integer)
    Photo = Column(String(150))
    
    Family = relationship('Family', backref='family')
    
    #description = Column(Text())
    #items = relationship('Item', backref='items')
    
    
    def __repr__(self):
        return '<Workers> {}'.format(self.WorkerName1)

    def __str__(self):
        return '<Workers> {}'.format(self.WorkerName1)

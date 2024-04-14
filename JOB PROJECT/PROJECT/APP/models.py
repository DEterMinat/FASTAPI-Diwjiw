from sqlalchemy import Column, Integer, String, DateTime
from database import Base_dev

class User(Base_dev):
    __table_args__ = {'schema': 'CUSTOMER'}
    __tablename__ = 'USER'
    
    USERID = Column(Integer, primary_key=True)
    EMPID = Column(Integer)
    USERNAME = Column(String)
    PASSWORD = Column(String)
    DATETIME_LOGIN = Column(DateTime)

class Emp(Base_dev):
    __table_args__ = {'schema': 'CUSTOMER'}
    __tablename__ = 'EMPLOYEE'
    EMPNAME = Column(String)
    EMPPASSWORD = Column(String)
    EMPID = Column(Integer, primary_key=True)
    JOB = Column(String)
    SALARY = Column(Integer)

    
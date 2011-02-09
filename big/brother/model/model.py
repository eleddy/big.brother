import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey



Base = declarative_base()
class UserView(Base):
    __tablename__ = 'userviews'
    id = Column(Integer, sa.Sequence('id_seq'), primary_key=True,)
    username = Column(String)
    date = Column(String)
    url = Column(String)
    uid = Column(String)
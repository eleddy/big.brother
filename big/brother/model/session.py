import os 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from big.brother.model import model

EVALUATIONS_CONNECTION_STRING = 'sqlite:////tmp/user_views.sqlite'
try:
    home = os.environ['CLIENT_HOME']
    homeDir = os.environ['CLIENT_HOME'] 
    # we want the var directory
    if home.count('var'):
        home = home.split("var")[0]
        homeDir = "%svar/sqlite"%home
        if not os.path.exists(homeDir):
            os.mkdir(homeDir)
    home = "%s/user_views.sqlite"%homeDir
    EVALUATIONS_CONNECTION_STRING = 'sqlite:///%s'%home
except: pass

# this has to be done globally I guess.
SQL_ENGINE = sa.create_engine(EVALUATIONS_CONNECTION_STRING) 
SQL_SESSION = sessionmaker(bind=SQL_ENGINE)
model.Base.metadata.create_all(SQL_ENGINE)
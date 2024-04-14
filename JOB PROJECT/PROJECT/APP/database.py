from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username_dev = 'avnadmin'
password_dev = 'AVNS_zqMQDqo3iF4I5VKnxcY'
hostname_dev = 'pg-294c11d9-tanakitsiriteerapan-0a3c.b.aivencloud.com'
port_dev = '26121'
service_name_dev = 'defaultdb'

# Construct the connection string
conn_dev = f'postgresql://{username_dev}:{password_dev}@{hostname_dev}:{port_dev}/{service_name_dev}'

# Create the SQLAlchemy engine
engine = create_engine(conn_dev)

# Create the base class for declarative class definitions
Base_dev = declarative_base()

# Create a sessionmaker to create sessions
SessionLocal_dev = sessionmaker(bind=engine, expire_on_commit=False)

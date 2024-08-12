from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir la URL de la base de datos directamente
DATABASE_URL = "mysql+pymysql://root:12345@db:3306/AutenticacionDB"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Configurar la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la bd y cerrarla
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
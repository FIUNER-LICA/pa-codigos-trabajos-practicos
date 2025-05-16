from modules.repositorio_concreto import RepositorioSQLAlchemy
from modules.config import crear_engine

def crear_repositorio():
    session = crear_engine()
    return RepositorioSQLAlchemy(session())
from modules.repositorio_concreto import RepositorioLibrosSQLAlchemy, RepositorioUsuariosSQLAlchemy
from modules.config import crear_engine

def crear_repositorio():
    session = crear_engine()
    repo_libro =  RepositorioLibrosSQLAlchemy(session())
    repo_usuario = RepositorioUsuariosSQLAlchemy(session())
    return repo_libro, repo_usuario
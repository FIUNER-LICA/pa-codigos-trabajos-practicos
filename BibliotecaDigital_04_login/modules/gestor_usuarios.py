from modules.dominio import Usuario
from modules.repositorio_abstracto import RepositorioAbstracto
from werkzeug.security import generate_password_hash, check_password_hash


class GestorDeUsuarios:
    def __init__(self, repo: RepositorioAbstracto):
        self.__repo = repo

    def registrar_nuevo_usuario(self, nombre, email, password):
        if self.__repo.obtener_registro_por_filtro("email", email):
            raise ValueError("El usuario ya está registrado, por favor inicie sesión")
        pass_encriptada = generate_password_hash(password= password,
                                                 method= 'pbkdf2:sha256',
                                                 salt_length=8
                                                )
        usuario = Usuario(None, nombre, email, pass_encriptada)
        self.__repo.guardar_registro(usuario)

    def autenticar_usuario(self, email, password):
        usuario = self.__repo.obtener_registro_por_filtro("email", email)
        if not usuario:
            raise ValueError("El usuario no está registrado")
        elif not check_password_hash(usuario.password, password):
            raise ValueError("Contraseña incorrecta")
        return usuario.to_dict()
        
    def cargar_usuario(self, id_usuario):
        return self.__repo.obtener_registro_por_filtro("id", id_usuario).to_dict()
        
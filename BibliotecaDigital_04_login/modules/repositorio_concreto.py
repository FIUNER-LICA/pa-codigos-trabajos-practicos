from modules.dominio import Libro, Usuario
from modules.repositorio_abstracto import RepositorioAbstracto
from modules.modelos import ModeloLibro, ModeloUsuario

    
class RepositorioLibrosSQLAlchemy(RepositorioAbstracto):
    def __init__(self, session):
        self.__session = session
        tabla_libro = ModeloLibro()
        tabla_libro.metadata.create_all(self.__session.bind)

    def guardar_registro(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("El parámetro no es una instancia de la clase Libro")
        modelo_libro = self.__map_entidad_a_modelo(libro)
        self.__session.add(modelo_libro)
        self.__session.commit()

    def obtener_todos_los_registros(self):
        modelo_libros = self.__session.query(ModeloLibro).all()
        return [self.__map_modelo_a_entidad(libro) for libro in modelo_libros]   
    
    def modificar_registro(self, libro_modificado):
        if not isinstance(libro_modificado, Libro):
            raise ValueError("El parámetro no es una instancia de la clase Libro")
        register = self.__session.query(ModeloLibro).filter_by(id=libro_modificado.id).first()
        register.nombre = libro_modificado.nombre
        register.autor = libro_modificado.autor
        register.calificacion = libro_modificado.calificacion
        self.__session.commit()

    def obtener_registro_por_filtro(self, filtro, valor):
        modelo_libro = self.__session.query(ModeloLibro).filter_by(**{filtro:valor}).first()
        return self.__map_modelo_a_entidad(modelo_libro) if modelo_libro else None
    
    def obtener_registros_segun_filtro(self, filtro, valor):
        modelo_libros = self.__session.query(ModeloLibro).filter_by(**{filtro:valor}).all()
        return [self.__map_modelo_a_entidad(libro) for libro in modelo_libros]
    
    def eliminar_registro(self, id):
        register = self.__session.query(ModeloLibro).filter_by(id=id).first()
        self.__session.delete(register)
        self.__session.commit()
    
    def __map_entidad_a_modelo(self, entidad: Libro):
        return ModeloLibro(
            nombre=entidad.nombre,
            autor=entidad.autor,
            calificacion=entidad.calificacion,
            id_usuario=entidad.id_usuario
        )
    
    def __map_modelo_a_entidad(self, modelo: ModeloLibro):
        return Libro(
            modelo.id,
            modelo.nombre,
            modelo.autor,
            modelo.calificacion,
            modelo.id_usuario 
        )
    
class RepositorioUsuariosSQLAlchemy(RepositorioAbstracto):
    def __init__(self, session):
        self.__session = session
        tabla_usuario = ModeloUsuario()
        tabla_usuario.metadata.create_all(self.__session.bind)

    def guardar_registro(self, usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError("El parámetro no es una instancia de la clase Usuario")
        modelo_usuario = self.__map_entidad_a_modelo(usuario)
        self.__session.add(modelo_usuario)
        self.__session.commit()

    def obtener_todos_los_registros(self):
        modelo_usuarios = self.__session.query(ModeloUsuario).all()
        return [self.__map_modelo_a_entidad(usuario) for usuario in modelo_usuarios]   
    
    def modificar_registro(self, usuario_modificado):
        if not isinstance(usuario_modificado, Usuario):
            raise ValueError("El parámetro no es una instancia de la clase Usuario")
        register = self.__session.query(ModeloUsuario).filter_by(id=usuario_modificado.id).first()
        register.nombre = usuario_modificado.nombre
        register.apellido = usuario_modificado.apellido
        register.email = usuario_modificado.email
        register.password = usuario_modificado.password
        self.__session.commit()

    def obtener_registro_por_filtro(self, filtro, valor):
        modelo_usuario = self.__session.query(ModeloUsuario).filter_by(**{filtro:valor}).first()
        return self.__map_modelo_a_entidad(modelo_usuario) if modelo_usuario else None
    
    def eliminar_registro(self, id):
        register = self.__session.query(ModeloUsuario).filter_by(id=id).first()
        self.__session.delete(register)
        self.__session.commit()
    
    def __map_entidad_a_modelo(self, entidad: Usuario):
        return ModeloUsuario(
            nombre=entidad.nombre,
            email=entidad.email,
            password=entidad.password
        )
    
    def __map_modelo_a_entidad(self, modelo: ModeloUsuario):
        return Usuario(
            modelo.id,
            modelo.nombre,
            modelo.email,
            modelo.password
        )
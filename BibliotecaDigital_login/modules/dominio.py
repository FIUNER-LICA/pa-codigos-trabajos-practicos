class Libro:
    def __init__(self, p_id, p_nombre, p_autor, p_calificacion, p_id_usuario):
        self.id = p_id
        self.nombre = p_nombre
        self.autor = p_autor
        self.calificacion = p_calificacion
        self.id_usuario = p_id_usuario

    @property
    def id(self):
        return self.__id
    
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def calificacion(self):
        return self.__calificacion
    
    @id.setter
    def id(self, p_id):
        if p_id != None:
            if not isinstance(p_id, int):
                raise ValueError("El id del libro debe ser un número entero")
            self.__id = p_id
        else:
            self.__id = None
    
    @id_usuario.setter
    def id_usuario(self, p_id_usuario):
        if p_id_usuario != None:
            if not isinstance(p_id_usuario, int):
                raise ValueError("El id del usuario debe ser un número entero")
            self.__id_usuario = p_id_usuario
        else:
            self.__id_usuario = None
    
    @nombre.setter
    def nombre(self, p_nombre:str):
        if not isinstance(p_nombre, str) or p_nombre.strip() == "":
            raise ValueError("El nombre del libro debe ser un string y no debe estar vacío")
        self.__nombre = p_nombre.strip()
        
    @autor.setter
    def autor(self, p_autor:str):
        if not isinstance(p_autor, str) or p_autor.strip() == "":
            raise ValueError("El nombre del autor debe ser un string y no debe estar vacío")
        self.__autor = p_autor.strip()

    @calificacion.setter
    def calificacion(self, p_calificacion):
        if not isinstance(p_calificacion, (float, int)):
            raise ValueError("La calificación del libro debe ser un número entre 0 y 10")
        if p_calificacion < 0 or p_calificacion > 10:
            raise ValueError("La calificación del libro debe ser un número entre 0 y 10")
        self.__calificacion = p_calificacion


    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "autor": self.autor,
            "calificacion": self.calificacion,
            "id_usuario": self.id_usuario
        }

    def __str__(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Calificación: {self.calificacion}"


class Usuario:
    def __init__(self, p_id, p_nombre, p_email, p_password):
        self.id = p_id
        self.nombre = p_nombre
        self.email = p_email
        self.password = p_password

    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    @id.setter
    def id(self, p_id):
        if p_id != None:
            if not isinstance(p_id, int):
                raise ValueError("El id del usuario debe ser un número entero")
            self.__id = p_id
        else:
            self.__id = None
    
    @nombre.setter
    def nombre(self, p_nombre:str):
        if not isinstance(p_nombre, str) or p_nombre.strip() == "":
            raise ValueError("El nombre del usuario debe ser un string y no debe estar vacío")
        self.__nombre = p_nombre.strip()
        
    @email.setter
    def email(self, p_email:str):
        if not isinstance(p_email, str) or p_email.strip() == "":
            raise ValueError("El email de usuario debe ser un string y no debe estar vacío")
        self.__email = p_email.strip()
        
    @password.setter
    def password(self, password:str):
        self.__password = password

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password
        }
            

class Libro:
    def __init__(self, titulo, autor, paginas, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.copias_disponibles = copias_disponibles

    def prestar(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            return True
        return False

    def devolver(self):
        self.copias_disponibles += 1

class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro.titulo)
            print(f"Prestado: {libro.titulo} a {self.nombre}")
        else:
            print(f"No disponible: {libro.titulo}")

    def devolver_libro(self, libro):
        if libro.titulo in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro.titulo)
            print(f"Devuelto: {libro.titulo} por {self.nombre}")

class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar_libro(self, miembro, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            miembro.tomar_prestado(libro)
        else:
            print(f"{titulo} no está en la biblioteca.")

    def devolver_libro(self, miembro, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            miembro.devolver_libro(libro)

# Uso
biblio = Biblioteca("Biblioteca Central", "Calle Falsa 123")
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1216, 5)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, 3)

biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)

miembro1 = Miembro("Diego Ibáñez", 1)

biblio.prestar_libro(miembro1, "El Señor de los Anillos")
biblio.prestar_libro(miembro1, "Don Quijote de la Mancha")
biblio.devolver_libro(miembro1, "El Señor de los Anillos")

class Biblioteca:
    class Horariodeatencion:
        def __init__(self, apertura, cierre):
            self.apertura = apertura
            self.cierre = cierre

        def mostrarHorario(self):
            return f"Abre: {self.apertura}, Cierra: {self.cierre}"

        def __str__(self):
            return self.mostrarHorario()

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Biblioteca.Horariodeatencion("08:00", "18:00")

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo("08/05/2026", "15/05/2026", estudiante, libro)
        self.prestamos.append(prestamo)

    def mostrarEstado(self):
        print("BIBLIOTECA")
        print("Nombre:", self.nombre)
        print("Horario:", self.horario)

        print("\nLIBROS DISPONIBLES")
        for libro in self.libros:
            print(libro)

        print("\nAUTORES REGISTRADOS")
        for autor in self.autores:
            print(autor)

        print("\nPRESTAMOS ACTIVOS")
        for prestamo in self.prestamos:
            print(prestamo.estudiante, "prestó", prestamo.libro)

    def cerrarBiblioteca(self):
        print("\nLa biblioteca ha cerrado")
        self.prestamos.clear()
        print("Todos los préstamos fueron eliminados")


class Libro:
    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrarPagina(self):
            return f"Pagina {self.numero}: {self.contenido}"

        def __str__(self):
            return self.mostrarPagina()

    def __init__(self, Titulo, isbn, contenidodepaginas):
        self.Titulo = Titulo
        self.isbn = isbn
        self.paginas = []

        numero = 1

        for contenido in contenidodepaginas:
            pagina = Libro.Pagina(numero, contenido)
            self.paginas.append(pagina)
            numero += 1

    def leer(self):
        print("LIBRO")
        print("Titulo:", self.Titulo)
        print("ISBN:", self.isbn)

        print("\nCONTENIDO")
        for pagina in self.paginas:
            print(pagina)

    def __str__(self):
        return f"{self.Titulo}, ISBN: {self.isbn}"


class Autor:
    def __init__(self, Nombre, Nacionalidad):
        self.Nombre = Nombre
        self.Nacionalidad = Nacionalidad

    def mostrarInfo(self):
        return f"Nombre: {self.Nombre}, Nacionalidad: {self.Nacionalidad}"

    def __str__(self):
        return self.mostrarInfo()


class Estudiante:
    def __init__(self, Codigodeestudiante, Nombre):
        self.Codigodeestudiante = Codigodeestudiante
        self.Nombre = Nombre

    def mostrarInfo(self):
        return f"Codigo: {self.Codigodeestudiante}, Nombre: {self.Nombre}"

    def __str__(self):
        return self.mostrarInfo()


class Prestamo:
    def __init__(self, fechaprestamo, fechadevolucion, estudiante, libro):
        self.fechaprestamo = fechaprestamo
        self.fechadevolucion = fechadevolucion
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        return f"Estudiante: {self.estudiante}, Libro: {self.libro}, Fecha del prestamo: {self.fechaprestamo}, Fecha de devolucion: {self.fechadevolucion}"

    def __str__(self):
        return self.mostrarInfo()


b1 = Biblioteca("Biblioteca Central")

a1 = Autor("Gabriel Garcia Marquez", "Colombiano")
a2 = Autor("Mario Vargas Llosa", "Peruano")

b1.agregarAutor(a1)
b1.agregarAutor(a2)

l1 = Libro("Cien años de soledad", "ISBN123", ["Inicio del libro", "Desarrollo del libro", "Final del libro"])
l2 = Libro("La ciudad y los perros", "ISBN456", ["Pagina 1", "Pagina 2"])

b1.agregarLibro(l1)
b1.agregarLibro(l2)

e1 = Estudiante(1001, "Juan Perez")

b1.prestarLibro(e1, l1)

print("\n")
b1.mostrarEstado()

print("\nDETALLE PRESTAMO")
for prestamo in b1.prestamos:
    print(prestamo)

print("\nLEER LIBRO")
l1.leer()

print("\nHORARIO")
print(b1.horario.mostrarHorario())

print("\n")
b1.cerrarBiblioteca()
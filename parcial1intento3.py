#parcial 1
#Raúl Santiago Bermúdez Camacho - Parcial 1 – Programación Orientada a Objetos

class Libro:
    def __init__(self, titulo, autor, categoria, numero_de_serie):
        self.__titulo = titulo              # privado
        self.__autor = autor                # privado
        self.__categoria = categoria        # privado
        self.__numero_de_serie = numero_de_serie  # privado

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_categoria(self):
        return self.__categoria

    def get_numero_de_serie(self):
        return self.__numero_de_serie

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre   # protegido

    def get_nombre(self):
        return self._nombre

class Biblioteca:
    def __init__(self):
        self.__libros = []      # privado
        self.__usuarios = []    # privado
        self.__categorias = ["Ciencia ficción", "Literatura", "Ingeniería", "Romance"]

    def registrar_libro(self):
        print("===||  Registro de nuevo libro  ||===")
        titulo = input("Título: ")
        autor = input("Autor: ")
        print("Categorías disponibles:")
        for idx, cat in enumerate(self.__categorias):
            print(f"{idx+1}. {cat}")
        cat_idx = int(input("Seleccione categoría (número): ")) - 1
        if 0 <= cat_idx < len(self.__categorias):
            categoria = self.__categorias[cat_idx]
            numero_de_serie = input("Número de serie: ")
            libro = Libro(titulo, autor, categoria, numero_de_serie)
            self.__libros.append(libro)
            print("YEIII libro registrado exitosamente.\n")
        else:
            print("Categoría inválida.\n")

    def registrar_usuario(self):
        print("===|| Registro de nuevo usuario ||===")
        nombre = input("Nombre: ")
        usuario = Persona(nombre)
        self.__usuarios.append(usuario)
        print(f"{usuario.get_nombre()}, su usuario registrado exitosamente.\n")

    def listar_libros(self):
        print("=== Libros registrados ===")
        if not self.__libros:
            print("No hay libros registrados.\n")
        else:
            for libro in self.__libros:
                print(f"Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Categoría: {libro.get_categoria()}, Serie: {libro.get_numero_de_serie()}")
            print()

    def listar_usuarios(self):
        print("=== Usuarios registrados ===")
        if not self.__usuarios:
            print("No hay usuarios registrados.\n")
        else:
            for usuario in self.__usuarios:
                print(f"Nombre: {usuario.get_nombre()}")
            print()

    def mostrar_menu(self):
        while True:
            print("  |=========================================================||")
            print("  ||======================= Menú Biblioteca ================||")
            print("  |=========================================================||")
            print("  |1.                    Registrar nuevo libro               |")
            print("  |__________________________________________________________|")
            print("  |2.                   Registrar nuevo usuario              |")
            print("  |__________________________________________________________|")
            print("  |3.                    Listar libros                       |")
            print("  |__________________________________________________________|")
            print("  |4.                    Listar usuarios                     |")
            print("  |__________________________________________________________|")
            print("  |5.                         Salir                          |")
            print("  |__________________________________________________________|")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_libro()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                self.listar_libros()
            elif opcion == "4":
                self.listar_usuarios()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida.\n")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.mostrar_menu()
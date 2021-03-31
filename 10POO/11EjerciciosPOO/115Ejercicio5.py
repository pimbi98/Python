#Ejercicio 1
# Crear un programa con tres clases 
# Universidad, 
# con atributos nombre (Donde se almacena el nombre de la Universidad). 
# Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante 
# con un objeto llamado persona.

class Universidad():
    Nombre  = "Nombre Universidad"

class Carrera():
    Especialidad = "Especialidad Estudiante."

class Estudiante():
    Nombre  = "Nombre Estudiante"
    Edad    = 0

UniversidadJose = Universidad()
UniversidadJose.Nombre = "Universidad Nacional de Rosario (Argentina)"

CarreraJose = Carrera()
CarreraJose.Especialidad = "Licenciado en Ciencias de la Computación"

EstudianteJose = Estudiante()
EstudianteJose.Nombre = "José Pérez"
EstudianteJose.Edad = 23


print("Alumno: ", EstudianteJose.Nombre, "\n Edad: ",EstudianteJose.Edad, "\n Estudia: ", CarreraJose.Especialidad, "\n En: ", UniversidadJose.Nombre)
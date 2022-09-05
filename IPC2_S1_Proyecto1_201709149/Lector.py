from tkinter import filedialog
from tkinter import *
from xml.dom import minidom

import Lista_pacientes
import Paciente

class Lector:

    file_root = None
    file = None
    read_done = False
    procesed_data = False

    lista_de_pacientes_procesados = None
    piso_calculado = None

    def open_a_file(self):
        print("Se cargará un archivo...")
        open_correctly = True
        try:
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                filetypes=(("Input Files [IPC2]", "*.xml"), ("all files", "*.*")))            
            self.file_root = root.filename            
        except:
            print("Error de directorio")
            open_correctly = False

        if open_correctly == True:
            if self.file_root == "":
                print("Dirección vacía.")
                print("")

        return open_correctly
    
    def read_file(self):
        load_correctly = True
        print("")
        print("Se leerá el directorio...")
        try:
            self.file = minidom.parse(self.file_root)
        except:
            print("Archivo no encontrado o no válido.")
            print("")
            load_correctly = False

        return load_correctly

    def proces_file(self):
        if self.procesed_data == False:

            print("Procesando información de pacientes...")
            print("")
            self.lista_de_pacientes_procesados = Lista_pacientes.Lista_pacientes()
            lista_de_pacientes = self.file.getElementsByTagName("paciente")        
            cant_pacientes = len(lista_de_pacientes)

            if cant_pacientes != 0:

                for i in range(cant_pacientes):
                    print("Obteniendo información del paciente: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    try:
                        # lista_de_pacientes[i].attributes["nombre"].value
                        personal_data = lista_de_pacientes[i].getElementsByTagName("datospersonales")[0]
                        name = personal_data.getElementsByTagName("nombre")[0].childNodes[0].data
                        age = personal_data.getElementsByTagName("edad")[0].childNodes[0].data
                        print("     Paciente encontrado con nombre: " + name + ", edad: " + age)
                    except:                        
                        print("No se han encontrado los atributos requerridos para el paciente. ")
                        print("El paciente será omitido.")
                        continue
                   
                    period = lista_de_pacientes[i].getElementsByTagName("periodos")[0].childNodes[0].data
                    m = lista_de_pacientes[i].getElementsByTagName("m")[0].childNodes[0].data

                    # Recoleección de datos de celdas para el i-ésimo paciente desde aquí:

                    nuevo_paciente = Paciente.Paciente(name, age, period, m)
                    self.lista_de_pacientes_procesados.agregar(nuevo_paciente)

                print("")
                print("Información de teerrenos procesada correctamente.")
                print("")

            else:
                print("")
                print("No se han encontrado pacientes.")
                print("")
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")

    def reset_all_r(self):
        self.file_root = None
        self.file = None
        self.read_done = False
        self.lista_de_pacientes_procesados = None
        self.procesed_data = False
        self.piso_calculado = None
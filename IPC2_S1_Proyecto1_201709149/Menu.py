import Lector as LectorClass
import Escritor as WriterClass

import sys
from tkinter import filedialog
from tkinter import *
import re
import os

class Menu:

    lector_obj = LectorClass.Lector()
    escritor_obj = WriterClass.Escritor()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ╔═══════════════════════════════════════════════════════════════════════════╗")
        print(" ║                        M E N Ú   P R I N C I P A L                        ║")
        print(" ╚═══════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("     [1]  Cargar datos desde archivo")
        print("     [2]  Diagnosticar paciente")
        print("     [3]  Generar gráfica (patrón inicial)")
        print("     [4]  Generar gráfica (patrón final)")
        print("     [5]  Salir")
        print("")
        print(" Escriba el número de acuerdo a la opción que desee: ")

    def imprimir_menu_de_carga(self):
        print("")
        print(" ---------------- Carga de archivos: ----------------")
        print("")
        print(" [1] Escribir dirección")
        print(" [2] Seleccionar archivo")
        print(" [3] Regresar al menú principal")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

 
    def mostrar_pacientes_disponibles(self, modo):
        while True:
            n = 1
            temp = self.lector_obj.lista_de_pacientes_procesados.first

            print("")
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1
            
            if modo == "b":
                print(" [" + str(n) + "] Todos (Estructura de entrada)")
                print(" [" + str(n+1) + "] Cancelar")

            print("")
            if modo == "a":
                print("Escriba el número correspondiente al paciente que desee diagnosticar:")
            elif modo == "b":
                print("Escriba el número correspondiente al paciente que desee diagnosticar, o 'Todos' para la estructura de entrada.")

                p_option = 0
                try:
                    p_option = int(input())
                except:
                    print("Opción no válida, ingrese un número.")
                    continue

                total_patients = self.lector_obj.lista_de_pacientes_procesados.cant
                if p_option <= total_patients:
                    p_selected = self.lector_obj.lista_de_pacientes_procesados.buscar_por_posicion(p_option)
                    print("Se diagnosticará al paciente: " + p_selected.name)
                elif p_option == total_patients + 1:
                    print("Diagnosticar todos")
                elif p_option == total_patients + 2:
                    print("")
                    break

    def iniciar_menu(self):
        print("")
        while(self.exit == False):
            self.imprimir_menu()
            try:
                selected_option = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")
                continue
            if selected_option == 1:
                back = False
                while back == False:
                    self.imprimir_menu_de_carga()
                    selected_option_l = 0
                    try:
                        selected_option_l = int(input())
                    except:
                        print("Error de entrada. Intente de nuevo")
                        print("")
                        continue

                    if selected_option_l == 1:
                        if self.lector_obj.read_done:
                            print("Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print("Escriba una ruta específica:")
                        root = input()
                        if root == "":
                            print("Dirección vacía.")
                            print("")
                        else:
                            self.lector_obj.file_root = root
                            if self.lector_obj.read_file():
                                print("Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True
                                self.lector_obj.proces_file()                                
                                back = True
                    elif selected_option_l == 2:
                        if self.lector_obj.read_done:
                            print("Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print("Elija el archivo para cargarlo:")

                        if self.lector_obj.open_a_file():
                            if self.lector_obj.read_file():
                                print("Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True
                                self.lector_obj.proces_file()                                
                                back = True

                    elif selected_option_l == 3:
                        print("Regresando al menú principal.")
                        print("")
                        back = True
                    else:
                        print("La opción no es válida, intente de nuevo.")
                        print("")                
            elif selected_option == 2:
                print("")
                lista = self.lector_obj.lista_de_pacientes_procesados
                sin_pacientes = False
                if lista != None:
                    if lista.first != None:
                        print("---------------- Pacientes disponibles ----------------")
                        todos = self.mostrar_pacientes_disponibles("b")
                    else:
                        sin_pacientes = True
                else:
                    sin_pacientes = True
                if sin_pacientes:
                    print(" (!) No se encuentran pacientes disponibles actualmente.")
                    print("")
            elif selected_option == 3:
                print("Se leerán los datos del archivo cargado...")
                if self.lector_obj.read_done:
                    self.lector_obj.proces_file()
                    Todos = self.mostrar_pacientes_disponibles("a")
                    paciente_a_graficar = input()

                    if paciente_a_graficar == "Todos":
                        print("")
                        #print("*** Se graficará la estructura del archivo de entrada.")
                        #self.escritor_obj.writeDOT_T(self.lector_obj.lista_de_pacientes_procesados)                        
                    else:
                        paciente_a_graficar = self.lector_obj.lista_de_pacientes_procesados.buscar_por_nombre(paciente_a_graficar)
                        print("")
                        if paciente_a_graficar == None:
                            print("(!) paciente no encontrado.")
                            print("--- Regresando al menú principal...")
                            print("")
                        else:
                            print("*** Se graficará el paciente: " + paciente_a_graficar.name)
                            self.escritor_obj.writeDOT_G(paciente_a_graficar, False)
                            print("")
            elif selected_option == 4:
                print("Se leerán los datos del archivo cargado...")
                if self.lector_obj.read_done:
                    self.lector_obj.proces_file()
                    Todos = self.mostrar_pacientes_disponibles("a")
                    paciente_a_graficar = input()

                    if paciente_a_graficar == "Todos":
                        print("")
                        #print("*** Se graficará la estructura del archivo de entrada.")
                        #self.escritor_obj.writeDOT_T(self.lector_obj.lista_de_pacientes_procesados)                        
                    else:
                        paciente_a_graficar = self.lector_obj.lista_de_pacientes_procesados.buscar_por_nombre(paciente_a_graficar)
                        print("")
                        if paciente_a_graficar == None:
                            print("(!) paciente no encontrado.")
                            print("--- Regresando al menú principal...")
                            print("")
                        else:
                            print("*** Se graficará el paciente: " + paciente_a_graficar.name)
                            self.escritor_obj.writeDOT_G(paciente_a_graficar, True)
                            print("")

                else:
                    print("No se ha cargado un archivo.")
                    print("")
            elif selected_option == 5:
                self.exit = True
                print("")
                print("Se cerrará el programa.")
                print(". . .")
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")
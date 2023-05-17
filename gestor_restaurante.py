"""
Gestor de Restaurantes
"""

from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

OPERADOR = ""
precios_comidas = [260, 790, 360, 700, 3000, 200, 80, 150]
precios_bebidas = [25, 37, 35, 30, 45, 85, 95, 90]
precios_postres = [50, 135, 130, 45, 80, 95, 130, 130]

def click_boton(numero):
    """Función para los botones de la calculadora"""
    global OPERADOR
    lista_operadores = ["*", "+", "-", "/"]
    if f"-{OPERADOR}"[-1] not in lista_operadores or numero not in lista_operadores:
        OPERADOR = OPERADOR + numero
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(END, OPERADOR)

def borrar():
    """Función para la tecla Borrar (B)"""
    global OPERADOR
    OPERADOR = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    """Función para realizar el cálculo deseado"""
    global OPERADOR
    try:
        resultado = str(eval(OPERADOR))
        OPERADOR = resultado
    except ImportError:
        resultado = "error"
        OPERADOR = ""
    finally:
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, resultado)

def revisar_check():
    """Función para configurar los checkbuttons"""
    # Comidas
    for x in reversed(range(len(cuadros_comidas))):
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == "0":
                cuadros_comidas[x].delete(0, END)
                cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set("0")

    # Bebidas
    for x in reversed(range(len(cuadros_bebidas))):
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == "0":
                cuadros_bebidas[x].delete(0, END)
                cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set("0")

    # Postres
    for x in reversed(range(len(cuadros_postres))):
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
                cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")

def total():
    """Función para calcular el Total"""
    # Comidas
    sub_total_comidas = 0
    p = 0
    for cantidad in texto_comidas:
        sub_total_comidas = sub_total_comidas + (float(cantidad.get()) * precios_comidas[p])
        p += 1

    # Bebidas
    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebidas[p])
        p += 1

    # Postres
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    # Sub Total
    sub_total = sub_total_comidas + sub_total_bebidas + sub_total_postres
    impuestos = sub_total * 0.16
    gran_total = sub_total + impuestos

    var_costo_comidas.set(f"$ {round(sub_total_comidas, 2)}")
    var_costo_bebidas.set(f"$ {round(sub_total_bebidas, 2)}")
    var_costo_postres.set(f"$ {round(sub_total_postres, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuestos.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(gran_total, 2)}")

def recibo():
    """Función para generar el Recibo"""
    global NUM_RECIBO, FECHA
    total()
    texto_recibo.configure(state="normal")
    texto_recibo.delete(1.0, END)
    NUM_RECIBO = f"N# - {random.randint(1000, 9999)}"
    FECHA = datetime.datetime.now()
    # fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    fecha_recibo = f"{FECHA.strftime('%d/%m/%Y - %H:%M:%S')}"
    texto_recibo.insert(END, f"Datos:\t{NUM_RECIBO}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 54 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\t\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 54 + "\n")

    x = 0
    for comidas in texto_comidas:
        if comidas.get() != "0":
            costo_comidas = round((float(comidas.get()) * precios_comidas[x]), 2)
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comidas.get()}\t\t"
                                f"$ {costo_comidas:.2f}\n")
        x += 1

    x = 0
    for bebidas in texto_bebidas:
        if bebidas.get() != "0":
            costo_bebidas = round((float(bebidas.get()) * precios_bebidas[x]), 2)
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebidas.get()}\t\t"
                                f"$ {costo_bebidas:.2f}\n")
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != "0":
            costo_postres = round((float(postres.get()) * precios_postres[x]), 2)
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t\t"
                                f"$ {costo_postres:.2f}\n")
        x += 1

    texto_recibo.insert(END, f"-" * 54 + "\n")
    texto_recibo.insert(END, f" Costo de la Comida: \t\t\t{var_costo_comidas.get()}\n")
    texto_recibo.insert(END, f" Costo de las Bebidas: \t\t\t{var_costo_bebidas.get()}\n")
    texto_recibo.insert(END, f" Costo de los Postres: \t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"-" * 54 + "\n")
    texto_recibo.insert(END, f" Sub-Total: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f" Impuestos: \t\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(END, f" Total: \t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 54 + "\n")
    texto_recibo.insert(END, "Lo esperamos pronto...")
    texto_recibo.configure(state="disabled")

def guardar():
    """Función para guardar el recibo en un archivo .txt"""
    info_recibo = texto_recibo.get(1.0, END)
    nom_archivo = NUM_RECIBO + "-" + FECHA.strftime("%d-%m-%Y")
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt", initialfile=nom_archivo)
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo(title="Información", message="Su recibo ha sido guardado correctamente")

def resetear():
    """Función para resetear la aplicación"""
    texto_recibo.configure(state="normal")
    texto_recibo.delete(0.1, END)
    texto_recibo.configure(state="disabled")
    for texto in texto_comidas:
        texto.set("0")
    for texto in texto_bebidas:
        texto.set("0")
    for texto in texto_postres:
        texto.set("0")
    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    for variable in variables_comidas:
        variable.set(0)
    for variable in variables_bebidas:
        variable.set(0)
    for variable in variables_postres:
        variable.set(0)
    var_costo_comidas.set("")
    var_costo_bebidas.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")

# Iniciar TKinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry("1050x630+158+50")

# Evitar Maximizar Ventana
aplicacion.resizable(0, 0)

# Título de la Ventana
aplicacion.title("Gestor de Restaurantes - Sistema de Facturación")

# Color de Fondo de la Ventana
aplicacion.config(bg="burlywood")

# Panel Superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta de Título
etiqueta_titulo = Label(panel_superior,
                        text="Sistema de Facturación",
                        fg="azure4",
                        font=("Dosis", 58),
                        bg="burlywood",
                        width=28)
etiqueta_titulo.grid(row=0,
                     column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de Costos
panel_costos = Frame(panel_izquierdo,
                     bd=1,
                     relief=FLAT,
                     bg="azure4",
                     padx=60)
panel_costos.pack(side=BOTTOM)

# Panel de Comidas
panel_comidas = LabelFrame(panel_izquierdo,
                           text="Comida",
                           font=("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_comidas.pack(side=LEFT)

# Panel de Bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                           text="Bebidas",
                           font=("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_bebidas.pack(side=LEFT)

# Panel de Postres
panel_postres = LabelFrame(panel_izquierdo,
                           text="Postres",
                           font=("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_postres.pack(side=LEFT)

# Panel Derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel de Calculadora
panel_calculadora = Frame(panel_derecho,
                          bd=1,
                          relief=FLAT,
                          bg="burlywood")
panel_calculadora.pack()

# Panel de Recibo
panel_recibo = Frame(panel_derecho,
                     bd=1,
                     relief=FLAT,
                     bg="burlywood")
panel_recibo.pack()

# Panel de Botones
panel_botones = Frame(panel_derecho,
                      bd=1,
                      relief=FLAT,
                      bg="burlywood")
panel_botones.pack()

# Lista de Productos
lista_comidas = ["Pollo", "Res", "Puerco", "Pescado", "Cabrito", "Pizza", "Tacos", "Torta"]
lista_bebidas = ["Agua", "Refresco", "Leche", "Café", "Cerveza", "Mezcal", "Tequila", "Vino"]
lista_postres = ["Fruta", "Pastel", "Pay", "Galletas", "Helado", "Crepas", "Budín", "Bizcocho"]

# Generar Items de Comida
variables_comidas = []
cuadros_comidas = []
texto_comidas = []
CONTADOR = 0
for comida in lista_comidas:
    # Crear el Checkbutton
    variables_comidas.append("")
    variables_comidas[CONTADOR] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comidas[CONTADOR],
                         command=revisar_check)
    comida.grid(row=CONTADOR,
                column=0,
                sticky=W)

    # Crear los Cuadros de Entrada
    cuadros_comidas.append("")
    texto_comidas.append("")
    texto_comidas[CONTADOR] = StringVar()
    texto_comidas[CONTADOR].set("0")
    cuadros_comidas[CONTADOR] = Entry(panel_comidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comidas[CONTADOR],
                                     justify=RIGHT)
    cuadros_comidas[CONTADOR].grid(row=CONTADOR,
                                  column=1)

    CONTADOR += 1

# Generar Items de Bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
CONTADOR = 0
for bebida in lista_bebidas:
    # Crear el Checkbutton
    variables_bebidas.append("")
    variables_bebidas[CONTADOR] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[CONTADOR],
                         command=revisar_check)
    bebida.grid(row=CONTADOR,
                column=0,
                sticky=W)

    # Crear los Cuadros de Entrada
    cuadros_bebidas.append("")
    texto_bebidas.append("")
    texto_bebidas[CONTADOR] = StringVar()
    texto_bebidas[CONTADOR].set("0")
    cuadros_bebidas[CONTADOR] = Entry(panel_bebidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[CONTADOR],
                                     justify=RIGHT)
    cuadros_bebidas[CONTADOR].grid(row=CONTADOR,
                                  column=1)

    CONTADOR += 1

# Generar Items de Postres
variables_postres = []
cuadros_postres = []
texto_postres = []
CONTADOR = 0
for postre in lista_postres:
    # Crear el Checkbutton
    variables_postres.append("")
    variables_postres[CONTADOR] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[CONTADOR],
                         command=revisar_check)
    postre.grid(row=CONTADOR,
                column=0,
                sticky=W)

    # Crear los Cuadros de Entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[CONTADOR] = StringVar()
    texto_postres[CONTADOR].set("0")
    cuadros_postres[CONTADOR] = Entry(panel_postres,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[CONTADOR],
                                     justify=RIGHT)
    cuadros_postres[CONTADOR].grid(row=CONTADOR,
                                  column=1)

    CONTADOR += 1

# Variables
var_costo_comidas = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Etiquetas de Costos y Campos de Entrada
# Comidas
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_costo_comidas)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Bebidas
etiqueta_costo_bebidas = Label(panel_costos,
                              text="Costo Bebidas",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_bebidas.grid(row=1, column=0)

texto_costo_bebidas = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row=1, column=1, padx=41)

# Postres
etiqueta_costo_postres = Label(panel_costos,
                              text="Costo Postres",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

# Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text="SubTotal",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Impuesto
etiqueta_impuesto = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_impuestos)
texto_impuesto.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ["Total", "Recibo", "Guardar", "Resetear"]
botones_creados = []
COLUMNAS = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=COLUMNAS)
    COLUMNAS += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Área de Recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis", 16, "bold"),
                          width=32,
                          bd=1,
                          justify=RIGHT)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-",
                       "1", "2", "3", "x", "R", "B", "0", "/"]
botones_guardados = []

FILA = 1
COLUMNA =0
for boton in botones_calculadora:
    BOTON_TEXT = boton.title()
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Dosis", 16, "bold"),
                   fg="white",
                   bg="Azure4",
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=FILA, column=COLUMNA)

    if BOTON_TEXT not in ("R", "B"):
        boton.config(command=lambda numero_param = BOTON_TEXT : click_boton(numero_param))
    elif BOTON_TEXT == "R":
        boton.config(command=obtener_resultado)
    elif BOTON_TEXT == "B":
        boton.config(command=borrar)

    if COLUMNA == 3:
        FILA += 1

    COLUMNA += 1

    if COLUMNA == 4:
        COLUMNA = 0

botones_guardados[0].config(command=lambda : click_boton("7"))
botones_guardados[1].config(command=lambda : click_boton("8"))
botones_guardados[2].config(command=lambda : click_boton("9"))
botones_guardados[3].config(command=lambda : click_boton("+"))
botones_guardados[4].config(command=lambda : click_boton("4"))
botones_guardados[5].config(command=lambda : click_boton("5"))
botones_guardados[6].config(command=lambda : click_boton("6"))
botones_guardados[7].config(command=lambda : click_boton("-"))
botones_guardados[8].config(command=lambda : click_boton("1"))
botones_guardados[9].config(command=lambda : click_boton("2"))
botones_guardados[10].config(command=lambda : click_boton("3"))
botones_guardados[11].config(command=lambda : click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton("0"))
botones_guardados[15].config(command=lambda : click_boton("/"))

# Evitar que la pantalla se cierre
aplicacion.mainloop()

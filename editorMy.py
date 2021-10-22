from tkinter import ttk
from tkinter import *
from random import choice
from  tkinter import filedialog as FileDialog
from io import open
 


boton = ""
operacion=""
resultado=0
#--------------RECONFIGURACION DE LA VENTANA--------------------
ventana = Tk()
ventana.title("<#/ TROYA \#>")
ventana.geometry("1370x700")
#ventana.iconbitmap("form.ico") cambiar de icono
          
def colorven():
     color=["#4B5F4E","black","#315E38"]
     coven=choice(color)
     ventana.config(bg=coven)

barramenu=Menu(ventana)
ventana.config(menu=barramenu,width=1300,height=800,bg="#121311")#23060B
#1a181bfrom tkinter import *
#imagen=PhotoImage(file="para1.jpg")
#fondo=Label(ventana,image=imagen).place(x=100,y=400)
decoracion1=Label(text="*",fg="yellow",bg="#1a181b",font="Ebrima 20")
decoracion1.place(x=5,y=2)
decoracion2=Label(text="*",fg="blue",bg="#1a181b",font="Ebrima 20")
decoracion2.place(x=18,y=2)
decoracion3=Label(text="*",fg="red",bg="#1a181b",font="Ebrima 20")
decoracion3.place(x=34,y=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#___________________________________-block-_____________________________
horscroll=Scrollbar(ventana,orient=HORIZONTAL)
horscroll.place(x=5,y=657,relwidth=0.65, relheight=0.03)

T = Text(ventana,fg="black",height=37,width=125,font="Modem 10")
T.configure(xscrollcommand=horscroll.set, wrap="none")
horscroll.config(command=T.xview)

verscroll=Scrollbar(ventana, orient=VERTICAL)
verscroll.place(x=895,y=45,relwidth=0.015, relheight=0.93)
verscroll.config(command=T.yview)
T.place(x=5,y=45)
 
# FUNCIONES DE MENU DESPLEGABLE
def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    T.delete(1.0, "end")
    ventana.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),("archivo de python","*.py")),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        T.delete(1.0,'end')
        T.insert('insert', contenido)
        fichero.close()
        ventana.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = T.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
        mode="w", defaultextension=".py")

    if fichero is not None:
        ruta = fichero.name
        contenido = T.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


#----------------barras de menu---------------------------------------
archivomenu=Menu(ventana,barramenu,tearoff=0)
archivomenu.config(fg="#03f943",bg="#191a19")
archivomenu.add_command(label="Nuevo",command=nuevo)
archivomenu.add_command(label="Guardar",command=guardar)
archivomenu.add_command(label="Abrir archivo",command=abrir)
archivomenu.add_command(label="")
archivomenu.add_command(label="Guardar como...",command=guardar_como)
archivomenu.add_command(label="Salir")

#-----------------CAJA DE TEXTO-----------------
entry=ttk.Entry(ventana)
entry.place(x=135,y=9,width=500,height=20)
botonBusca = Button(ventana,font="impact 11",text="#/c\#",fg="white",bg="black",command=colorven).place(x=635,y=5)
borrartodo = Button(ventana,font="impact 9",text="BORRAR TODO",fg="white",bg="black").place(x=765,y=5)
nuevo=Button(ventana,font="impact 9",text="Nuevo.T",fg="white",bg="black").place(x=845,y=5)
#------------------MENU-----------------
archivoedicion=Menu(ventana,barramenu,tearoff=0)
archivoedicion.config(fg="#03f943",bg="#191a19")
archivoedicion.add_command(label="Tipo de letra")
archivoedicion.add_command(label="Color de letra")
archivoedicion.add_command(label="Tamaño de letra")
#191a19
archivoherramienta=Menu(ventana,barramenu,tearoff=0)
archivoherramienta.config(fg="#03f943",bg="#191a19")
archivoherramienta.add_command(label="Calculadora")
archivoherramienta.add_command(label="Editor")
#191a19
archivoayuda=Menu(ventana,barramenu,tearoff=0)
archivoayuda.config(fg="#03f943",bg="#191a19")
archivoayuda.add_command(label="Acerca del programa")
archivoayuda.add_command(label="Funciones del programa")
archivoayuda.add_command(label="")
archivoayuda.add_command(label="Tutoriales")

barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Editor", menu=archivoedicion)
barramenu.add_cascade(label="Configuracion",menu=archivoherramienta)
barramenu.add_cascade(label="Ayuda",menu=archivoayuda)

filemenu = Menu(archivomenu, tearoff=0)
barramenu.add_cascade(menu=filemenu, label="Archivo")

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(ventana, textvar=mensaje, justify='left')
monitor.place(x=5,y=635)

ventana.config(menu=archivomenu)

#-----------------fondo del los botones Y BUSCADOR-----------------------------
framx=Frame(bg="#2b2d2a",width=353,height=285).place(x=1000,y=375)

                                   # FUNCION DE LOS BOTONES EN LA CALCULADORA

                                   # SIMBOLOS DE OPERACIONES ARITMETICAS
boton = ""

def digito(num):
     global boton
     boton = boton + str(num)
     calculo.set(boton)

def igual():
     try:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        boton = ""
     except:
        calculo.set(" error ")
#ventana.configure(background="light blue")
calculo = StringVar()
datos = Entry(ventana, textvariable=calculo,bg="#1b1918",fg="red",font="Tahoma 13")
datos.place(x=1020,y=380,width=320,height=38)

boton1 = ttk.Button(ventana, text=' 1 ',command=lambda: digito(1))
boton1.place(x=1063,y=562,width=40,height=40)
boton2 = ttk.Button(ventana, text=' 2 ',command=lambda: digito(2))
boton2.place(x=1106,y=562,width=40,height=40)
boton3 = ttk.Button(ventana, text=' 3 ',command=lambda: digito(3))
boton3.place(x=1149,y=562,width=40,height=40)

boton4 = ttk.Button(ventana, text=' 4 ',command=lambda: digito(4))
boton4.place(x=1063,y=512,width=40,height=40)
boton5 = ttk.Button(ventana, text=' 5 ',command=lambda: digito(5))
boton5.place(x=1106,y=512,width=40,height=40)
boton6 = ttk.Button(ventana, text=' 6 ',command=lambda: digito(6))
boton6.place(x=1149,y=512,width=40,height=40)

boton7 = ttk.Button(ventana, text=' 7 ',command=lambda: digito(7))
boton7.place(x=1063,y=462,width=40,height=40)
boton8 = ttk.Button(ventana, text=' 8 ',command=lambda: digito(8))
boton8.place(x=1106,y=462,width=40,height=40)
boton9 = ttk.Button(ventana, text=' 9 ',command=lambda: digito(9))
boton9.place(x=1149,y=462,width=40,height=40)

boton0 = ttk.Button(ventana, text=' 0 ',command=lambda: digito(0))
boton0.place(x=1063,y=612,width=40,height=40)

suma = ttk.Button(ventana, text=' + ',command=lambda: digito("+"))
suma.place(x=1020,y=462,width=40,height=40)

resta = ttk.Button(ventana, text=' - ',command=lambda: digito("-"))
resta.place(x=1020,y=512,width=40,height=40)

multiplica = ttk.Button(ventana, text=' * ',command=lambda: digito("*"))
multiplica.place(x=1020,y=562,width=40,height=40)

divide = ttk.Button(ventana, text=' / ',command=lambda: digito("/"))
divide.place(x=1020,y=612,width=40,height=40)

resultado = ttk.Button(ventana, text=' = ',command=igual)
resultado.place(x=1106,y=612,width=85,height=40)

# FUNCIONES

class numeros():
     ttk.Style().configure("TButton", padding=8, relief="flat",
                           background="black",font="impact 14")
#---------MODO CALCULADORA-------------
frambot=Frame(framx,bg="red",width=146,height=210).place(x=1195,y=440)
# ------------BORRAR------------
def limpiar():
     calculo.set("")
borrarC=ttk.Button(framx,text="BORRAR",command=limpiar).place(x=1063,y=418,width=87,height=35)
#-----------------------------------------------------------------CHATBOT--------------------------------------------------------------------------------------------
framchat=Frame(ventana,bg="#2b2d2a",width=353,height=320).place(x=1000,y=40)#353
def chatB():
     usr = usuario.get()
     if usr == "hola":
          mensaje="hola"
     elif usr=="como estas":
          mensaje="bien y tu"
     elif usr== "como te llamas":
          mensaje="asistente de app"
     elif usr== "quien te creo":
          mensaje="CRISTIAN JAVIER PERDOMO ALDANA"
     elif usr== "buenos dias":
          mensaje="buenos dias como estas"
     elif usr== "buenas tardes":
          mensaje="buenas tardes como estas"
     elif usr== "buenas noches":
          mensaje="buenas noches como estas"
     elif usr== "que tal":
          mensaje="bien"
     elif usr== "que hay de nuevo":
          mensaje="estoy con un exelente animo"
     else:
          mensaje="lo siento no entiendo que es",usr
     respuesta.config(text=mensaje,bg="#292727",fg="white",width=40,height=2,font="Tahoma 11")
     respuesta.place(x=1020,y=195)
usuario=StringVar()
chat = Entry(framchat,textvariable=usuario,bg="#1b1918",fg="green",font="Tahoma 13").place(x=1020,y=245,width=320,height=38)
respuesta=Label(framchat)

def limchat():
     usuario.set("")
borrar_chat=ttk.Button(text="BorrarChat",command=limchat).place(x=1228,y=285,width=115,height=45)
boton_bot=ttk.Button(framx,text="ChatBot",command=chatB).place(x=1020,y=285,width=87,height=45)#,command=lambda:numeropulsado("ChatBot")
#---------------------------------------------------------------FINAL DEL PROGRAMA-------------------------------------------------------------------------------
ventana.mainloop()
#___________________________________________________________________________________________________________________________________________________







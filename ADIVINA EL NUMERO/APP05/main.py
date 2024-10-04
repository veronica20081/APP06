import flet as ft
import random 

#Funcion principal
def main(page: ft.Page):
    #Variables globales
    global numero_Secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title = "Adivina el numero"
    
    #Generar un numero aleatoreo
    numero_Secreto = random.randint(1,100)

    #Crear los elementos de la interfas 
    titulo=ft.Text("Adivina el numero secreto entre 1 y 100",size= 20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resuldado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )   
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.with,
        height=page.window.height,
        padding=20
        
        
    )
    

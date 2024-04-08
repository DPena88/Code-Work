#Diego Peña
#counter

import flet as ft

#Requirements:
#2 labels, 1 for title, 1 for the number.
#2 buttons, 1 for adding, 1 for subtracting

def main(page:ft.Page):
    def add1(e):
        numero = int(numberlabel.value)
        numero += 1
        numberlabel.value = str(numero)
        page.update()

    def minus1(e):
        numero = int(numberlabel.value)
        numero -= 1
        if numero < 0:
            numero = 0
        numberlabel.value = str(numero)
        page.update()

    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    titleText = ft.Text(value="Counter App", size = 50)
    numberlabel = ft.Text(value="0", size = 50)
    plusButton = ft.ElevatedButton(text="+", on_click=add1)
    minusButton = ft.ElevatedButton(text="-", on_click=minus1)
    fotoperro = ft.Image(src="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRobGg3aKquGcVbd5im6zzt3gl4ft40HfOYQF69jT9fKeoGf3PvDMgjYkSRqgqtg1d43zglnzlxHNc3OzQ", height = 300, width = 600)
    rowperro = ft.Row(controls=[fotoperro], alignment = ft.MainAxisAlignment.CENTER)
    rowbuttons = ft.Row(controls=[minusButton, plusButton], alignment=ft.MainAxisAlignment.CENTER)
    page.add(titleText, numberlabel, rowbuttons, rowperro)
    

ft.app(target=main)

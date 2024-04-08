#GUI
#Text Editor with Word Counter

#Diego Peña

import flet as ft
import os

def main(page:ft.Page):
    def createf(e):
        pass

    def openf (e):
        pass
        
    def savef(e):
        pass

    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    titleText = ft.Text(value="Word Count", size = 50)
    createB = ft.ElevatedButton(text = "Create", on_click=createf)
    openB = ft.ElevatedButton(text = "Open", on_click=openf)
    saveB = ft.ElevatedButton(text = "Save", on_click=savef)

    def textbox_changed(e):
        words = len(tb.value.split())
        wLabel.value = "Enter text: " + str(words)
        page.update()
    
    wLabel = ft.Text(value = "Words: 0")
    t = ft.Text()
    tb = ft.TextField(
        label="Word Counter",
        on_change=textbox_changed,
    )
    rowbuttons = ft.Row(controls=[createB, openB, saveB], alignment=ft.MainAxisAlignment.CENTER)
    page.add(titleText, tb, wLabel, rowbuttons)

ft.app(target=main)

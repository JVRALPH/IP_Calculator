import flet as ft
import UIElements as UIE
import IPManager as IPM
from flet import *
from math import pi

def main(page: Page):

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                route='/',
                padding=0,
                controls=[
                    UIE.UIElements.form_body,
                ]
            )
        )
        if page.route =='/Tabla':
            page.views.append(
            View(
                route='/',
                padding=0,
                scroll='ADAPTIVE',
                controls=[
                    AppBar(title=Text('Regresar'),bgcolor='black',toolbar_height=40),
                    UIE.UIElements.table_body,
                ]
            )
        )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    
    UIE.UIElements.page_settings(page)
    page.add(UIE.UIElements.form_body)
    #UIE.UIElements.ip_txtField.on_blur = lambda e: IPM.IPManager.validate_ip(e, page)
    #UIE.UIElements.sub_dropdown.on_blur = lambda e: IPM.IPManager.validate_ip(e, page)
    UIE.UIElements.btn_calcular.on_click = lambda e: IPM.IPManager.btn_calcular_click(e,page)
    

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

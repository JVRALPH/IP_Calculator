import flet as ft
from flet import *
from math import pi
import IPManager as IPM

#Clase que maneja los elementos en las vistas
class UIElements:

    #Configuracion general de pagina
    def page_settings(page):
        page.window_prevent_close = True
        page.window_width=1000
        page.window_height=800
        page.window_min_width=600
        page.window_min_height=800
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding=0
        page.window_resizable = True
        page.window_center()
        page.window_to_front()

    #Estilo de los campos de entrada
    ip_txtField =TextField(
        tooltip="Ingrese una IP valida ej. 192.158.1.38",
        width=280,
        height=70,
        hint_text='IP',
        border_color=ft.colors.WHITE,
        border='underline',
        color='white',
        prefix_icon=icons.COMPUTER_OUTLINED,
        border_radius=11,
    )

    #Configuracion de menu desplegable para el prefijo 
    sub_dropdown=Dropdown(
        prefix_icon=icons.ONETWOTHREE_OUTLINED,
        tooltip="Seleccione prefijo de la red",
        label="Prefijo '/'",
        width=280,
        height=90,
        border='underline',
        options=[
            ft.dropdown.Option(str(i)) for i in range(1, 33)
        ],
    )
    
    #Estilos de textos
    ip_text=Text(
        "IP: ",
        width=800,
        size=20,
        weight='w900',
        text_align='center',
    )
    ip_pri_valida=Text(
        
        width=800,
        size=20,
        weight='w900',
        text_align='center',
    )
    ip_ult_valida=Text(
        width=800,
        size=20,
        weight='w900',
        text_align='center',
    )

    #Estilo de tabla
    table_info = DataTable( 
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
    )
    
    #Estilos de botones
    btn_clear_txtf = IconButton(
        icon=icons.RESTORE_FROM_TRASH_OUTLINED,
        icon_color='white',
        icon_size=30,
        tooltip="Limpiar campos",
    ) 
    btn_calcular=ElevatedButton(
        content=Text(
            "Calcular",
            color='white',
            weight='w400',
        ),width=220,bgcolor='black'
    )
    btn_confirm=ElevatedButton(
        text="Si, quiero salir",
    )
    btn_deny=ElevatedButton(
        text="No",
    )

    #Estilo de dialogo de confirmacion para salir
    confirm_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Confirmacion"),
        content=ft.Text("¿Realmente quieres salir de esta aplicación?"),
        actions=[
            btn_confirm,
            btn_deny,
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    #Estilo page principal
    form_body = Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*pi), #degree
                    width=360,
                    height=560,
                    bgcolor="#22ffffff",
                ),
                Container(
                    Container(
                        Column([
                            Container(
                                Icon(
                                    ft.icons.CALCULATE_OUTLINED,
                                    size=80,
                                ),padding=padding.only(130,20),
                            ),
                            Text(
                                "CALCULADORA IP",
                                width=340,
                                size=20,
                                weight='w900',
                                text_align='center',
                            ),
                            Divider(height=25, color="transparent"),
                            Text(
                                "Porfavor ingresa la direccion IP",
                                width=340,
                                weight='w600',
                                text_align='center',
                                size=10,
                            ),
                            Container(
                                ip_txtField,
                                padding=padding.only(25,10),
                            ),
                            Container(
                                sub_dropdown,
                                padding=padding.only(25,0),
                            ),
                            Container(
                                Row(
                                    [
                                        btn_clear_txtf,
                                        btn_calcular,
                                    ]
                                ),padding=padding.only(30,50),
                            ),
                        ])
                    ),
                    width=360,
                    height=580,
                    bgcolor="#22ffffff",
                    border_radius=11,
                )
            ]),
            padding=80,
            alignment=ft.alignment.top_center,
            width=360,
            height=900,
        ),
        width=1920,
        height=1080,
        gradient=LinearGradient(
            colors=["#0A3431","#2A6858","#6CE5BB"],
            #rotation=(pi*1.5),
            rotation=(pi*0.5),
        ),
    )
    
    #Estilo de la pagina con tabla de informacion
    table_body = Container(
        Container(
            Stack([
                    Container(
                        Column([
                            Container(
                                Icon(
                                    ft.icons.CALCULATE_OUTLINED,
                                    size=80,
                                ),padding=padding.only(360,20),
                            ),
                                Text(
                                    "CALCULADORA IP",
                                    width=800,
                                    size=20,
                                    weight='w900',
                                    text_align='center',
                                ),
                                ip_text,
                            Divider(height=25, color="transparent"),
                            table_info,
                            Divider(height=25, color="transparent"),
                            ip_pri_valida,
                            ip_ult_valida,
                        ])
                        ,padding=padding.only(0,20),
                    ),
            ]),
            padding=40,
            alignment=ft.alignment.top_center,
            width=1920,
            height=1080,
        ),
        width=1920,
        height=1080,
        gradient=LinearGradient(["#0A3431","#2A6858","#6CE5BB"]),
    )

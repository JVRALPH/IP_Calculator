import flet as ft
from flet import *
from math import pi

class UIElements:

    def page_settings(page):
        page.window_width=1000
        page.window_height=800
        page.window_title_bar_hidden=True
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding=0
        page.window_resizable = False
        page.window_center()

    btn_calcular=ElevatedButton(
        content=Text(
            "Calcular",
            color='white',
            weight='w500',
        ),width=280,bgcolor='black'
    )
    ip_txtField =TextField(
        width=280,
        height=70,
        hint_text='IP',
        border_color=ft.colors.WHITE,
        border='underline',
        color='white',
        prefix_icon=icons.COMPUTER_OUTLINED,
        border_radius=11,
    )

    sub_dropdown=Dropdown(
        prefix_icon=icons.ONETWOTHREE_OUTLINED,
        label="Prefijo '/'",
        width=280,
        height=90,
        border='underline',
        options=[
            ft.dropdown.Option(str(i)) for i in range(1, 33)
        ],
    )
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

    table_info = DataTable(
        column_spacing=50,
    )

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
                                btn_calcular,
                                padding=padding.only(30,50),
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
        gradient=LinearGradient(["#000000","#212825","#435049","#65786E","#869F93"]),
    )
    
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
        gradient=LinearGradient(["#000000","#212825","#435049","#65786E","#869F93"]),
    )

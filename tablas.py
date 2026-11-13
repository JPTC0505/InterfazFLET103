import flet as ft
from flet.controls import border_radius

from estilos import *

def crear_tabla(datos):
    return ft.DataTable(
        columns = [
            ft.DataColumn(
                label = ft.Text("MAQUINA")
            ),
            ft.DataColumn(
                label=ft.Text("TEMPERATURA")
            ),
            ft.DataColumn(
                label=ft.Text("PRODUCCION")
            ),
            ft.DataColumn(
                label=ft.Text("ESTADO")
            ),
        ],

        rows = [
            ft.DataRow(
                cells = [
                    ft.DataCell(
                        ft.Text(dato[0])
                    ),
                    ft.DataCell(
                        ft.Text(dato[1])
                    ),
                    ft.DataCell(
                        ft.Text(dato[2])
                    ),
                    ft.DataCell(
                        ft.Text(dato[3])
                    )
                ]
            )
            for dato in datos
        ]
    )

def crear_panel_tabla(datos):
    tabla = crear_tabla(datos)
    return  ft.Container(
        bgcolor = PANEL,
        padding = 20,
        border_radius = 16,
        content = ft.Column(
            controls = [
                ft.Text("Ultimos registros",
                        size = 18,
                        weight = ft.FontWeight.BOLD),
                ft.Row(

                    scroll = ft.ScrollMode.AUTO,
                    controls = [
                        tabla
                    ]
                )
            ]
        )
    )
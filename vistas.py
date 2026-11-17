import flet as ft
from flet.controls import border_radius
from flet_charts import bar_chart_group

from estilos import *

from tablas import crear_tabla

def crear_vista_sensores():
    sensores = ft.Column(
        expand = True,
        spacing = 20,
        controls = [ ft.Text("Sensores",
                             size = 30,
                             weight = ft.FontWeight.BOLD),
                     ft.Text("Estado individual de las variables",color = TEXTO_SEC)
                     ]
    )

    sensores.controls.append(
        ft.Container(
            bgcolor = PANEL,
            padding = 25,
            border_radius = 16,
            content = ft.Column(
                spacing = 15,
                controls = [
                    ft.Row(
                        controls = [
                            ft.Icon(ft.Icons.THERMOSTAT, color = ROJO),
                            ft.Text("Temperatura", size = 18, weight = ft.FontWeight.BOLD),
                        ]
                    ),
                    ft.ProgressBar(value = 0.64, color = ROJO, bgcolor = PANEL_2),
                    ft.Text("64% del rango", color= TEXTO_SEC)
                ]

        )
    )
    )
    return sensores

def crear_vista_registros(datos):
    tabla = crear_tabla(datos)
    return ft.Column(
        expand = True,
        spacing = 20,
        scroll = ft.ScrollMode.AUTO,
        controls = [
            ft.Text("Registros", size = 30, weight = ft.FontWeight.BOLD),
            ft.Text("Historial de mediciones", color = TEXTO_SEC),
            ft.Container(
                bgcolor = PANEL,
                padding = 20,
                border_radius = 16,
                content = ft.Row(
                    scroll = ft.ScrollMode.AUTO,
                    controls = [tabla]
                )
            )
        ]
    )

def crear_vista_configuracion():
    return ft.Column(
        expand = True,
        spacing = 20,
        controls = [
            ft.Text("Configuraciones", size = 30, weight = ft.FontWeight.BOLD),
            ft.TextField(label= "Nombre de la planta", value = "Planta industrial UTP"),
            ft.Switch(label = "Activar alarmas", value = True)
        ]
    )
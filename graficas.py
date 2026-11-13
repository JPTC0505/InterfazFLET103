import flet as ft
import flet_charts as fch
from estilos import *

def crear_grafica():
    temperaturas = [32, 62, 12, 56, 78, 65, 45, 15, 6, 10]
    puntos_temperatura = [fch.LineChartDataPoint(i, temperatura) for i, temperatura in enumerate(temperaturas)]

    serie_temperatura = fch.LineChartData(
        color=AZUL,
        stroke_width=4,
        curved=False,
        point=True,
        points=puntos_temperatura
    )

    grafica_temperatura = fch.LineChart(
        expand=True,
        min_x=0,
        max_x=10,
        min_y=0,
        max_y=100,
        interactive=True,
        data_series=[serie_temperatura],
        left_axis=fch.ChartAxis(
            title=ft.Text("Temperatura (C)", color=TEXTO_SEC),
            title_size=30,
            label_size=40,
            label_spacing=10
        ),
        bottom_axis=fch.ChartAxis(
            title=ft.Text("Medicion", color=TEXTO_SEC),
            title_size=30,
            label_size=40,
            label_spacing=1
        ),
        horizontal_grid_lines=fch.ChartGridLines(
            interval=10,
            color=PANEL_2,
            width=1,
        ),

        vertical_grid_lines=fch.ChartGridLines(
            interval=1,
            color=PANEL_2,
            width=1),

        border=ft.Border.all(1, PANEL_2)

    )

    panel_grafica = ft.Container(
        expand=2,
        height=360,
        bgcolor=PANEL,
        padding=20,
        border_radius=16,
        content=ft.Column(
            controls=[
                ft.Text("Tendencia de temperatura",
                        size=18,
                        weight=ft.FontWeight.BOLD, ),
                ft.Text("Ultimas 10 mediciones", color=TEXTO_SEC),
                ft.Container(
                    expand=True,
                    content=grafica_temperatura
                )
            ]
        )
    )
    grafica_estados = fch.PieChart(
        expand=True,
        center_space_radius=45,
        sections_space=3,
        sections=[
            fch.PieChartSection(
                value=65,
                title="65%",
                color=VERDE,
                radius=60
            ),
            fch.PieChartSection(
                value=25,
                title="25%",
                color=AMARILLO,
                radius=60
            ),
            fch.PieChartSection(
                value=10,
                title="10%",
                color=ROJO,
                radius=60
            ),
        ]
    )

    panel_estados = ft.Container(
        expand=1,
        height=360,
        bgcolor=PANEL,
        padding=20,
        border_radius=16,
        content=ft.Column(
            controls=[
                ft.Text("Estado maquinas", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Distribucion actual", color=TEXTO_SEC),
                ft.Container(
                    expand=True,
                    content=grafica_estados
                )
            ]
        )
    )

    fila_graficas = ft.Row(
        spacing=20,
        controls=[
            panel_grafica, panel_estados
        ]
    )

    return fila_graficas, temperaturas,  serie_temperatura

def actualizar_grafica_temperatura(temperaturas, serie_temperatura, nueva_temperatura):
    temperaturas.pop(0)
    temperaturas.append(nueva_temperatura)
    serie_temperatura.points = [
        fch.LineChartDataPoint(
            i,temperatura
        ) for i,temperatura in enumerate(temperaturas)
    ]

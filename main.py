import flet as ft
import flet_charts as fch
from estilos import *
from graficas import crear_grafica
from tablas import crear_panel_tabla


def main(page:ft.Page):

    page.window.width = 1200
    page.window.height = 720
    page.bgcolor = FONDO
    page.window.min_height= 600
    page.window.min_width = 900
    page.title = "Industrial control"
    page.theme_mode = ft.ThemeMode.DARK

    barra_lateral = ft.Container(
        width=230,
        bgcolor = PANEL,
        padding = 20,
        border_radius =15)

    area_principal = ft.Container(
        expand = True,
        padding = 30,
    )

    estructura = ft.Row(
        expand = True,
        spacing = 0,
        controls = [barra_lateral, area_principal]
    )
    page.add(estructura)

    dashboard = ft.Column(
        expand = True,
        spacing = 20,
        scroll = ft.ScrollMode.AUTO
    )

    area_principal.content = dashboard

    titulo = ft.Text("Dashboard",
                     size = 30,
                     weight = ft.FontWeight.BOLD,
                     color = TEXTO)
    subtitulo = ft.Text("Supervision genera del proceso industrial",
                        size = 13,
                        color = TEXTO_SEC)

    encabezado = ft.Column(spacing = 3,
                           controls = [titulo, subtitulo])

    dashboard.controls.append(encabezado)

    def crear_kpi(titulo, valor, icono, color):
        return ft.Container(
            expand=1,
            bgcolor=PANEL,
            padding=20,
            border_radius=16,
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [ft.Column(
                    spacing = 5,
                    controls = [ft.Text(titulo,color = TEXTO_SEC), valor]
                ),
                ft.Icon(icono, color = color, size = 32)]
            )
        )

    valor_humedad = ft.Text("56%", size = 26, weight = ft.FontWeight.BOLD, color = TEXTO)
    valor_produccion = ft.Text("1258", size = 26, weight = ft.FontWeight.BOLD, color = TEXTO)
    valor_eficiencia = ft.Text("92%", size = 26, weight = ft.FontWeight.BOLD, color = TEXTO)
    valor_temperatura = ft.Text("24.5 °C", size = 26, weight = ft.FontWeight.BOLD, color = TEXTO)

    tarjetas = ft.Row(
        spacing = 15,
        controls = [crear_kpi("TEMPERATURA", valor_temperatura,ft.Icons.THERMOSTAT, ROJO),
                    crear_kpi("HUMEDAD", valor_humedad, ft.Icons.WATER_DROP, AZUL),
                    crear_kpi("PRODUCCION", valor_produccion, ft.Icons.FACTORY, MORADO),
                    crear_kpi("EFICIENCIA", valor_eficiencia, ft.Icons.TRENDING_UP, VERDE)]
    )

    dashboard.controls.append(tarjetas)

    ######################### GRAFICAS ##############################

    filas, temperaturas, serie = crear_grafica()
    dashboard.controls.append(filas)

    datos_registros = [
        ["M01", "58.4 C", "116", "NORMAL"],
        ["M02", "67.5 C", "110", "ADVERTENCIA"],
        ["M03","54.8 C", "124", "NORMAL"]
    ]

    panel_tabla = crear_panel_tabla(datos_registros)
    dashboard.controls.append(panel_tabla)




ft.run(main)
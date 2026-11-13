from encodings.punycode import punycode_encode

import flet as ft
import flet_charts as fch
from flet.controls import border_radius


def main(page:ft.Page):
    FONDO = "#0F172A"
    PANEL = "#1E293B"
    PANEL_2 = "#334155"
    TEXTO = "#F8FAFC"
    TEXTO_SEC = "#94A3B8"
    AZUL = "#38BDF8"
    VERDE = "#22C55E"
    AMARILLO = "#F59E0B"
    ROJO = "#EF4444"
    MORADO = "#A855F7"

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

    temperaturas = [32,62,12,56,78,65,45,15,6,10]
    puntos_temperatura = [fch.LineChartDataPoint(i, temperatura) for i, temperatura in enumerate(temperaturas)]

    serie_temperatura = fch.LineChartData(
        color = AZUL,
        stroke_width = 4,
        curved = False,
        point = True,
        points = puntos_temperatura
   )

    grafica_temperatura = fch.LineChart(
        expand = True,
        min_x = 0,
        max_x = 10,
        min_y = 0,
        max_y = 100,
        interactive = True,
        data_series = [serie_temperatura],
        left_axis = fch.ChartAxis(
            title = ft.Text("Temperatura (C)", color = TEXTO_SEC),
            title_size = 30,
            label_size = 40,
            label_spacing = 10
        ),
        bottom_axis =fch.ChartAxis(
            title = ft.Text("Medicion", color = TEXTO_SEC),
            title_size = 30,
            label_size = 40,
            label_spacing = 1
        ),
        horizontal_grid_lines = fch.ChartGridLines(
            interval = 10,
            color = PANEL_2,
            width = 1,
        ),

        vertical_grid_lines = fch.ChartGridLines(
            interval=1,
            color=PANEL_2,
            width=1),

        border = ft.Border.all(1, PANEL_2)

    )

    panel_grafica = ft.Container(
        expand = 2,
        height = 360,
        bgcolor = PANEL,
        padding = 20,
        border_radius = 16,
        content = ft.Column(
            controls = [
                ft.Text("Tendencia de temperatura",
                        size = 18,
                        weight = ft.FontWeight.BOLD,),
                ft.Text("Ultimas 10 mediciones", color = TEXTO_SEC),
                ft.Container(
                    expand = True,
                    content = grafica_temperatura
                )
            ]
        )
    )
    grafica_estados = fch.PieChart(
        expand = True,
        center_space_radius = 45,
        sections_space = 3,
        sections = [
            fch.PieChartSection(
                value = 65,
                title = "65%",
                color = VERDE,
                radius = 60
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




ft.run(main)
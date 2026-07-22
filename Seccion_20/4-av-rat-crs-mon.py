import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("data/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()

chart_def = """{
    "chart": {
        "type": "area"
    },
    "accessibility": {
        "description": "Image description: An area chart compares the nuclear stockpiles of the USA and the USSR/Russia between 1945 and 2024. The number of nuclear weapons is plotted on the Y-axis and the years on the X-axis. The chart is interactive, and the year-on-year stockpile levels can be traced for each country. The US has a stockpile of 2 nuclear weapons at the dawn of the nuclear age in 1945. This number has gradually increased to 170 by 1949 when the USSR enters the arms race with one weapon. At this point, the US starts to rapidly build its stockpile culminating in 31,255 warheads by 1966 compared to the USSR's 8,400. From this peak in 1967, the US stockpile gradually decreases as the USSR's stockpile expands. By 1978 the USSR has closed the nuclear gap at 25,393. The USSR stockpile continues to grow until it reaches a peak of 40,159 in 1986 compared to the US arsenal of 24,401. From 1986, the nuclear stockpiles of both countries start to fall. By 2000, the numbers have fallen to 10,577 and 12,188 for the US and Russia, respectively. The decreases continue slowly after plateauing in the 2010s, and in 2024 the US has 3,708 weapons compared to Russia's 4,380."
    },
    "title": {
        "text": "US and USSR nuclear stockpiles"
    },
    "subtitle": {
        "text": "Source: <a href='https://fas.org/issues/nuclear-weapons/status-world-nuclear-forces/' target='_blank'>FAS</a>"
    },
    "xAxis": {
        "allowDecimals": false,
        "accessibility": {
            "rangeDescription": "Range: 1940 to 2024."
        }
    },
    "yAxis": {
        "title": {
            "text": "Nuclear weapon states"
        }
    },
    "tooltip": {
        "pointFormat": "{series.name} had stockpiled <b>{point.y:,.0f}</b><br/>warheads in {point.x}"
    },
    "plotOptions": {
        "area": {
            "pointStart": 1940,
            "marker": {
                "enabled": false,
                "symbol": "circle",
                "radius": 2,
                "states": {
                    "hover": {
                        "enabled": true
                    }
                }
            }
        }
    },
    "series": [{
        "name": "USA",
        "data": [
            null, null, null, null, null, 2, 9, 13, 50, 170, 299, 438, 841,
            1169, 1703, 2422, 3692, 5543, 7345, 12298, 18638, 22229, 25540,
            28133, 29463, 31139, 31175, 31255, 29561, 27552, 26008, 25830,
            26516, 27835, 28537, 27519, 25914, 25542, 24418, 24138, 24104,
            23208, 22886, 23305, 23459, 23368, 23317, 23575, 23205, 22217,
            21392, 19008, 13708, 11511, 10979, 10904, 11011, 10903, 10732,
            10685, 10577, 10526, 10457, 10027, 8570, 8360, 7853, 5709, 5273,
            5113, 5066, 4897, 4881, 4804, 4717, 4571, 4018, 3822, 3785, 3805,
            3750, 3708, 3708, 3708, 3708
        ]
    }, {
        "name": "USSR/Russia",
        "data": [
            null, null, null, null, null, null, null, null, null,
            1, 5, 25, 50, 120, 150, 200, 426, 660, 863, 1048, 1627, 2492,
            3346, 4259, 5242, 6144, 7091, 8400, 9490, 10671, 11736, 13279,
            14600, 15878, 17286, 19235, 22165, 24281, 26169, 28258, 30665,
            32146, 33486, 35130, 36825, 38582, 40159, 38107, 36538, 35078,
            32980, 29154, 26734, 24403, 21339, 18179, 15942, 15442, 14368,
            13188, 12188, 11152, 10114, 9076, 8038, 7000, 6643, 6286, 5929,
            5527, 5215, 4858, 4750, 4650, 4600, 4500, 4490, 4300, 4350, 4330,
            4310, 4495, 4477, 4489, 4380
        ]
    }]
}"""

def app():
    wp = jp.QuasarPage()  # Crea una nueva página web utilizando justpy con el tema Quasar
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")  # agrega un encabezado de nivel 1 (h1) y aplica clases CSS para el estilo
    p1 = jp.QDiv(a=wp, text = "These graphs represent course review analysis", classes="text-subtitle1 text-center q-pa-md")  # agrega un párrafo con texto descriptivo y aplica clases CSS para el estilo

    # ======== Insertar los datos en la definición del gráfico ==========
    hc = jp.HighCharts(a=wp, options=chart_def)  # Crea un gráfico de HighCharts y lo agrega a la página web
    hc.options.series = []  # Limpia las series de datos predeterminadas en la definición del gráfico
    for crs in month_average_crs.columns:  # Itera sobre cada curso en los datos de calificaciones promedio mensuales
        hc.options.series.append({  # Agrega una nueva serie de datos al gráfico para cada curso
            'name': crs,  # Establece el nombre de la serie como el nombre del curso
            'data': list(month_average_crs[crs])  # Establece los datos de la serie utilizando las calificaciones promedio mensuales del curso
        })

    # ========== Ajustar otras opciones del gráfico =========
    hc.options.xAxis.categories = list(month_average_crs.index)  # Establece las categorías del eje X del gráfico utilizando los índices de mes
    hc.options.yAxis.title.text = "Average Rating"  # Establece el título del eje Y del gráfico
    hc.options.title.text = "Average Course Ratings by Month"  # Establece el título del gráfico
    hc.options.title.align = 'center'  # Centra el título
    hc.options.title.style = {  # Estilo del título
        'fontSize': '18px',
        'fontWeight': 'bold',
        'color': '#333'
    }
    hc.options.subtitle.text = "Based on course reviews"  # Establece el subtítulo del gráfico
    hc.options.subtitle.align = 'center'  # Centra el subtítulo
    hc.options.subtitle.style = {  # Estilo del subtítulo
        'fontSize': '14px',
        'color': '#666'
    }
    hc.options.chart.type = "line"  # Cambia el tipo de gráfico a línea

    # Ajustar la posicion de los tipos de lineas que representan cada curso
    hc.options.chart.zoomType = 'x'  # Habilita el zoom en el eje X del gráfico

    # Configuraciones adicionales para mejorar la apariencia y funcionalidad del gráfico
    hc.options.plotOptions = {  # Configura las opciones de trazado para el gráfico
        'line': {
            'marker': {
                'enabled': False
            }
        }
    }

    # Configuraciones adicionales para mejorar la apariencia y funcionalidad del gráfico
    hc.options.tooltip = {  # Configura las opciones de información sobre herramientas para el gráfico
        'headerFormat': '<b>{series.name}</b><br/>',
        'pointFormat': 'Month: {point.x}<br/>Average Rating: {point.y:.2f} stars'
    }

    hc.options.legend = {  # Configura las opciones de la leyenda del gráfico
        'enabled': True,
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'top',
        'floating': False,  # La leyenda no flota sobre el gráfico
        'x': -10,  # Posición horizontal relativa
        'y': 50,   # Posición vertical relativa
        'itemStyle': {
            'fontSize': '12px',
            'fontWeight': 'normal'
        },
        'itemMarginTop': 3,
        'itemMarginBottom': 3,
        'symbolWidth': 16
    }

    # Ajustes adicionales para mejorar la apariencia y funcionalidad del gráfico

    hc.options.chart.marginRight = 420  # Margen derecho muy amplio para separar completamente la leyenda
    hc.options.chart.marginBottom = 60   # Margen inferior normal para las fechas
    hc.options.chart.height = 400  # Altura aumentada para zoom
    hc.options.chart.width = 1250  # Ancho aumentado para zoom
    hc.options.yAxis.min = 0  # Establece el valor mínimo del eje Y en 0
    hc.options.yAxis.max = 5  # Establece el valor máximo del eje Y en 5
    hc.options.yAxis.tickInterval = 0.5  # Establece el intervalo de las marcas del eje Y en 0.5

    # Ajustes adicionales para mejorar la apariencia y funcionalidad del gráfico
    hc.options.yAxis.labels = {  # Configura las etiquetas del eje Y
        'format': '{value} stars'
    }

    hc.options.accessibility = {  # Configura las opciones de accesibilidad para el gráfico
        'description': 'Image description: A line chart showing the average course ratings for different courses over several months. The X-axis represents the months, while the Y-axis represents the average ratings ranging from 0 to 5 stars. Each course is represented by a different colored line, allowing for easy comparison of their ratings over time.'
    }

    hc.options.chart.style = {  # Configura el estilo del gráfico
        'fontFamily': 'Arial, sans-serif'
    }

    hc.options.colors = [  # Define una paleta de colores personalizada para las series del gráfico
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]

    hc.options.responsive = {  # Configura las opciones de respuesta para el gráfico
        'rules': [{
            'condition': {
                'maxWidth': 800
            },
            'chartOptions': {
                'legend': {
                    'layout': 'horizontal',
                    'align': 'center',
                    'verticalAlign': 'bottom',
                    'floating': False,
                    'x': 0,
                    'y': 0,
                    'itemStyle': {
                        'fontSize': '10px'
                    },
                    'itemMarginTop': 3,
                    'itemMarginBottom': 3
                },
                'chart': {
                    'width': '100%',
                    'height': 450,
                    'marginRight': 20,
                    'marginBottom': 100
                }
            }
        }]
    }

    return wp

jp.justpy(app)
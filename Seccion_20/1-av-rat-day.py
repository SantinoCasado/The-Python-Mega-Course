import justpy as jp     # justpy es un framework web basado en Python que permite crear aplicaciones web interactivas de manera sencilla.
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pandas.read_csv("data/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day'])['Rating'].mean()

# Highchart documentation: https://www.highcharts.com/docs/chart-and-series-types
chart_def = """
{
    chart: {
        type: 'line',
        inverted: false
    },
    title: {
        text: 'Course Review Analysis'
    },
    subtitle: {
        text: 'Average Rating by Day'
    },
    xAxis: {
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            rotation: -45,
            style: {
                fontSize: '10px'
            }
        },
        accessibility: {
            rangeDescription: 'Range: Daily course ratings.'
        }
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        min: 1,
        max: 5,
        accessibility: {
            rangeDescription: 'Range: 1 to 5 stars.'
        },
        lineWidth: 2,
        gridLineWidth: 1
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Date: {point.x}<br/>Rating: {point.y:.2f} stars'
    },
    plotOptions: {
        line: {
            marker: {
                enabled: false
            },
            lineWidth: 1,
            dataLabels: {
                enabled: false
            }
        },
        series: {
            connectNulls: true,
            lineWidth: 1,
            marker: {
                enabled: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        type: 'line',
        lineWidth: 1,
        color: '#1f77b4',
        marker: {
            enabled: false
        },
        data: [
            [0, 4.5], [1, 4.2], [2, 4.7], [3, 4.1], [4, 4.6]
        ]
    }]
}
"""

# Documentation for classes https://justpy.io
def app():              # Define la función principal de la aplicación web, se puede llamar app o como se desee
    wp = jp.WebPage()   # crea una nueva página web utilizando justpy
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-4xl m-2 text-center q-pt-xs")  # agrega un encabezado de nivel 1 (h1)  y aplica clases CSS para el estilo
    pi = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-lg m-2 text-center")  # agrega un párrafo con texto descriptivo y aplica clases CSS para el estilo

    hc = jp.HighCharts(a=wp, options=chart_def)  # crea un gráfico de Highcharts en la página web utilizando la definición de gráfico proporcionada en chart_def
    
    # Configurar datos dinámicos del gráfico
    hc.options.xAxis.categories = list(day_average.index)  # establece las categorías del eje x utilizando las fechas del conjunto de datos
    hc.options.series[0].data = list(day_average)  # actualiza los datos del gráfico con las fechas y calificaciones promedio calculadas a partir del conjunto de datos

    return wp           # devuelve la página web creada

jp.justpy(app)  # inicia la aplicación web llamando a la función app definida anteriormente
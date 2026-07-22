import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("data/reviews.csv", parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week'])['Rating'].mean()

chart_def = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}"""


def app():
    wp = jp.QuasarPage()  # Crea una nueva página web utilizando justpy con el tema Quasar
    h1 = jp.QDiv(a=wp, text = "Weekly Average Ratings", classes="text-h3 text-center q-pa-md")  # agrega un encabezado de nivel 1 (h1) y aplica clases CSS para el estilo
    p1 = jp.QDiv(a=wp, text = "These graphs represent course review analysis", classes="text-subtitle1 text-center q-pa-md")  # agrega un párrafo con texto descriptivo y aplica clases CSS para el estilo


    hc = jp.HighCharts(a=wp, options=chart_def)  # Crea un gráfico de HighCharts y lo agrega a la página web
    hc.options.xAxis.categories = list(week_average.index)  # Establece las categorías del eje X del gráfico utilizando los índices del promedio semanal
    hc.options.series[0].data = list(week_average)  # Establece los datos de la serie del gráfico utilizando los valores del promedio semanal

    return wp

jp.justpy(app)
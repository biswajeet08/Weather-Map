import json
import requests
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Place


def map(request):
    """
    Returns: This method returns the 'map.html' with the processed weather data and the leaflet frontend to show the
            the locations stored in database with their max and min temp of the day.
    """
    weather_data = serialize('geojson', Place.objects.all(),
                             geometry_field='location',
                             fields=('name', 'place', 'location'))
    # print(weather_data)

    weather_data = update_weather_data(weather_data)
    weather_data = json.dumps(weather_data)
    return render(request, 'map.html', {'weather_data': weather_data})


def update_weather_data(weather_data):
    """
    Returns: This method adds the max and min temperature of a particular location and returns the processed data.
    """
    weather_data = json.loads(weather_data)
    features = weather_data.get('features')
    for i, feature in enumerate(features):
        coordinates = feature.get('geometry').get('coordinates')
        try:
            resp = requests.get(f"https://api.weather.gov/points/{coordinates[1]},{coordinates[0]}")
            forecast_link = resp.json().get('properties').get('forecast')
            resp2 = requests.get(forecast_link)
            temp_dict = {"max_T": str(resp2.json().get('properties').get('periods')[0].get('temperature'))+'F',
                         "min_T": str(resp2.json().get('properties').get('periods')[1].get('temperature'))+'F'}
        except:
            temp_dict = {"max_T": "N/A", "min_T": 'N/A'}

        weather_data['features'][i]['properties'].update(temp_dict)
    return weather_data


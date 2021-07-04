import requests

geojson_data = {"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": [
    {"type": "Feature", "properties": {"place": "New York"},
     "geometry": {"type": "Point", "coordinates": [-74.0155792133291, 40.7070859943043]}},
    {"type": "Feature", "properties": {"place": "Washington"},
     "geometry": {"type": "Point", "coordinates": [-77.04162596583593, 38.89274365045192]}}]}

geojson_data2 = {"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
                 "features": [{"type": "Feature", "properties": {"place": "New York"},
                               "geometry": {"type": "Point", "coordinates": [-74.0155792133291, 40.7070859943043]}},
                              {"type": "Feature", "properties": {"place": "Washington"},
                               "geometry": {"type": "Point", "coordinates": [-77.04162596583593, 38.89274365045192]}},
                              {"type": "Feature", "properties": {"place": "Cuttack"},
                               "geometry": {"type": "Point", "coordinates": [85.93008077639269, 20.41648949500153]}}]}

features = geojson_data2.get('features')
# print(features[0].get('geometry').get('geometry'))

forecast = {'@context': ['https://geojson.org/geojson-ld/geojson-context.jsonld',
                         {'@version': '1.1', 'wx': 'https://api.weather.gov/ontology#', 's': 'https://schema.org/',
                          'geo': 'http://www.opengis.net/ont/geosparql#', 'unit': 'http://codes.wmo.int/common/unit/',
                          '@vocab': 'https://api.weather.gov/ontology#',
                          'geometry': {'@id': 's:GeoCoordinates', '@type': 'geo:wktLiteral'},
                          'city': 's:addressLocality', 'state': 's:addressRegion',
                          'distance': {'@id': 's:Distance', '@type': 's:QuantitativeValue'},
                          'bearing': {'@type': 's:QuantitativeValue'}, 'value': {'@id': 's:value'},
                          'unitCode': {'@id': 's:unitCode', '@type': '@id'}, 'forecastOffice': {'@type': '@id'},
                          'forecastGridData': {'@type': '@id'}, 'publicZone': {'@type': '@id'},
                          'county': {'@type': '@id'}}], 'id': 'https://api.weather.gov/points/40.7070999,-74.0156',
            'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [-74.0156, 40.7070999]},
            'properties': {'@id': 'https://api.weather.gov/points/40.7070999,-74.0156', '@type': 'wx:Point',
                           'cwa': 'OKX', 'forecastOffice': 'https://api.weather.gov/offices/OKX', 'gridId': 'OKX',
                           'gridX': 32, 'gridY': 34,
                           'forecast': 'https://api.weather.gov/gridpoints/OKX/32,34/forecast',
                           'forecastHourly': 'https://api.weather.gov/gridpoints/OKX/32,34/forecast/hourly',
                           'forecastGridData': 'https://api.weather.gov/gridpoints/OKX/32,34',
                           'observationStations': 'https://api.weather.gov/gridpoints/OKX/32,34/stations',
                           'relativeLocation': {'type': 'Feature',
                                                'geometry': {'type': 'Point', 'coordinates': [-74.06476, 40.711417]},
                                                'properties': {'city': 'Jersey City', 'state': 'NJ',
                                                               'distance': {'value': 4171.3653072071,
                                                                            'unitCode': 'unit:m'},
                                                               'bearing': {'value': 96,
                                                                           'unitCode': 'unit:degrees_true'}}},
                           'forecastZone': 'https://api.weather.gov/zones/forecast/NYZ072',
                           'county': 'https://api.weather.gov/zones/county/NYC061',
                           'fireWeatherZone': 'https://api.weather.gov/zones/fire/NYZ072',
                           'timeZone': 'America/New_York', 'radarStation': 'KDIX'}}

geojson_data3 = {'@context': ['https://geojson.org/geojson-ld/geojson-context.jsonld',
                              {'@version': '1.1', 'wx': 'https://api.weather.gov/ontology#',
                               'geo': 'http://www.opengis.net/ont/geosparql#',
                               'unit': 'http://codes.wmo.int/common/unit/',
                               '@vocab': 'https://api.weather.gov/ontology#'}], 'type': 'Feature',
                 'geometry': {'type': 'Polygon', 'coordinates': [
                     [[-74.0250952, 40.7270524], [-74.0295579, 40.7053617], [-74.0009483, 40.7019775],
                      [-73.9964798, 40.723667899999995], [-74.0250952, 40.7270524]]]},
                 'properties': {'updated': '2021-07-03T18:22:46+00:00', 'units': 'us',
                                'forecastGenerator': 'BaselineForecastGenerator',
                                'generatedAt': '2021-07-03T19:09:03+00:00', 'updateTime': '2021-07-03T18:22:46+00:00',
                                'validTimes': '2021-07-03T12:00:00+00:00/P7DT1H',
                                'elevation': {'value': 2.1336, 'unitCode': 'unit:m'}, 'periods': [
                         {'number': 1, 'name': 'This Afternoon', 'startTime': '2021-07-03T15:00:00-04:00',
                          'endTime': '2021-07-03T18:00:00-04:00', 'isDaytime': True, 'temperature': 64,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '9 mph', 'windDirection': 'NE',
                          'icon': 'https://api.weather.gov/icons/land/day/rain_showers,50?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Mostly cloudy, with a high near 64. Northeast wind around 9 mph. Chance of precipitation is 50%.'},
                         {'number': 2, 'name': 'Tonight', 'startTime': '2021-07-03T18:00:00-04:00',
                          'endTime': '2021-07-04T06:00:00-04:00', 'isDaytime': False, 'temperature': 60,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '5 to 9 mph',
                          'windDirection': 'N',
                          'icon': 'https://api.weather.gov/icons/land/night/rain_showers,40/rain_showers,20?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Mostly cloudy, with a low around 60. North wind 5 to 9 mph. Chance of precipitation is 40%.'},
                         {'number': 3, 'name': 'Independence Day', 'startTime': '2021-07-04T06:00:00-04:00',
                          'endTime': '2021-07-04T18:00:00-04:00', 'isDaytime': True, 'temperature': 74,
                          'temperatureUnit': 'F', 'temperatureTrend': 'falling', 'windSpeed': '5 to 9 mph',
                          'windDirection': 'SW',
                          'icon': 'https://api.weather.gov/icons/land/day/rain_showers,20/rain_showers,40?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Mostly sunny. High near 74, with temperatures falling to around 72 in the afternoon. Southwest wind 5 to 9 mph. Chance of precipitation is 40%. New rainfall amounts less than a tenth of an inch possible.'},
                         {'number': 4, 'name': 'Sunday Night', 'startTime': '2021-07-04T18:00:00-04:00',
                          'endTime': '2021-07-05T06:00:00-04:00', 'isDaytime': False, 'temperature': 66,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '3 to 8 mph',
                          'windDirection': 'SW',
                          'icon': 'https://api.weather.gov/icons/land/night/rain_showers,40/rain_showers,20?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers before 2am. Partly cloudy, with a low around 66. Southwest wind 3 to 8 mph. Chance of precipitation is 40%. New rainfall amounts less than a tenth of an inch possible.'},
                         {'number': 5, 'name': 'Monday', 'startTime': '2021-07-05T06:00:00-04:00',
                          'endTime': '2021-07-05T18:00:00-04:00', 'isDaytime': True, 'temperature': 81,
                          'temperatureUnit': 'F', 'temperatureTrend': 'falling', 'windSpeed': '6 to 12 mph',
                          'windDirection': 'S', 'icon': 'https://api.weather.gov/icons/land/day/sct?size=medium',
                          'shortForecast': 'Mostly Sunny',
                          'detailedForecast': 'Mostly sunny. High near 81, with temperatures falling to around 78 in the afternoon. South wind 6 to 12 mph.'},
                         {'number': 6, 'name': 'Monday Night', 'startTime': '2021-07-05T18:00:00-04:00',
                          'endTime': '2021-07-06T06:00:00-04:00', 'isDaytime': False, 'temperature': 71,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '8 to 12 mph',
                          'windDirection': 'S', 'icon': 'https://api.weather.gov/icons/land/night/sct?size=medium',
                          'shortForecast': 'Partly Cloudy', 'detailedForecast': 'Partly cloudy, with a low around 71.'},
                         {'number': 7, 'name': 'Tuesday', 'startTime': '2021-07-06T06:00:00-04:00',
                          'endTime': '2021-07-06T18:00:00-04:00', 'isDaytime': True, 'temperature': 92,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '8 to 12 mph',
                          'windDirection': 'SW', 'icon': 'https://api.weather.gov/icons/land/day/sct?size=medium',
                          'shortForecast': 'Mostly Sunny', 'detailedForecast': 'Mostly sunny, with a high near 92.'},
                         {'number': 8, 'name': 'Tuesday Night', 'startTime': '2021-07-06T18:00:00-04:00',
                          'endTime': '2021-07-07T06:00:00-04:00', 'isDaytime': False, 'temperature': 74,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '6 to 10 mph',
                          'windDirection': 'SW', 'icon': 'https://api.weather.gov/icons/land/night/few?size=medium',
                          'shortForecast': 'Mostly Clear', 'detailedForecast': 'Mostly clear, with a low around 74.'},
                         {'number': 9, 'name': 'Wednesday', 'startTime': '2021-07-07T06:00:00-04:00',
                          'endTime': '2021-07-07T18:00:00-04:00', 'isDaytime': True, 'temperature': 89,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '8 mph', 'windDirection': 'SW',
                          'icon': 'https://api.weather.gov/icons/land/day/sct/tsra_hi,40?size=medium',
                          'shortForecast': 'Mostly Sunny then Chance Showers And Thunderstorms',
                          'detailedForecast': 'A chance of showers and thunderstorms after 2pm. Mostly sunny, with a high near 89. Chance of precipitation is 40%.'},
                         {'number': 10, 'name': 'Wednesday Night', 'startTime': '2021-07-07T18:00:00-04:00',
                          'endTime': '2021-07-08T06:00:00-04:00', 'isDaytime': False, 'temperature': 70,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '7 mph', 'windDirection': 'SW',
                          'icon': 'https://api.weather.gov/icons/land/night/tsra_sct,40?size=medium',
                          'shortForecast': 'Chance Showers And Thunderstorms',
                          'detailedForecast': 'A chance of showers and thunderstorms before 8pm, then a chance of showers and thunderstorms. Mostly cloudy, with a low around 70. Chance of precipitation is 40%.'},
                         {'number': 11, 'name': 'Thursday', 'startTime': '2021-07-08T06:00:00-04:00',
                          'endTime': '2021-07-08T18:00:00-04:00', 'isDaytime': True, 'temperature': 83,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '6 to 9 mph',
                          'windDirection': 'SW',
                          'icon': 'https://api.weather.gov/icons/land/day/rain_showers,40/rain_showers,50?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Partly sunny, with a high near 83. Chance of precipitation is 50%.'},
                         {'number': 12, 'name': 'Thursday Night', 'startTime': '2021-07-08T18:00:00-04:00',
                          'endTime': '2021-07-09T06:00:00-04:00', 'isDaytime': False, 'temperature': 66,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '7 mph', 'windDirection': 'W',
                          'icon': 'https://api.weather.gov/icons/land/night/rain_showers,50?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Mostly cloudy, with a low around 66. Chance of precipitation is 50%.'},
                         {'number': 13, 'name': 'Friday', 'startTime': '2021-07-09T06:00:00-04:00',
                          'endTime': '2021-07-09T18:00:00-04:00', 'isDaytime': True, 'temperature': 82,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '6 to 9 mph',
                          'windDirection': 'N',
                          'icon': 'https://api.weather.gov/icons/land/day/rain_showers,30?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Partly sunny, with a high near 82. Chance of precipitation is 30%.'},
                         {'number': 14, 'name': 'Friday Night', 'startTime': '2021-07-09T18:00:00-04:00',
                          'endTime': '2021-07-10T06:00:00-04:00', 'isDaytime': False, 'temperature': 68,
                          'temperatureUnit': 'F', 'temperatureTrend': None, 'windSpeed': '3 to 7 mph',
                          'windDirection': 'E',
                          'icon': 'https://api.weather.gov/icons/land/night/rain_showers,30/rain_showers?size=medium',
                          'shortForecast': 'Chance Rain Showers',
                          'detailedForecast': 'A chance of rain showers. Partly cloudy, with a low around 68. Chance of precipitation is 30%.'}]}}

for i, feature in enumerate(features):
    coordinates = feature.get('geometry').get('coordinates')
    # print(coordinates)
    try:
        resp = requests.get(f"https://api.weather.gov/points/{coordinates[1]},{coordinates[0]}")
        # print(resp.json())
        forecast_link = resp.json().get('properties').get('forecast')
        # print(resp.json().get('properties').get('forecast'))
        resp2 = requests.get(forecast_link)
        # max_T = resp2.json().get('properties').get('periods')[0].get('temperature')
        # min_T = resp2.json().get('properties').get('periods')[1].get('temperature')
        temp_dict = {"max_T": resp2.json().get('properties').get('periods')[0].get('temperature'),
                     "min_T": resp2.json().get('properties').get('periods')[1].get('temperature')}
    except:
        # max_T = 'N/A'
        # min_T = 'N/A'
        temp_dict = {"max_T": "N/A", "min_T": 'N/A'}

    # print(max_T, min_T)
    geojson_data2['features'][i]['properties'].update(temp_dict)
    # geojson_data2['features'][i]['properties']["min_T"] = min_T
print(geojson_data2)
data = {'type': 'FeatureCollection', 'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}}, 'features': [
    {'type': 'Feature', 'properties': {'place': 'New York', 'max_T': 65, 'min_T': 62},
     'geometry': {'type': 'Point', 'coordinates': [-74.0155792133291, 40.7070859943043]}},
    {'type': 'Feature', 'properties': {'place': 'Washington', 'max_T': 80, 'min_T': 63},
     'geometry': {'type': 'Point', 'coordinates': [-77.04162596583593, 38.89274365045192]}},
    {'type': 'Feature', 'properties': {'place': 'Cuttack', 'max_T': 'N/A', 'min_T': 'N/A'},
     'geometry': {'type': 'Point', 'coordinates': [85.93008077639269, 20.41648949500153]}}]}

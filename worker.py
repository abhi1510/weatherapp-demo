import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging

def fetch_data():
    api_token = '0c96a38dcbcdc8be'
    url = 'http://api.wunderground.com/api/' +api_token+ '/conditions/q/CA/San_Francisco.json'
    r = requests.get(url).json();
    data =r['current_observation'];

    #print(data)
    location = data['observation_location']['full']
    weather = data['weather']
    wind = data['wind_string']
    temp = data['temp_f']
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time = data['observation_time']

    #open db 
    try:
        conn = psycopg2.connect(host='localhost', dbname='weather', user='postgres', password='abhidb')
        print("Successfully connected to database")
    except:
        logging.exception("Unable to open database")        
    else:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute(''' INSERT INTO station_reading(location,weather,wind,temp,humidity,precip,icon_url,observation_time) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ''',(location, weather,wind,temp,humidity,precip,icon_url,observation_time))
    conn.commit()
    cursor.close()
    conn.close()

    print("Data written successfully!!!")   
 
    
fetch_data()
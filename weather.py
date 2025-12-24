import requests
import time
from datetime import datetime
import pytz

# Andhra Pradesh districts
districts = {
    "Anakapalli": (17.6913, 83.0039),
    "Anantapur": (14.6819, 77.6006),
    "Annamayya": (13.8000, 79.0000),
    "Bapatla": (15.9040, 80.4675),
    "Chittoor": (13.2172, 79.1003),
    "Dr. B.R. Ambedkar Konaseema": (16.5833, 82.0167),
    "East Godavari": (16.9634, 82.2351),
    "Eluru": (16.7107, 81.0952),
    "Guntur": (16.3067, 80.4365),
    "Kakinada": (16.9891, 82.2475),
    "Krishna": (16.5151, 80.6326),
    "Kurnool": (15.8281, 78.0373),
    "Nandyal": (15.4770, 78.4836),
    "NTR": (16.5062, 80.6480),
    "Palnadu": (16.1500, 80.2000),
    "Parvathipuram Manyam": (18.7833, 83.4333),
    "Prakasam": (15.5000, 79.5000),
    "Sri Potti Sriramulu Nellore": (14.4426, 79.9865),
    "Sri Sathya Sai": (14.1651, 77.8110),
    "Srikakulam": (18.2949, 83.8938),
    "Tirupati": (13.6288, 79.4192),
    "Visakhapatnam": (17.6868, 83.2185),
    "Vizianagaram": (18.1067, 83.3956),
    "West Godavari": (16.7107, 81.0952),
    "YSR Kadapa": (14.4674, 78.8241)
}


def get_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current_weather=true"
        "&daily=temperature_2m_min,temperature_2m_max,precipitation_probability_max"
        "&timezone=Asia/Kolkata"
    )
    return requests.get(url).json()

while True:
    # Clear screen (works in VS Code terminal)
    print("\033c", end="")

    # IST time
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist).strftime("%a, %d %b %Y %I:%M:%S %p, IST")

    print("ANDHRA PRADESH LIVE WEATHER DASHBOARD")
    print("Updated At:", now)
    print("=" * 50)

    for district, (lat, lon) in districts.items():
        data = get_weather(lat, lon)

        current_temp = data["current_weather"]["temperature"]
        min_temp = data["daily"]["temperature_2m_min"][0]
        max_temp = data["daily"]["temperature_2m_max"][0]
        rain_prob = data["daily"]["precipitation_probability_max"][0]

        print("District       :", district)
        print("Current Temp   :", current_temp, "°C")
        print("Next 24h Min   :", min_temp, "°C")
        print("Next 24h Max   :", max_temp, "°C")
        print("Rain Chance   :", rain_prob, "%")
        print("-" * 50)

    print("Refreshing again...\n")
    time.sleep(10)
    break
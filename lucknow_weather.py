import requests
import matplotlib.pyplot as plt

API_KEY = "ea74f14effd738a663cdf36945a42851"
city = "Lucknow"

# API URL for Lucknow
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description}")

    # Create simple bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(["Temperature", "Humidity"], [temperature, humidity], color=["orange", "skyblue"])
    plt.title(f"Current Weather in {city}")
    plt.ylabel("Value")
    plt.savefig("lucknow_weather_chart.png")
    plt.show()

else:
    print("Failed to fetch data. Please check the API key or city name.")


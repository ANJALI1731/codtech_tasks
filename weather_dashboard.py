import requests
import matplotlib.pyplot as plt

# ✅ Step 1: Enter your API key and city
API_KEY = "58098de98395a8fda0a6868b2a98a4ab"  # Replace with your own key if needed
city = 'Hyderabad'  # Change to your desired city

# ✅ Step 2: Build the API request URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# ✅ Step 3: Send request and get the response
response = requests.get(url)
data = response.json()

# ✅ Step 4: Extract temperature, humidity, and pressure
if response.status_code == 200:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    # ✅ Step 5: Print values in console
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"Pressure: {pressure} hPa")

    # ✅ Step 6: Visualize with a bar chart
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [temperature, humidity, pressure]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['skyblue', 'orange', 'green'])
    plt.title(f"Weather in {city}")
    plt.ylabel("Values")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("❌ Failed to retrieve data. Please check the API key or city name.")

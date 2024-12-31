import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"  # Replace with your email
receiver_email = "charlesopuba@gmail.com"
password = "your_password"  # Replace with your email password or app password

# Weather API configuration
api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
city = "Nairobi"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

def get_weather():
    response = requests.get(weather_url)
    data = response.json()
    if data["cod"] != 200:
        return "Failed to fetch weather data."
    
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    weather_report = (
        f"Weather in {city}:\n"
        f"Condition: {weather}\n"
        f"Temperature: {temperature}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s\n"
    )
    return weather_report

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    weather_report = get_weather()
    send_email("Weather Update for Nairobi", weather_report)
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/track')
def track():
    user_id = request.args.get('user_id')

    # Get the user's public IP address using Ipify API
    ipify_url = 'https://api.ipify.org?format=json'
    try:
        response = requests.get(ipify_url)
        ip_data = response.json()
        user_ip = ip_data.get('ip', 'Unknown IP')
    except requests.exceptions.RequestException:
        user_ip = 'Unable to retrieve IP'

    # Get geolocation data using Ipinfo.io API
    ipinfo_url = f'https://ipinfo.io/{user_ip}/json'
    try:
        geo_response = requests.get(ipinfo_url)
        geo_data = geo_response.json()
        
        # Extract geolocation details
        country = geo_data.get('country', 'Unknown Country')
        city = geo_data.get('city', 'Unknown City')
        region = geo_data.get('region', 'Unknown Region')
    except requests.exceptions.RequestException:
        country = city = region = 'Unable to retrieve geolocation data'

    # Print log with flush=True to ensure real-time output
    print(f"User ID: {user_id}, IP: {user_ip}, Location: {city}, {region}, {country}", flush=True)

    return f"Tracking data: User ID: {user_id}, IP: {user_ip}, Location: {city}, {region}, {country}"

if __name__ == '__main__':
    app.run(debug=True)

import streamlit as st
import requests

# Function to fetch disaster alerts from NASA EONET API
def fetch_disaster_alerts():
    # Make a request to the EONET API to fetch disaster events
    response = requests.get('https://eonet.gsfc.nasa.gov/api/v2.1/events')
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract relevant information from the response
        events = data.get('events', [])  # Get the list of events, default to empty list if not found
        return events
    else:
        st.error("Failed to fetch disaster alerts")

# Function to run the Streamlit app
def app():
    # Fetch disaster alerts from NASA EONET API
    alerts = fetch_disaster_alerts()

    # Display alerts on the Streamlit app
    st.title("Daily Disaster Alerts from NASA EONET")
    if alerts:
        for alert in alerts:
            st.write(f"**{alert['title']}**")
            st.write(f"*{alert['description']}*")
            categories = ", ".join(category['title'] for category in alert['categories'])
            st.write(f"Category: {categories}")
            geometries = alert.get('geometry', [])
            for geometry in geometries:
                st.write(f"Date: {geometry['date']}")
            st.write("---")
    else:
        st.write("No alerts available at the moment.")

# Run the Streamlit app
if __name__ == "__main__":
    app()

import streamlit as st
import requests

def fetch_real_time_weather(location):
    api_key = "97bf3b7b0d40cfa920f42806d9f3e4d68bb442e925caecd9dcf2719117330101"
    query = f"weather {location}"
    url = f"https://serpapi.com/search.json?q={query}&hl=en&gl=in&api_key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            snippets = [item.get('snippet', 'No snippet available') for item in data.get('organic_results', [])]
            answer_box = data.get('answer_box', {})
            return snippets, answer_box
        else:
            return [], f"Failed to fetch weather data. Status Code: {response.status_code}"
    except Exception as e:
        return [], f"An error occurred while fetching the weather data: {str(e)}"

# Streamlit UI components
st.title('Real-Time Weather Information')
location = st.text_input('Enter the location:')
if st.button('Fetch Weather'):
    if location:
        snippets, answer_box = fetch_real_time_weather(location)
        if snippets:
            for snippet in snippets:
                st.markdown(f"**RESULT:** {snippet}")
        if answer_box:
            st.markdown("**FINAL RESULT:**")
            weather = answer_box.get('weather', 'Not available')
            temperature = answer_box.get('temperature', 'Not available')
            humidity = answer_box.get('humidity', 'Not available')
            wind = answer_box.get('wind', 'Not available')
            date_time = answer_box.get('date', 'Date and time not specified')
            st.write(f"Weather: {weather}")
            st.write(f"Temperature: {temperature}")
            st.write(f"Humidity: {humidity}")
            st.write(f"Wind: {wind}")
            st.write(f"Date and Time: {date_time}")
        else:
            st.error("No answer box data found.")
    else:
        st.error('Please enter a location.')
import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDV4WzJV0KQlCAk1cwf1fqC5wW_i4WAyM4")

# Streamlit UI setup
st.title("AI-Powered Travel Planner")
st.write("Find the best travel options with cost, time, and convenience details.")

# User inputs
source = st.text_input("Enter Source:")
destination = st.text_input("Enter Destination:")

if st.button("Plan My Trip"):
    if source and destination:
        with st.spinner("Fetching travel details..."):
            prompt = f"""
            Generate a comprehensive travel plan from {source} to {destination}. Include:
            
            1. **Travel Mode Comparison**: List bike, cab, bus, train, and flight with estimated costs, travel time, and advantages/disadvantages.
            2. **Food & Rest Stops**: Recommend popular food items and notable restaurants along the way.
            3. **Best Time to Travel**: Suggest optimal travel times to save money and avoid traffic.
            4. **Follow-up Queries**: Provide answers for "What’s the cheapest option?" and "What’s the fastest route?".
            
            Present all information in an easy-to-read, structured format.
            """
            
            model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")
            response = model.generate_content(prompt)
            
            st.success("Your Travel Plan:", icon="🌍")
            st.markdown(response.text)
    else:
        st.warning("Please enter both source and destination.")

# import streamlit as st
# import google.generativeai as genai
# import os

# genai.configure(api_key="AIzaSyDV4WzJV0KQlCAk1cwf1fqC5wW_i4WAyM4")

# # Streamlit UI setup
# st.set_page_config(page_title="AI-Powered Travel Planner", layout="centered")
# st.title("🌍 AI-Powered Travel Planner")
# st.write("Plan your journey with ease! Get travel options, estimated costs, food stops, and the best travel times.")

# # User inputs
# source = st.text_input("📍 Enter Source:")
# destination = st.text_input("📍 Enter Destination:")

# if st.button("🚀 Generate Travel Plan"):
#     if source and destination:
#         with st.spinner("🔍 Fetching travel details..."):
#             prompt = f"""
#             Generate a comprehensive travel plan from {source} to {destination}. Ensure the following:
            
#             **1. Travel Mode Comparison:**
#             - Compare bike, cab, bus, train, and flight based on estimated costs, travel time, and pros/cons.
#             - Highlight the best option based on affordability and speed.
            
#             **2. Food & Rest Stops:**
#             - Recommend famous food items along the route.
#             - List well-rated restaurants and rest stops.
            
#             **3. Best Time to Travel:**
#             - Suggest peak vs. off-peak travel times for cost savings and avoiding traffic.
#             - Mention weather conditions if relevant.
            
#             **4. Follow-up Queries:**
#             - Provide clear answers for "What’s the cheapest option?" and "What’s the fastest route?".
            
#             **5. Safety & Travel Tips:**
#             - Suggest safety tips for night travel or solo trips.
#             - Provide guidance on tolls, fuel stations, and necessary travel documents.
            
#             Present the information in a user-friendly format, avoiding excessive bullet points.
#             """
            
#             model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-002")
#             response = model.generate_content(prompt)
            
#             st.success("✅ Your Travel Plan:")
#             st.markdown(response.text)
#     else:
#         st.warning("⚠️ Please enter both source and destination.")

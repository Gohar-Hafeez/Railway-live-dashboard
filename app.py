import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Railway Analytics Dashboard", layout="wide")

st.title("🚆 National Transit: Delay & Capacity Dashboard")
st.markdown("Yeh dashboard 100,000+ train trips ka live data analyze kar raha hai.")

@st.cache_data
def load_data():
 df = pd.read_csv("mega_railway_data.csv")
 return df

df = load_data()

st.sidebar.header("🔍 Filters")

selected_route = st.sidebar.selectbox("Select Route:", df['Route'].unique())

filtered_df = df[df['Route'] == selected_route]

# 5. Top Metrics (Summary Boxes)
col1, col2, col3= st.columns(3)
with col1:
    st.metric("Total Trips", f"{len(filtered_df):,}")
with col2:
    st.metric("Total Passengers", f"{filtered_df['Passengers'].sum():,}")
with col3:
    avg_delay = round(filtered_df['Delay_Minutes'].mean(), 1)
    st.metric("Avg Delay (Minutes)", avg_delay)


st.markdown("---") 

# 6. Graphs (Data Visualization)
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🌦️ Weather Impact on Delays")
    
    weather_delay = filtered_df.groupby('Weather')['Delay_Minutes'].mean().reset_index()
    fig1 = px.bar(weather_delay, x='Weather', y='Delay_Minutes', color='Weather', 
                  title="Average Delay by Weather Condition")
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("🚂 Train Load Distribution")
    
    train_load = filtered_df.groupby('Train_Name')['Passengers'].sum().reset_index()
    fig2 = px.pie(train_load, values='Passengers', names='Train_Name', 
                  title="Passenger Load per Train", hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)
import pandas as pd
import random
from datetime import datetime, timedelta

print("Khufiya Data Factory On Ho Gayi Hai... 1 Lakh rows ban rahi hain!")

# Pakistan Railway ke farzi routes aur trains
routes = ['Lahore - Karachi', 'Rawalpindi - Lahore', 'Peshawar - Quetta', 'Multan - Lahore', 'Karachi - Peshawar']
trains = ['Tezgam', 'Green Line', 'Awam Express', 'Karakoram', 'Shalimar']
weathers = ['Clear', 'Rain', 'Fog', 'Storm']

data = []
start_date = datetime(2025, 1, 1)

# 1 Lakh rows (trips) generate karne ka loop
for i in range(100000):
    # Random delay logic: Barish/Fog mein delay zyada hota hai
    weather = random.choice(weathers)
    if weather in ['Fog', 'Storm']:
        delay = random.randint(30, 300) # 30 se 300 minute ka delay
    else:
        delay = random.randint(0, 60)   # Normal din mein 0 se 60 min delay
        
    trip_date = start_date + timedelta(days=random.randint(0, 365))
    
    data.append({
        "Trip_ID": f"TRK-{10000 + i}",
        "Date": trip_date.strftime("%Y-%m-%d"),
        "Train_Name": random.choice(trains),
        "Route": random.choice(routes),
        "Weather": weather,
        "Passengers": random.randint(200, 1200),
        "Delay_Minutes": delay
    })

# DataFrame bana kar CSV mein save karna
df = pd.DataFrame(data)
df.to_csv("mega_railway_data.csv", index=False)

print("Mubarak Ho! 'mega_railway_data.csv' (100,000 rows) tayyar hai!")
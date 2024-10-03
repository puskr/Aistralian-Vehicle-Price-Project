
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\lenovo\Desktop\Australian Vehicle Prices.csv') #importing csv file


df['Price'] = pd.to_numeric(df['Price'], errors='coerce') #converting string to numeric

df.iloc[8:18][['Brand', 'Year', 'Model']]

df['Kilometres'] = pd.to_numeric(df['Kilometres'], errors='coerce')


# 1. Top 5 most expensive vehicles
top_5_expensive = df.nlargest(5, 'Price')[[ 'Title', 'Model', 'Car/Suv', 'Year']]
print(top_5_expensive)



# 2. Vehicles listed in each state

# Extract the state from the 'Location' column
df['State'] = df['Location'].str.split(', ').str[-1]


vehicles_per_state = df['State'].value_counts()
print(vehicles_per_state)



# 3. Vehicles with mileage greater than 100,000 km
high_mileage_vehicles = df[df['Kilometres'] > 100000][['Car/Suv', 'Model', 'Kilometres']]

print(high_mileage_vehicles)

# 4. Distinct brands in the dataset
distinct_brands = pd.DataFrame(df['Brand'].unique(), columns=['Brand'])
print(distinct_brands)


# 5. Average price based on transmission type
avg_price_transmission = df.groupby('Transmission')['Price'].mean().round(2)
print(avg_price_transmission)

# 6. Average price for each fuel type
avg_price_fuel_type = df.groupby('FuelType')['Price'].mean().round(2)
print(avg_price_fuel_type)



# 7. Top 10 most common vehicle models
top_10_models = df['Model'].value_counts().head(10)
print(top_10_models)

# 8. Correlation between mileage and price for each brand
correlation_mileage_price = df.groupby('Brand').apply(lambda x: x['Kilometres'].corr(x['Price']))
print(correlation_mileage_price)

# 9. Price distribution by year
price_distribution_year = df.groupby('Year')['Price'].describe()
print(price_distribution_year)

# 10. Count of vehicles by year and state, top 3 years with highest counts
vehicles_by_year_state = df.groupby(['Year', 'State']).size().reset_index(name='Count')
top_3_years = vehicles_by_year_state.groupby('Year')['Count'].sum().nlargest(3)
print(top_3_years)

# 11. Average price per brand compared to overall average
avg_price_brand = df.groupby('Brand')['Price'].mean()
overall_avg_price = df['Price'].mean()
comparison = avg_price_brand - overall_avg_price
print(comparison)


# 13. Percentage change in vehicle prices year-over-year
# Calculate average price per year
avg_price_per_year = df.groupby('Year')['Price'].mean().reset_index()
avg_price_per_year.columns = ['Year', 'Average Price']

# Calculate percentage change
avg_price_per_year['Previous Average Price'] = avg_price_per_year['Average Price'].shift(1)
avg_price_per_year['Percentage Change'] = (avg_price_per_year['Average Price'] - avg_price_per_year['Previous Average Price']) / avg_price_per_year['Previous Average Price'] * 100

# Display the relevant columns
print(avg_price_per_year[['Year', 'Average Price', 'Previous Average Price', 'Percentage Change']])


# 14. Rank of each vehicle model by price within its fuel type
df['Rank'] = df.groupby('FuelType')['Price'].rank(method='dense', ascending=False)
print(df['Rank'])
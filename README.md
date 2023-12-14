# IR_project_wpi
This is the code and related data of the final project for the wpi information retrieval class
This file is the recommend.py

# Rest of your script

import ssl

from geopy.geocoders import Nominatim

import certifi

import geopy.geocoders

from math import radians, sin, cos, sqrt, atan2

geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())

geolocator = Nominatim(user_agent="my_geocoder")


def get_coordinates(city_list):
    coordinates = []
    for city in city_list:
        location = geolocator.geocode(city)
        if location:
            lat, lon = location.latitude, location.longitude
            coordinates.append({"City": city, "Latitude": lat, "Longitude": lon})
        else:
            print(f"Unable to geocode {city}")
    return coordinates

"cities = ["Boston","New York City","Los Angeles","D.C.","Chicago",
          #"Seattle", "Atlanta", "Chicago", "Salt Lake City", "Houston", "Miami"]"

#city_coordinates = get_coordinates(cities)

#turn the geolocation into latitude

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
  
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
   
    radius = 6371.0
   
    distance = radius * c
    return distance

def calculate_similarity(coord1,coord2):
   
    distance = haversine_distance(coord1['Latitude'], coord1['Longitude'], coord2['Latitude'], coord2['Longitude'])
    
    similarity = 1 / (1 + distance)

    return similarity


def find_nearest_city(target_city, cities_data):
    target_location = geolocator.geocode(target_city)

    if target_location:
        target_lat, target_lon = target_location.latitude, target_location.longitude
        city1 = {"Latitude": target_lat, "Longitude": target_lon}

        City_similarity = []

        for city_data in cities_data:
            similarity_score = calculate_similarity(city1, city_data)
            City_similarity.append({"City": city_data["City"], "Similarity": similarity_score})

        # Find the city with the maximum similarity after the loop
        nearest_city = max(City_similarity, key=lambda x: x["Similarity"])

        # Store the result
        result_city = nearest_city['City']
        result_similarity = nearest_city['Similarity']

        print(
            f"\nThe city most similar to {target_city} is {result_city} with a similarity score of {result_similarity:.4f}")

        # Return the result if needed
        return result_similarity,result_city
    else:
        print(f"Unable to geocode {target_city}")
        return None


# Example usage
#target_city = input("Please enter the location: ")
#loca_similarity,nearest_city= find_nearest_city(target_city, city_coordinates)


#path= "/Users/a981199/Desktop/IR_dataset0.csv"
#table_data = pd.read_csv(path)
#selected_column_1 = 'Category'# Replace with the actual column name
#selected_value_1 = input("Enter the category: Clothing, Beauty&Health, Home, Food or Outdoors:") # Replace with the value you want to filte
#print (selected_value_1)
#filtered_rows_1 = table_data[table_data[selected_column_1] == selected_value_1]

#if filtered_rows_1.empty:
    #print('filtered1 empty')
#else:
    #print('0')

#device_model = input("Enter your device model: ")
def device_price(device_model):
    # Convert device_model to lowercase for case-insensitive matching
    device_model_lower = device_model.lower()
    if "iphone 15" in device_model_lower or "iphone 15 pro" in device_model_lower:
        result = "high"
    else:
        result = "low"
    return result

#product_value=device_price(device_model)
#print (product_value)
def column2(geosimilarity):
    if geosimilarity>=0.4:
        return 'Selling Price'  # Replace with the actual column name
    else:
        return 'Location'
#selected_column_2= column2(loca_similarity)

def product_price(product_value, filtered_rows, selected_column):

    if not filtered_rows.empty:
        column_values = filtered_rows[selected_column].tolist()
        print(column_values)
        if product_value == "high":
            result1 = max(column_values)
        else:
            result1 = min(column_values)
        return result1
    else:
        return None

#if selected_column_2=='Selling Price':
    selected_value_2 = product_price(product_value, filtered_rows_1, selected_column_2)
#else:
    selected_value_2= nearest_city

#print(selected_value_2)

# Filter rows based on the conditions
#filtered_rows_2 = filtered_rows_1[filtered_rows_1[selected_column_2] == selected_value_2]

# Check if any rows match the conditions
#if not filtered_rows_2.empty:
    # Print the information of the first matching row (you can modify as needed)
    #print("Information for the row with", selected_column_1, "=", selected_value_1, "and", selected_column_2, "=",
          #selected_value_2)
    #print(filtered_rows_2.iloc[0])
#else:
    #print("No matching rows found.")

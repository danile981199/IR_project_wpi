from flask import Flask, render_template, request
import recommmend
import pandas as pd


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])

def recommend():
    cities = ["Boston", "New York City", "Los Angeles", "D.C.", "Chicago",
              "Seattle", "Atlanta", "Chicago", "Salt Lake City", "Houston", "Miami"]

    city_coordinates = recommmend.get_coordinates(cities)

    path = "/Users/a981199/Desktop/IR_dataset0.csv"
    table_data = pd.read_csv(path)
    target_city = request.form['target_city']
    selected_value_1 = request.form['selected_value_1']
    device_model = request.form['device_model']
    loca_similarity, nearest_city = recommmend.find_nearest_city(target_city, city_coordinates)
    selected_column_1 = 'Category'

    filtered_rows_1 = table_data[table_data[selected_column_1] == selected_value_1]
    if filtered_rows_1.empty:
        print('filtered1 empty')
    else:
        print('0')

    product_value = recommmend.device_price(device_model)
    selected_column_2 = recommmend.column2(loca_similarity)
    if selected_column_2 == 'Selling Price':
        selected_value_2 = recommmend.product_price(product_value, filtered_rows_1, selected_column_2)
    else:
        selected_value_2 = nearest_city

    filtered_rows_2 = filtered_rows_1[filtered_rows_1[selected_column_2] == selected_value_2]

    return render_template('result.html', selected_value_1=selected_value_1,
                           selected_value_2=selected_value_2, filtered_rows_2=filtered_rows_2.to_html())

if __name__ == '__main__':
    app.run(debug=True)

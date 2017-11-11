from flask import Flask, send_file, request
from DataContext import *


app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/api/v1/get_all_food", methods=['GET'])
def return_all_foods():
    return get_product_list()


@app.route("/api/v1/get_all_recipes", methods=['GET'])
def return_all_recipes():
    # print(get_all_recipies())
    return get_all_recipies()


@app.route("/api/v1/calculate_water_score", methods=["POST"])
def calculate_water_score():
    data_body = json.loads(request.form.get('data'))
    return data_calculate_water_score(data_body)


if __name__ == '__main__':
    app.run(debug=True)

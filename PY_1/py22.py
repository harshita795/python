from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_2.2_CW

def is_even(number):
  return number % 2 == 0

@app.route("/even-numbers", methods=["GET"])
def even_numbers():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  result = []
  for num in numbers:
    if is_even(num):
      result.append(num)
  return jsonify(result) 

def is_adult(age):
  return age > 18

@app.route("/adult-ages", methods=["GET"])
def adult_ages():
  ages = [10, 20, 30, 40, 50]
  result = []
  for age in ages:
    if is_adult(age):
      result.append(age)
  return jsonify(result)

def is_smaller_than_file_size(size, limit):
  return size < limit

@app.route("/small-files", methods=["GET"])
def small_files():
  file_sizes = [25, 50, 75, 120, 90, 150]
  filter_param = float(request.args.get("filterParam", 50))
  result = []
  for size in file_sizes:
    if is_smaller_than_file_size(size, filter_param):
      result.append(size)
  return jsonify(result)

# PY_2.2_HW_1

def filterHighTemperatures(temp):
  return temp > 25

@app.route("/high-temperatures", methods=["GET"])
def high_temperatures():
  temperatures = [22, 26, 19, 30, 23, 28, 17, 31]
  high_temps = list(filter(filterHighTemperatures, temperatures))
  return jsonify(high_temps)

def filterLowPrices(price):
  return price <= 100

@app.route("/low-prices", methods=["GET"])
def low_prices():
  prices = [80, 120, 95, 150, 60, 110]
  low_prices = list(filter(filterLowPrices, prices))
  return jsonify(low_prices)

def filterHighRatings(rating):
  return rating > 3.5

@app.route("/high-ratings", methods=["GET"])
def high_ratings():
  ratings = [4.2, 3.8, 2.5, 4.7, 3.0, 4.9, 3.6]
  high_ratings = list(filter(filterHighRatings, ratings))
  return jsonify(high_ratings)

def filterLongIndianNames(name):
  return len(name) > 6

@app.route("/long-indian-names", methods=["GET"])
def long_indian_names():
  names = ['Akshay', 'Priyanka', 'Arjun', 'Anushka', 'Rajesh', 'Kavita']
  long_names = list(filter(filterLongIndianNames, names))
  return jsonify(long_names)

def filterCheaperProducts(product, price):
  return product < price

@app.route("/cheaper-products", methods=["GET"])
def cheaper_products():
  products = [10, 25, 50, 75, 100, 150, 200]
  filter_param = float(request.args.get("filterParam", 50))
  cheaper_products = list(filter(lambda product: filterCheaperProducts(product, filter_param), products))
  return jsonify(cheaper_products)



if __name__ == "__main__":
  app.run()


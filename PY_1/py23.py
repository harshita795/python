from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_2.3_CW

# products = [
#   {"name": "Laptop", "price": 75000, "category": "Electronics"},
#   {"name": "Smartphone", "price": 30000, "category": "Electronics"},
#   {"name": "Headphones", "price": 1500, "category": "Accessories"},
#   {"name": "Backpack", "price": 2000, "category": "Fashion"}
# ]

cars = [
  {"make": "Toyota", "model": "Corolla", "mileage": 15000},
  {"make": "Honda", "model": "Civic", "mileage": 25000},
  {"make": "Ford", "model": "Focus", "mileage": 30000}
]

# movies = [
#   {"title": "Inception", "genre": "Sci-Fi", "rating": 8},
#   {"title": "The Dark Knight", "genre": "Action", "rating": 9},
#   {"title": "Forrest Gump", "genre": "Drama", "rating": 7}
# ]

orders = [
  {"orderId": 101, "customerName": "Alice Johnson", "status": "Pending"},
  {"orderId": 102, "customerName": "Bob Smith", "status": "Shipped"},
  {"orderId": 103, "customerName": "Charlie Brown", "status": "Delivered"}
]

def filter_by_category(product, category):
  return product["category"] == category

@app.route("/products/category/<string:category>", methods=["GET"])
def get_products_by_category(category):
  result = [product for product in products if filter_by_category(product, category)]
  return jsonify(result)

def filter_cars_by_mileage(car, max_mileage):
  return car["mileage"] < max_mileage

@app.route("/cars/mileage/<int:max_mileage>", methods=["GET"])
def get_cars_by_mileage(max_mileage):
  result = [car for car in cars if filter_cars_by_mileage(car, max_mileage)]
  return jsonify(result)

def filter_movie_by_rating(movie, min_rating):
  return movie["rating"] > min_rating

@app.route("/movies/rating/<int:min_rating>", methods=["GET"])
def get_movies_by_rating(min_rating):
  result = [movie for movie in movies if filter_movie_by_rating(movie, min_rating)]
  return jsonify(result)

def filter_order_by_status(order, status):
  return order["status"] == status

@app.route("/orders/status/<string:status>", methods=["GET"])
def get_order_by_status(status):
  result = [order for order in orders if filter_order_by_status(order, status)]
  return jsonify(result)

# PY_2.3_HW_1

# employees = [
#   { "name": 'Rahul Gupta', "department": 'HR', "salary": 50000 },
#   { "name": 'Sneha Sharma', "department": 'Finance', "salary": 60000 },
#   { "name": 'Priya Singh', "department": 'Marketing', "salary": 55000 },
#   { "name": 'Amit Kumar', "department": 'IT', "salary": 65000 }
# ] 

def filter_by_department(employee, department):
  return employee["department"] == department

@app.route("/employees/department/<string:department>", methods=["GET"])
def get_employee_by_department(department):
  result = [employee for employee in employees if filter_by_department(employee, department)]
  return jsonify(result)

bikes = [
  { "make": 'Hero', "model": 'Splendor', "mileage": 80 },
  { "make": 'Bajaj', "model": 'Pulsar',"mileage": 60 },
  { "make": 'TVS', "model": 'Apache', "mileage": 70 }
]

def filter_biked_by_mileage(bike, min_mileage):
  return bike["mileage"] > min_mileage

@app.route("//bikes/mileage/<int:min_mileage>", methods=["GET"])
def get_bikes_by_mileage(min_mileage):
  result = [bike for bike in bikes if filter_biked_by_mileage(bike, min_mileage)]
  return jsonify(result)

def filter_bike_by_make(bike, make):
  return bike["make"] == make

@app.route("/bikes/make/<string:make>", methods=["GET"])
def get_bike_by_make(make):
  result = [bike for bike in bikes if filter_bike_by_make(bike, make)]
  return jsonify(result)

songs = [
  { "title": 'Tum Hi Ho', "genre": 'Romantic', "rating": 4 },
  { "title": 'Senorita', "genre": 'Pop', "rating": 5 },
  { "title": 'Dil Chahta Hai', "genre": 'Bollywood', "rating": 3 }
]

def filter_song_by_rating(song, min_rating):
  return song["rating"] > min_rating

@app.route("/songs/rating/<int:min_rating>", methods=["GET"])
def get_song_by_rating(min_rating):
  result = [song for song in songs if filter_song_by_rating(song, min_rating)]
  return jsonify(result)

def filter_song_by_genre(song, genre):
  return song["genre"] == genre

@app.route("/songs/genre/<string:genre>", methods=["GET"])
def get_song_by_genre(genre):
  result = [song for song in songs if filter_song_by_genre(song, genre)]
  return jsonify(result)

tasks = [
  { "taskId": 1, "taskName": 'Prepare Presentation', "status": 'pending' },
  { "taskId": 2, "taskName": 'Attend Meeting', "status": 'in-progress' },
  { "taskId": 3, "taskName": 'Submit Report', "status": 'completed' }
]

def filter_task_by_status(task, status):
  return task["status"] == status

@app.route("/tasks/status/<string:status>", methods=["GET"])
def get_task_by_status(status):
  result = [task for task in tasks if filter_task_by_status(task, status)]
  return jsonify(result)

# PY_2.3_HW_1

products = [
  { "name": 'Product A', "inStock": "true" },
  { "name": 'Product B', "inStock": "false" },
  { "name": 'Product C', "inStock": "true" },
  { "name": 'Product D', "inStock": "false" }
]

users = [
  { "name": 'Alice', "age": 25 },
  { "name": 'Bob', "age": 30 },
  { "name": 'Charlie', "age": 17 },
  { "name": 'Dave', "age": 16 }
]

productPrices = [
  { "name": 'Product A', "price": 50 },
  { "name": 'Product B', "price": 150 },
  { "name": 'Product C', "price": 200 },
  { "name": 'Product D', "price": 90 }
]

articles = [
  { "title": 'Article A', "wordCount": 400 },
  { "title": 'Article B', "wordCount": 600 },
  { "title": 'Article C', "wordCount": 700 },
  { "title": 'Article D', "wordCount": 300 }
]


movies = [
  { "title": 'Movie A', "rating": 8.5 },
  { "title": 'Movie B', "rating": 7.0 },
  { "title": 'Movie C', "rating": 9.0 },
  { "title": 'Movie D', "rating": 6.5 }
]

employees = [
  { "name": 'Employee A', "experience": 3 },
  { "name": 'Employee B', "experience": 6 },
  { "name": 'Employee C', "experience": 10 },
  { "name": 'Employee D', "experience": 2 }
]

def filter_by_stock(product):
  return product["inStock"] == "true"

@app.route("/in-stock-products", methods=["GET"])
def get_product_by_in_stock():
  result = [product for product in products if filter_by_stock(product)]
  return jsonify(result)

def filter_adult(user):
  return user["age"] >= 18

@app.route("/adult-users", methods=["GET"])
def get_user_by_age():
  result = [user for user in users if filter_adult(user)]
  return jsonify(result)

def filterExpensiveProducts(productPrice, price):
  return productPrice["price"] > price

@app.route("/expensive-products", methods=["GET"])
def get_expensive_product():
  price = int(request.args.get("price", 0))
  result = [productPrice for productPrice in productPrices if filterExpensiveProducts(productPrice, price)]
  return jsonify(result)

def filterLongArticles(article, minWords):
  return article["wordCount"] > minWords

@app.route("/long-articles", methods=["GET"])
def get_long_articles():
  minWords = int(request.args.get("minWords", 0))
  result = [article for article in articles if filterLongArticles(article, minWords)]
  return jsonify(result)

def filterHighRatedMovie(movie, rating):
  return movie["rating"] > rating

@app.route("/high-rated-movies", methods=["GET"])
def get_high_rated_movies():
  rating = float(request.args.get("rating", 0))
  result = [movie for movie in movies if filterHighRatedMovie(movie, rating)]
  return jsonify(result)

def filterExperiencedEmployees(employee, years):
  return employee["experience"] > years

@app.route("/experienced-employees", methods=["GET"])
def get_experienced_employees():
  years = float(request.args.get("years", 0))
  result = [employee for employee in employees if filterExperiencedEmployees(employee, years)]
  return jsonify(result)

if __name__ == "__main__":
  app.run()

from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_3.3_CW

# products = [
#   { 'productId': 1, 'name': 'Laptop', "price": 1000, 'inStock': True },
#   { 'productId': 2, 'name': 'Phone', "price": 25, 'inStock': True },
#   { 'productId': 3, 'name': 'Tablet', "price":  200, 'inStock': False },
#   { 'productId': 4, 'name': 'Keyboard', "price": 50, 'inStock': False }
# ]

users = [
  {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "role": "admin"},
  {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "role": "editor"},
  {"id": 3, "name": "Charlie Davis", "email": "charlie@example.com", "role": "viewer"},
  {"id": 4, "name": "Diana Evans", "email": "diana@gmail.com", "role": "admin"}
]

posts = [
  {"id": 1, "author": "Alice Johnson", "content": "Exploring the beauty of nature in the countryside."},
  {"id": 2, "author": "Bob Smith", "content": "Tips and tricks for mastering Python programming."},
  {"id": 3, "author": "Charlie Davis", "content": "Thoughts on the latest trends in technology."},
  {"id": 4, "author": "Diana Evans", "content": "Sharing my favorite recipes for quick and healthy meals."}
]

@app.route("/products/filter", methods=["GET"])
def filter_products():
  min_price = float(request.args.get("min_price", 0))
  max_price = float(request.args.get("max_price", float("inf")))

  filtered_products = []
  for product in products:
    if min_price <= product["price"] <= max_price and product["inStock"]:
      filtered_products.append(product)
  return jsonify(filtered_products)

@app.route("/users/find", methods=["GET"])
def find_users():
  role = request.args.get("role")
  email_domain = request.args.get("email_domain")

  matched_users = []
  for user in users:
    if user["role"] == role or user["email"].endswith(f"@{email_domain}"):
      matched_users.append(user)
  return jsonify(matched_users) 

@app.route("/posts/search", methods=["GET"])
def search_post():
  author = request.args.get("author")
  keyword = request.args.get("keyword")

  matched_posts = []
  for post in posts:
    if post["author"] == author or keyword.lower() in post["content"].lower():
      matched_posts.append(post)
  return jsonify(matched_posts)

# PY_3.3_HW_1

movies = [
  {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'available': True},
  {'id': 2, 'title': 'Titanic', 'genre': 'Romance', 'available': False},
  {'id': 3, 'title': 'The Dark Knight', 'genre': 'Action', 'available': True},
  {'id': 4, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'available': True},
]

students = [
  {'id': 1, 'name': 'Anna', 'major': 'Computer Science', 'gpa': 3.8},
  {'id': 2, 'name': 'Ben', 'major': 'Physics', 'gpa': 3.4},
  {'id': 3, 'name': 'Clara', 'major': 'Engineering', 'gpa': 3.9},
  {'id': 4, 'name': 'David', 'major': 'Computer Science', 'gpa': 2.8},
]

products = [
  {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
  {'id': 2, 'name': 'Headphones', 'category': 'Electronics', 'price': 100},
  {'id': 3, 'name': 'Coffee Maker', 'category': 'Appliances', 'price': 150},
  {'id': 4, 'name': 'Smartphone', 'category': 'Electronics', 'price': 800},
]

reviews = [
  {'id': 1, 'product_id': 1, 'rating': 4, 'content': 'Great laptop for work.'},
  {'id': 2, 'product_id': 2, 'rating': 5, 'content': 'Excellent sound quality.'},
  {'id': 3, 'product_id': 3, 'rating': 3, 'content': 'Works fine but feels cheap.'},
  {'id': 4, 'product_id': 4, 'rating': 4, 'content': 'Good value for money.'},
]

def filterMoviesByGenreAndAvailability(movies, genre, available):
  filtered_movies = []
  for movie in movies:
    if movie["genre"] == genre and movie["available"] == available:
      filtered_movies.append(movie)
  return jsonify({'Movies' : filtered_movies})


@app.route("/movies/filter", methods=["GET"])
def get_movies_by_genre_and_availability():
  genre = request.args.get("genre")
  available = request.args.get("available").lower() == "true"
  result = filterMoviesByGenreAndAvailability(movies, genre, available)
  return result

def findStudentsByMajorOrGPARange(students, min_gpa, max_gpa, major):
  filtered_students = []
  for student in students:
    if min_gpa <= student["gpa"] <= max_gpa and student["major"] == major:
      filtered_students.append(student)
  return jsonify({'Filtered Students' : filtered_students})

@app.route("/students/find", methods=["GET"])
def find_students():
  min_gpa = float(request.args.get("min_gpa", 0))
  max_gpa = float(request.args.get("max_gpa", float("inf")))
  major = request.args.get("major", "")
  result = findStudentsByMajorOrGPARange(students, min_gpa, max_gpa, major)
  return result

def deleteProductsByCategoryOrPrice(products, category, price):
  filter_products = []
  for product in products:
    if product["category"] != category and product["price"] != price:
      filter_products.append(product)
  return jsonify({'Remaining Products' : filter_products})

@app.route("/products/delete", methods=["GET"])
def delete_products():
  category = request.args.get("category", "")
  price = int(request.args.get("price", 0))
  result = deleteProductsByCategoryOrPrice(products, category, price)
  return result

def searchReviewsByProductAndRating(reviews, product_id, rating):
  filtered_reviews = []
  for review in reviews:
    if review["product_id"] == product_id and review["rating"] == rating:
      filtered_reviews.append(review)
  return jsonify({'Reviews' : filtered_reviews})

@app.route("/reviews/search", methods=["GET"])
def search_reviews():
  product_id = int(request.args.get("product_id", 0))
  rating = float(request.args.get("rating", 0))
  result = searchReviewsByProductAndRating(reviews, product_id, rating)
  return result

# PY_3.3_HW_2

customers= [
  {'id': 1, 'name': 'Alice', 'age': 30, 'city': 'New York', 'membership': 'Premium'},
  {'id': 2, 'name': 'Bob', 'age': 45, 'city': 'Los Angeles', 'membership': 'Basic'},
  {'id': 3, 'name': 'Eve', 'age': 28, 'city': 'San Francisco', 'membership': 'Gold'},
  {'id': 4, 'name': 'Frank', 'age': 60, 'city': 'Chicago', 'membership': 'Premium'}
]

cars = [
  {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 25000},
  {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 22000},
  {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'price': 35000},
  {'id': 4, 'make': 'Chevrolet', 'model': 'Malibu', 'year': 2020, 'price': 23000},
]

def filterCustomersByAgeAndMembership(customers, age, membership):
  filtered_customers = []
  for customer in customers:
    if customer["age"] == age and customer["membership"] == membership:
      filtered_customers.append(customer)
  return jsonify({'Filtered Customers' : filtered_customers})

@app.route("/customers/filter", methods=["GET"])
def filter_customer_by_age_and_membership():
  age = float(request.args.get("age", 0))
  membership = request.args.get("membership", "")
  result = filterCustomersByAgeAndMembership(customers, age, membership)
  return result

def findCarsByPriceOrYear(cars, price, year):
  filtered_cars = []
  for car in cars:
    if car["price"] == price or car["year"] == year:
      filtered_cars.append(car)
  return jsonify({'Filtered Cars' : filtered_cars})

@app.route("/cars/find", methods=["GET"])
def find_car_by_price_or_year():
  price = float(request.args.get("price", 0))
  year = int(request.args.get("year", 0))
  result = findCarsByPriceOrYear(cars, price, year)
  return result

def filterCustomersByCityOrMembership(customers, city, membership):
  filtered_customers = []
  for customer in customers:
    if customer["city"] == city or customer["membership"] == membership:
      filtered_customers.append(customer)
  return jsonify({'Filtered Customers' : filtered_customers})

@app.route("/customers/filterByCity", methods=["GET"])
def filter_customer_by_city_membership():
  city = request.args.get("city", "")
  membership = request.args.get("membership", "")
  result = filterCustomersByCityOrMembership(customers, city, membership)
  return result

def filterCarsByMakeAndYear(cars, make, year):
  filtered_cars = []
  for car in cars:
    if car["make"] == make and car["year"] == year:
      filtered_cars.append(car)
  return jsonify({'Filtered Cars' : filtered_cars})

@app.route("/cars/filter", methods=["GET"])
def filter_car_by_make_and_year():
  make = request.args.get("make", "")
  year = int(request.args.get("year", 0))
  result = filterCarsByMakeAndYear(cars, make, year)
  return result

def findCustomersByAgeOrCity(customers, age, city):
  filtered_customers = []
  for customer in customers:
    if customer["age"] == age or customer["city"] == city:
      filtered_customers.append(customer)
  return jsonify({'Filtered Customers' : filtered_customers})

@app.route("/customers/find", methods=["GET"])
def get_customer_by_age_or_city():
  age = float(request.args.get("age", 0))
  city = request.args.get("city", "")
  result = findCustomersByAgeOrCity(customers, age, city)
  return result


if __name__ == "__main__":
  app.run()
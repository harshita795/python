from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_2.4_CW

ages = [25, 30, 18, 22, 27]

cars = [
  {"make": "Toyota", "model": "Corolla", "mileage": 15},
  {"make": "Honda", "model": "Civic", "mileage":18},
  {"make": "Ford", "model": "Focus", "mileage": 20}
]

students = [
  {"name": "Rahul", "rollNo": 101, "marks": 85},
  {"name": "Sita", "rollNo": 102, "marks": 95},
  {"name": "Amit", "rollNo": 103, "marks": 70}
]

@app.route("/ages/sort-ascending", methods=["GET"])
def sort_ages_ascending():
  ages_copy = ages.copy()
  ages_copy.sort()
  return jsonify(ages_copy)

@app.route("/ages/sort-descending", methods=["GET"])
def sort_ages_descnding():
  ages_copy = ages.copy()
  ages_copy.sort(reverse=True)
  return jsonify(ages_copy)

def get_marks(student):
  return student["marks"]

@app.route("/students/sort-by-marks-descending", methods=["GET"])
def sort_students_by_marks_descending():
  students_copy = students.copy()
  students_copy.sort(key=get_marks, reverse=True)
  return jsonify(students_copy)

def get_mileage(car):
  return car["mileage"]

@app.route("/cars/sort-by-mileage-descending", methods=["GET"])
def sort_cars_by_mileage_descending():
  cars_copy = cars.copy()
  cars_copy.sort(key=get_mileage, reverse=True)
  return jsonify(cars_copy)

# PY_2.4_HW_1

heights = [160, 175, 180, 165, 170]

def sortHeightsAscending(heights_copy):
  return sorted(heights_copy)

@app.route("/heights/sort-ascending", methods=["GET"])
def sort_heights_ascending():
  heights_copy = heights.copy()
  sorted_heights = sortHeightsAscending(heights_copy)
  return jsonify(sorted_heights)

def sortHeightsDescending(heights):
  return sorted(heights, reverse=True)

@app.route("/heights/sort-descending", methods=["GET"])
def sort_heights_descending():
  sorted_heights = sortHeightsDescending(heights)
  return jsonify(sorted_heights)

# employees = [
#   { "name": 'Rahul', "employeeId": 101, "salary": 50000 },
#   { "name": 'Sita', "employeeId": 102, "salary": 60000 },
#   { "name": 'Amit', "employeeId": 103, "salary": 45000 }
# ]

def sortEmployeesBySalaryDescending(employees):
  return sorted(employees, key=lambda employee: employee["salary"], reverse=True)

@app.route("/employees/sort-by-salary-descending", methods=["GET"])
def get_employee_by_salary_descending():
  sorted_employee = sortEmployeesBySalaryDescending(employees)
  return jsonify(sorted_employee)

# books = [
#   { "title": 'The God of Small Things', "author": 'Arundhati Roy', "pages": 340 },
#   { "title": 'The White Tiger', "author": 'Aravind Adiga', "pages": 321 },
#   { "title": 'The Palace of Illusions', "author": 'Chitra Banerjee', "pages": 360 }
# ]

def sortBooksByPagesAscending(books):
  return sorted(books, key=lambda book: book["pages"])

@app.route("/books/sort-by-pages-ascending", methods=["GET"])
def get_books_by_pages_ascending():
  sorted_books = sortBooksByPagesAscending(books)
  return jsonify(sorted_books)

# PY_2.4_HW_1

books = [
   { "title": 'Moby Jonas', "author": 'Herman Melville', "publication_year": 2023 },
   { "title": '1984', "author": 'George Orwell', "publication_year": 1984 },
   { "title": 'A Tale of Two Cities', "author": 'Charles Jonas', "publication_year": 2000 },
]

employees = [
  { "name": 'John', "salary": 75000 },
  { "name": 'Doe', "salary": 30000 },
  { "name": 'Jane', "salary": 50000 }
]

products = [
  { "name": 'Product A', "price": 15 },
  { "name": 'Product B', "price": 25 },
  { "name": 'Product C', "price": 10 }
]

events = [
  { "name": 'Event A', "date": '2023-05-01' },
  { "name": 'Event B', "date": '2023-01-01' },
  { "name": 'Event C', "date": '2023-12-01' }
]

movies = [
  { "title": 'Movie A', "rating": 9.0 },
  { "title": 'Movie C', "rating": 7.0 },
  { "title": 'Movie B', "rating": 8.5 }
]

customers = [
  { "name": 'Customer A', "lastPurchase": '2023-06-15' },
  { "name": 'Customer B', "lastPurchase": '2023-11-01' },
  { "name": 'Customer C', "lastPurchase": '2023-03-10' }
]

def sortBooksByYear(books):
  return sorted(books, key=lambda book: book["publication_year"])

@app.route("/books/sort-by-year", methods=["GET"])
def get_book_by_year_ascending():
  sorted_books = sortBooksByYear(books)
  return jsonify(sorted_books)

def sortEmployeesBySalary(employees):
  return sorted(employees, key=lambda employee: employee["salary"], reverse=True)

@app.route("/employees/sort-by-salary", methods=["GET"])
def get_employees_by_salary_descending():
  sorted_employees = sortEmployeesBySalary(employees)
  return jsonify(sorted_employees)

def sortProductsByPrice(products):
  return sorted(products, key=lambda product: product["price"])

@app.route("/products/sort-by-price", methods=["GET"])
def get_product_by_price_ascending():
  sorted_products = sortProductsByPrice(products)
  return jsonify(sorted_products)

def sortEventsByDate(events):
  return sorted(events, key=lambda event: event["date"])

@app.route("/events/sort-by-date", methods=["GET"])
def get_event_by_date_ascending():
  sorted_events = sortEventsByDate(events)
  return jsonify(sorted_events)

def sortMoviesByRating(movies):
  return sorted(movies, key=lambda movie: movie["rating"], reverse=True)

@app.route("/movies/sort-by-rating", methods=["GET"])
def get_movies_by_rating_descending():
  sorted_movies = sortMoviesByRating(movies)
  return jsonify(sorted_movies)

def sortCustomersByLastPurchase(customers):
  return sorted(customers, key=lambda customer: customer["lastPurchase"], reverse=True)

@app.route("/customers/sort-by-last-purchase", methods=["GET"])
def get_customers_by_lastpurchase_descending():
  sorted_customers = sortCustomersByLastPurchase(customers)
  return jsonify(sorted_customers)


if __name__ == "__main__":
  app.run()
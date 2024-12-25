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

employees = [
  { "name": 'Rahul', "employeeId": 101, "salary": 50000 },
  { "name": 'Sita', "employeeId": 102, "salary": 60000 },
  { "name": 'Amit', "employeeId": 103, "salary": 45000 }
]

def sortEmployeesBySalaryDescending(employees):
  return sorted(employees, key=lambda employee: employee["salary"], reverse=True)

@app.route("/employees/sort-by-salary-descending", methods=["GET"])
def get_employee_by_salary_descending():
  sorted_employee = sortEmployeesBySalaryDescending(employees)
  return jsonify(sorted_employee)

books = [
  { "title": 'The God of Small Things', "author": 'Arundhati Roy', "pages": 340 },
  { "title": 'The White Tiger', "author": 'Aravind Adiga', "pages": 321 },
  { "title": 'The Palace of Illusions', "author": 'Chitra Banerjee', "pages": 360 }
]

def sortBooksByPagesAscending(books):
  return sorted(books, key=lambda book: book["pages"])

@app.route("/books/sort-by-pages-ascending", methods=["GET"])
def get_books_by_pages_ascending():
  sorted_books = sortBooksByPagesAscending(books)
  return jsonify(sorted_books)





if __name__ == "__main__":
  app.run()
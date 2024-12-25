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



if __name__ == "__main__":
  app.run()
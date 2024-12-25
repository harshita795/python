from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_3.1_CW

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Rahul", "Priya", "Anuj", "Harshita", "Rakul"]
employees = [
  {"employeeId": 1, "name": "Rahul"},
  {"employeeId": 2, "name": "Sita"},
  {"employeeId": 3, "name": "Rita"}
]
contacts = [
  {"phoneNumber": "8362652534", "name":"Rahul", "address": "123 Street, City"},
  {"phoneNumber": "8362675434", "name":"Sita", "address": "456 Avenue, City"},
  {"phoneNumber": "8362989534", "name":"Amit", "address": "789 Street, City"}
]

@app.route("/numbers/find/<int:number>", methods=["GET"])
def get_number(number):
  for ele in numbers:
    if ele == number:
      return jsonify(ele)
  return jsonify(None)

@app.route("/names/find/<string:name>", methods=["GET"])
def get_name(name):
  for ele in names:
    if ele == name:
      return jsonify(ele)
  return jsonify(None)

@app.route("/employees/find/<int:id>", methods=["GET"])
def get_employee_id(id):
  for ele in employees:
    if ele["employeeId"] == id:
      return jsonify(ele)
  return jsonify(None)

@app.route("/contacts/find/<string:phoneNumber>", methods=["GET"])
def get_phone_number(phoneNumber):
  for ele in contacts:
    if ele["phoneNumber"] == phoneNumber:
      return jsonify(ele)
  return jsonify(None)


if __name__ == "__main__":
  app.run()
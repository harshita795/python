from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_3.1_CW

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Rahul", "Priya", "Anuj", "Harshita", "Rakul"]
# employees = [
#   {"employeeId": 1, "name": "Rahul"},
#   {"employeeId": 2, "name": "Sita"},
#   {"employeeId": 3, "name": "Rita"}
# ]
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

# PY_3.1_HW_1

users = [
  {'id': 1, 'username': 'ankit', 'fullName': 'Ankit Kumar'},
  {'id': 2, 'username': 'dhananjit', 'fullName': 'Dhananjit Singh'},
]

credit_cards = [
  {'number': '1234567890123456', 'holder': 'John Doe', 'expiry': '12/24'},
  {'number': '9876543210987654', 'holder': 'Jane Smith', 'expiry': '01/25'},
]

users_details = [
  {'email': 'johndoe@example.com', 'name': 'John Doe', 'age': 30},
  {'email': 'janesmith@example.com', 'name': 'Jane Smith', 'age': 25},
]

books = [
  {'isbn': '9783161484100', 'title': 'Example Book', 'author': 'John Author'},
  {'isbn': '9781234567897', 'title': 'Another Book', 'author': 'Jane Writer'},
]

people = [
  {'ssn': '123-45-6789', 'name': 'John Doe', 'birthDate': '1990-01-01'},
  {'ssn': '987-65-4321', 'name': 'Jane Smith', 'birthDate': '1985-05-05'},
]

@app.route("/username/find/<string:username>", methods=["GET"])
def get_username(username):
  for ele in users:
    if ele["username"] == username:
      return jsonify({'result' : 'Username is available'})
  return jsonify({'result' : 'Username is not available'})

def findCreditCard(credit_cards, cardNumber):
  for ele in credit_cards:
    if ele["number"] == cardNumber:
      return jsonify({'creditCard' : ele})
  return jsonify(None)

@app.route("/credit-cards/find/<string:cardNumber>", methods=["GET"])
def get_credit_card_number(cardNumber):
  credit_card = findCreditCard(credit_cards, cardNumber)
  return credit_card

def findUserByEmail(users_details, email):
  for ele in users_details:
    if ele["email"] == email:
      return jsonify({'user' : ele})
  return jsonify(None)

@app.route("/emails/find/<string:email>", methods=["GET"])
def get_user_email(email):
  user_email = findUserByEmail(users_details, email)
  return user_email

def findBookByISBN(books, isbn):
  for ele in books:
    if ele["isbn"] == isbn:
      return jsonify({'book' : ele})
  return jsonify(None)

@app.route("/books/find/<string:isbn>", methods=["GET"])
def get_book_isbn(isbn):
  book = findBookByISBN(books, isbn)
  return book

def findPeopleBySSN(people, ssn):
  for ele in people:
    if ele["ssn"] == ssn:
      return jsonify({"person" : ele})
  return jsonify(None)

@app.route("/ssn/find/<string:ssn>", methods=["GET"])
def get_people_ssn(ssn):
  person = findPeopleBySSN(people, ssn)
  return person


if __name__ == "__main__":
  app.run()
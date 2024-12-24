from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_2.1_CW

person = {
  "firstname" : "Harshita",
  "lastname" : "Yadav",
  "gender" : "female",
  "age" : 22,
  "isMember" : True
}

def get_full_name(person):
  return f"{person["firstname"]} {person["lastname"]}"

@app.route("/person/fullname", methods=["GET"])
def get_person_full_name():
  fullname = get_full_name(person)
  return jsonify({"fullName" : fullname})

def get_firstname_and_gender(person):
  return {"firstname": person["firstname"], "gender": person["gender"]}

@app.route("/person/firstname-gender", methods=["GET"])
def get_person_firstname_and_gender():
  firstname_and_gender = get_firstname_and_gender(person)
  return jsonify(firstname_and_gender)

def increment_age(person):
  person["age"] += 1
  return person

@app.route("/person/increment-age", methods=["GET"])
def increment_person_age():
  updated_person = increment_age(person)
  return jsonify(updated_person)

male_image_url = "https://via.placeholder.com/150/0000FF?text=Male"
female_image_url = "https://via.placeholder.com/150/0000FF?text=Female"
unknown_image_url = "https://via.placeholder.com/150/0000FF?text=Unknown"

def get_profile_image(person):
  if person["gender"].lower() == "male":
    return male_image_url
  elif person["gender"].lower() == "female":
    return female_image_url
  else:
    return unknown_image_url

@app.route("/person/profile-image", methods=["GET"])
def get_person_profile_image():
  profile_image = get_profile_image(person)
  return jsonify({"profileImage" : profile_image})

def get_final_price(cart_total, is_member):
  discount = 0.10
  if is_member:
    final_price = cart_total * (1 - discount)
  else:
    final_price = cart_total
  return {"final_price": f"{final_price}"}

@app.route("/person/final-price", methods=["GET"])
def get_person_final_price():
  cart_total = float(request.args.get("cartTotal", 0))
  final_price = get_final_price(cart_total, person["isMember"])
  return jsonify(final_price)

# PY_2.1_HW_1

# Book data
book = {
    'title': 'The God of Small Things',
    'author': 'Arundhati Roy',
    'publicationYear': 1997,
    'genre': 'Novel',
    'isAvailable': True,
    'stock': 5,
}



if __name__ == "__main__":
  app.run()
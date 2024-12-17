from flask import Flask, request, jsonify

app = Flask(__name__)

# welcome route

@app.route("/", methods=["GET"])
def api_welcome():
  return jsonify({"message": "Welcome to the Flask API."})

# shout route
@app.route("/shout", methods=["GET"])
def shout():
  name = request.args.get("name", "")
  uppercase_name = name.upper()
  return uppercase_name
 
# fullname route
@app.route("/fullname", methods=["GET"]) 
def fullname():
  first_name = request.args.get("firstname", "")
  last_name = request.args.get("lastname", "")
  fullname = f"{first_name} {last_name}"
  return fullname

# @app.route("/date", methods=["GET"])
# def formatdate():
#   month = request.args.get("month", "")
#   year = request.args.get("year","")
#   formatted_date = f"{month} {year}"
#   return formatted_date

# @app.route("/greet", methods=["GET"])
# def greet():
#   name = request.args.get("name", "")
#   greeting =f"Namaste, {name}"
#   return greeting

@app.route("/address", methods=["GET"])
def address():
  street = request.args.get("street", "")
  city = request.args.get("city", "")
  state = request.args.get("state", "")
  formatted_address = f"{street}, {city}, {state}"
  return formatted_address

# PY_1.1_HW_1

@app.route("/whisper", methods=["GET"])
def whisper():
  name = request.args.get("name", "")
  lowercase_name = name.lower()
  return lowercase_name

@app.route("/productname", methods=["GET"])
def productname():
  company_name = request.args.get("companyName", "")
  product_name = request.args.get("productName", "")
  fullname = f"{company_name} {product_name}"  
  return fullname

@app.route("/date", methods=["GET"])
def formattedDate():
  month = request.args.get("month","")
  year = request.args.get("year", "")
  formattedDate = f"{month}/{year}"
  return formattedDate

@app.route("/greet", methods=["GET"])
def greet():
  city = request.args.get("city", "")
  greeting = f"You live in {city}"
  return greeting


@app.route("/capital", methods=["GET"])
def capital():
  capital = request.args.get("capital", "")
  country = request.args.get("country", "")
  countryCapital = f"{capital} is the capital of {country}."
  return countryCapital

@app.route("/email", methods=["GET"])
def email():
  first_name = request.args.get("firstName", "")
  last_name = request.args.get("lastName", "")
  domain = request.args.get("domain", "")
  email = f"{first_name}.{last_name}@{domain}"
  return email

@app.route("/custom-commit", methods=["GET"])
def customCommit():
  commit_type = request.args.get("type", "")
  message = request.args.get("message", "")
  customCommit = f"{commit_type}: {message}"
  return customCommit

@app.route("/certificate", methods=["GET"])
def certificate():
  first_name = request.args.get("firstName", "")
  last_name = request.args.get("lastName", "")
  course_name = request.args.get("courseName", "")
  certificate = f"This certification is awarded to {first_name} {last_name} for completing the course {course_name}"
  return certificate

@app.route("/autoreply", methods=["GET"])
def autoreply():
  start_month = request.args.get("startMonth", "")
  end_month = request.args.get("endMonth", "")
  autoreply = f"""Dear customer, thank you for reaching out to me.<br>
  Unfortunately, I'm out of office from {start_month} till {end_month}. Your enquiry will be resolved by another colleague."""  
  return autoreply

@app.route("/secureurl", methods=["GET"])
def secureurl():
  domain = request.args.get("domain", "")
  secureurl = f"https://{domain}"
  return secureurl  

if __name__ == "__main__":
  app.run()
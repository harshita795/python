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


# PY_1.1_HW_2

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

@app.route("/sendotp", methods=["GET"])
def sendotp():
  otp_code = request.args.get("otpCode", "")
  sendotp = f"Your OTP for account verification is {otp_code}. Do not share this with anyone"
  return sendotp

@app.route("/welcome", methods=["GET"])
def welcome():
  first_name = request.args.get("firstName", "")
  email = request.args.get("email", "")
  welcome = f"Hey {first_name}. We're excited to have you here, we'll send future notifications to your registered mail ({email})"
  return welcome


@app.route("/github-profile", methods=["GET"])
def githubProfile():
  username = request.args.get("userName", "")
  githubProfile = f"https://github.com/{username}"
  return githubProfile

@app.route("/text-to-csv", methods=["GET"])
def textToCsv():
  id = request.args.get("id","")
  email = request.args.get("email", "")
  roll_number = request.args.get("rollNumber", "")
  textToCsv = f"{id}, {email}, {roll_number}"
  return textToCsv

# PY_1.2_HW_1 (operators)

@app.route("/total-distance", methods=["GET"])
def total_distance():
  distance1 = float(request.args.get("distance1", 0))
  distance2 = float(request.args.get("distance2", 0))  
  total_distance = distance1 + distance2
  return str(total_distance)

@app.route("/total-time", methods=["GET"])
def total_time():
  time1 = float(request.args.get("time1", 0))
  time2 = float(request.args.get("time2", 0))
  time3 = float(request.args.get("time3", 0))
  total_time = time1 + time2 + time3
  return str(total_time)

@app.route("/average-speed", methods=["GET"])
def average_speed():
  total_distance = float(request.args.get("totalDistance", 0))
  total_time = float(request.args.get("totalTime", 1))
  average_speed = total_distance / total_time
  return str(average_speed)

@app.route("/interest-earned", methods=["GET"])
def interest_earned():
  principal = float(request.args.get("principal", 1))
  rate = float(request.args.get("rate", 1))
  time = float(request.args.get("time", 1))
  interest_earned = (principal * rate * time) / 100
  return str(interest_earned)

@app.route("/total-marks", methods=["GET"])
def total_marks():
  marks1 = float(request.args.get("marks1", 0))
  marks2 = float(request.args.get("marks2", 0))
  totalMarks = marks1 + marks2
  return str(totalMarks)

@app.route("/total-weight", methods=["GET"])
def total_weight():
  weight1 = float(request.args.get("weight1", 0))
  weight2 = float(request.args.get("weight2", 0))
  weight3 = float(request.args.get("weight3", 0))
  totalWeight = weight1 + weight2 + weight3
  return str(totalWeight)

@app.route("/monthly-salary", methods=["GET"])
def monthly_salary():
  annual_salary = float(request.args.get("annualSalary", 0))
  monthly_salary = annual_salary / 12
  return str(monthly_salary)  

@app.route("/total-pages", methods=["GET"]) 
def total_pages():
  pagesPerDay = float(request.args.get("pagesPerDay", 1))
  days = float(request.args.get("days", 1))
  totalPages = pagesPerDay * days
  return str(totalPages)

@app.route("/currency-conversion", methods=["GET"])
def currency_conversion():
  amount = float(request.args.get("amount", 1))
  exchangeRate = float(request.args.get("exchangeRate", 1))
  convertedAmount = amount * exchangeRate
  return str(convertedAmount)

@app.route("/average-sales", methods=["GET"])
def average_sales():
  sales1 = float(request.args.get("sales1", 1))  
  sales2 = float(request.args.get("sales2", 1))
  sales3 = float(request.args.get("sales3", 1))
  avgSales = (sales1 + sales2 + sales3) / 3

  return f"{avgSales:.2f}"

# PY_1.2_HW_2 (operators)

@app.route("/bmi", methods=["GET"])
def bmi():
  height = float(request.args.get("height", 1)) 
  weight = float(request.args.get("weight", 0))
  bmi =  weight / (height * height) 
  return f"Your BMI is {bmi:.2f}"

@app.route("/checkout", methods=["GET"])
def checkout():
  product = request.args.get("product", 0)
  units = int(request.args.get("units", 0))
  price = float(request.args.get("price", 0))
  total_price = price * units
  return f"Your total for {units} {product} is {int(total_price)}"

@app.route("/grade", methods=["GET"])
def grade():
  maths = float(request.args.get("maths", 0))
  science = float(request.args.get("science", 0))
  english = float(request.args.get("english", 0))
  gradeInPercentage = ((maths + science + english) / 300 ) * 100
  return f"Your grade in percentage is {round(gradeInPercentage)}%"

@app.route("/discounted-price", methods=["GET"])
def discountedPrice():
  cartTotal = float(request.args.get("cartTotal", 0))
  discount = float(request.args.get("discount", 0)) 
  total_price = cartTotal - ( cartTotal * ( discount / 100 ) )
  return f"Result: Your bill amount is {total_price:.1f}"


@app.route("/split-bill", methods=["GET"])
def splitBill():
  billAmount = float(request.args.get("billAmount", 0))
  numberOfFriends = int(request.args.get("numberOfFriends", 1))
  splitAmount = billAmount / numberOfFriends
  return f"Result: Each friend owes ₹{int(splitAmount)} against the bill"

@app.route("/celsius-to-fahrenheit", methods=["GET"])
def celsius_to_fahrenheit():
  temperature = float(request.args.get("temperature", 0))
  fahrenheit = temperature * 9/5 + 32 
  return f"Result: {int(fahrenheit)} Fahrenheit"

@app.route("/monthly_salary", methods=["GET"])
def monthly_Salary():
  totalHours = float(request.args.get("totalHours", 1))
  hourlyWage = float(request.args.get("hourlyWage", 1))
  monthly_salary = hourlyWage * totalHours
  return f"Result: Your monthly salary is ₹{int(monthly_salary)}"
  

if __name__ == "__main__":
  app.run()
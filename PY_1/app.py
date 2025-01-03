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

# @app.route("/greet", methods=["GET"])
# def greet():
#   city = request.args.get("city", "")
#   greeting = f"You live in {city}"
#   return greeting

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

# @app.route("/welcome", methods=["GET"])
# def welcome():
#   first_name = request.args.get("firstName", "")
#   email = request.args.get("email", "")
#   welcome = f"Hey {first_name}. We're excited to have you here, we'll send future notifications to your registered mail ({email})"
#   return welcome


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

# @app.route("/monthly-salary", methods=["GET"])
# def monthly_salary():
#   annual_salary = float(request.args.get("annualSalary", 0))
#   monthly_salary = annual_salary / 12
#   return str(monthly_salary)  

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
  
# PY_1.3_CW (if-Else)

@app.route("/check-number", methods=["GET"])
def check_number():
  number = float(request.args.get("number", 0))
  if number >= 0:
    result = "positive"
  else:
    result = "negative"
  return f"Number is {result}"

@app.route("/check-login", methods=["GET"])
def check_login():
  is_logged_in = request.args.get("isLoggedIn", "false") == "true"
  if is_logged_in:
    result = "User is logged in"
  else: 
    result = "User is not logged in"
  return result
  
@app.route("/check-temperature", methods=["GET"])
def check_temperature():
  temperature = float(request.args.get("temperature", 0))
  if temperature < 15:
    result = "cold"
  elif temperature <= 25:
    result = "warm"
  else:
    result = "hot"
  return f"Temperature is {result}"

@app.route("/check-engagement", methods=["GET"])
def check_engagement():
  likes = int(request.args.get("likes", 0))
  if likes < 100:
    result = "low"
  elif likes <= 500:
    result = "moderate"
  else:
    result = "high"
  return f"Engagement level is {result}"

# PY_1.3_HW_1 (if-Else)

@app.route("/check-whole-number", methods=["GET"])
def check_whole_number():
  number = float(request.args.get("number", 0))
  if number >= 0:
    result = "whole"
  else:
    result = "not whole"
  return f"Number is {result} number"

@app.route("/check-equal", methods=["GET"])
def check_equal():
  num1 = float(request.args.get("num1", 0))
  num2 = float(request.args.get("num2", 0))
  if num1 == num2:
    result = "equal"
  else:
    result = "not equal"
  return f"Numbers are {result}"

@app.route("/check-active", methods=["GET"])
def check_active():
  isActive = request.args.get("isActive", "false") == "true"
  if isActive:
    result = "User is active"
  else:
    result = "User is not active"
  return result

@app.route("/check-discount", methods=["GET"])
def check_discount():
  cost = float(request.args.get("cost", 0))
  if cost > 1000:
    result = "User is eligible for a discount"
  else:
    result = "User is not eligible for a discount"
  return result

@app.route("/check-experience", methods=["GET"])
def check_experience():
  years = float(request.args.get("years", 0))
  if years > 0:
    result = "experienced"
  elif years < 0:
    result = "non-working"
  else:
    result = "fresher"
  return f"Person is {result}"

@app.route("/check-result", methods=["GET"])
def check_result():
  result = float(request.args.get("result", 0))
  if result > 80:
    grade = "A"
  elif result > 50 and result < 80:
    grade = "B"
  else:
    grade = "Fail"
  return f"The grade is {grade}"

@app.route("/check-attendance", methods=["GET"])
def check_attendance():
  attendance = float(request.args.get("attendance", 0))
  if attendance < 50:
    result = "low"
  elif attendance < 90:
    result = "moderate"
  else: 
    result = "high"
  return f"Attendance is {result}"

@app.route("/check-rating", methods=["GET"])
def check_rating():
  stars = float(request.args.get("stars", 0))
  if stars < 3:
    result = "low"
  elif stars <= 4:
    result = "moderate"
  else:
    result = 'high'
  return f"Restaurant rating is {result}"

# PY_1.3_HW_2 (if-Else)

@app.route("/check-bmi", methods=["GET"])
def check_bmi():
  height = float(request.args.get("height", 1)) 
  weight = float(request.args.get("weight", 0))
  bmi =  weight / (height * height) 
  if bmi < 18.5:
    result = "under weight"
  elif bmi >= 18.5 and bmi <= 24.9:
    result = "normal weight"
  elif bmi >= 25.0 and bmi <= 29.9:
    result = "over weight"
  else:
    result = "obesity"
  return f"BMI category is {result}"

@app.route("/check-performance", methods=["GET"])
def check_performance():
  grade = float(request.args.get("grade", 0))
  if grade >= 90:
    result = 'excellent'
  elif grade >= 75:
    result = 'good'
  elif grade >= 50:
    result = 'average'
  else:
    result = 'poor'
  return f"Academic performance is {result}"

@app.route("/check-age-group", methods=["GET"])
def check_age_group():
  age = float(request.args.get("age", 0))
  if age <= 12:
    result = 'child'
  elif age <= 17:
    result = 'teenager'
  elif age <= 64:
    result = 'adult'
  else:
    result = 'senior'
  return f"Age group is {result}"

@app.route("/check-loan-eligibility", methods=["GET"])
def check_loan_eligibility():
  creditScore = float(request.args.get("creditScore", 0))
  if creditScore >= 750:
    result = 'high'
  elif creditScore >= 650:
    result = 'medium'
  else:
    result = 'low'
  return f"Loan eligibility is {result}"

@app.route("/check-tax-bracket", methods=["GET"])
def check_tax_bracket():
  income = float(request.args.get("income", 0))
  if income <= 500000:
    result = '10% tax bracket'
  elif income <= 1000000:
    result = '15% tax bracket'
  elif income <= 1500000:
    result = '20% tax bracket'
  else:
    result = '30% tax bracket'
  return f"You fall under the {result}"

@app.route("/check-experiences", methods=["GET"])
def check_experiences():
  yearsOfExperience = float(request.args.get("yearsOfExperience", 0))
  if yearsOfExperience > 5:
    result = "expert"
  else:
    result = "Noob"
  return f"Experience level is {result}"

# PY_1.4_CW (modular functions)

def getWelcomeMessage():
  return "Welcome to the service"

@app.route("/welcome-service", methods=["GET"])
def welcome_service():
  return getWelcomeMessage()

def checkPasswordStrength(password):
  if len(password) >= 15:
    return "Password is strong"
  else:
    return "Password is weak"

@app.route("/check-password", methods=["GET"])
def check_password():
  password = request.args.get("password", "")
  return checkPasswordStrength(password)

def getSum(num1, num2):
  return num1 + num2

@app.route("/sum", methods=["GET"])
def sum():
  num1 = float(request.args.get("num1", 0))
  num2 = float(request.args.get("num2", 0))
  return str(getSum(num1, num2))

def getPersonalizedMessage(age, gender, name):
  return f"Hello, {name}! You are {age} years old {gender}."

@app.route("/personalized-greeting", methods=["GET"])
def personalized_greeting():
  age = int(request.args.get("age", 0))
  gender = request.args.get("gender", "")
  name = request.args.get("name", "")
  return getPersonalizedMessage(age, gender, name)

# PY_1.4_HW_1 (modular functions)

def getWelcomeMessage():
  return f"We will now learn functions!"

@app.route("/welcome", methods=["GET"])
def welcome():
  return getWelcomeMessage()

def getGreetingMessage(username):
  return f"Hey, {username}! Are you ready to learn functions with us?"

@app.route("/greet", methods=["GET"])
def greet():
  username = request.args.get("username", "")
  return getGreetingMessage(username)

def checkYearsOfExp(yearsOfExp):
  if(yearsOfExp > 0):
    return f"You have some experience with functions. Great!"
  else: 
    return f"No worries. You will start writing functions in no time!"

@app.route("/message", methods=["GET"])
def message():
  yearsOfExp = float(request.args.get("yearsOfExp", 0))
  return checkYearsOfExp(yearsOfExp)

def getTime(days, hours):
  return str(hours * days)

@app.route("/hours", methods=["GET"])
def hours():
  days = float(request.args.get("days", 0))
  hours = float(request.args.get("hours", 0))
  return getTime(days, hours)

def getModuleCompletion(username, hasCompleted):
  if hasCompleted:
    return f"{username} has completed the modules"
  else:
    return f"{username} has not completed the modules"

@app.route("/module-completion-status", methods=["GET"])
def module_completion_status():
  username = request.args.get("username", "")
  hasCompleted = request.args.get("hasCompleted", "false") == "true"
  return getModuleCompletion(username, hasCompleted)

def getPersonalizedGreetingEach(city, name):
  return f"Hey, {name}! What's famous about {city}?"

@app.route("/personalized-greetings", methods=["GET"])
def personalized_greetings():
  city = request.args.get("city", "")
  name = request.args.get("name", "")
  return getPersonalizedGreetingEach(city, name)

def findAge(birthyear):
  return str(2024 - birthyear)

@app.route("/find-age", methods=["GET"])
def find_age():
  birthyear = int(request.args.get("birthyear", 0))
  return findAge(birthyear)

def findRequiredTime(days, hours):
  time = days * hours
  if time > 30:
    return f"The time being dedicated is sufficient for learning functions"
  else:
    return f"The time being dedicated is not sufficient for learning functions"

@app.route("/is-time-sufficient", methods=["GET"])
def is_time_sufficient():
  days = float(request.args.get("days", 0))
  hours = float(request.args.get("hours", 0))
  return findRequiredTime(days, hours)

# PY_1.4_HW_2 (modular functions)

def generateProfileUrl(username):
  return f"https://github.com/{username}"

@app.route("/github-profile", methods=["GET"])
def github_profile():
  username = request.args.get("username", "")
  return generateProfileUrl(username)

def generateCertificate(first_name, last_name, course_name):
  return f"This certification is awarded to {first_name} {last_name} for completing the course {course_name}"

@app.route("/certificates", methods=["GET"])
def certificates():
  first_name = request.args.get("firstName", "")
  last_name = request.args.get("lastName", "")
  course_name = request.args.get("courseName", "")
  return generateCertificate(first_name, last_name, course_name)

def calculateGrade(maths, english, science):
  gradeInPercentage = ((maths + english + science) / 300 ) * 100
  return f"Your grade in percentage is {round(gradeInPercentage)}%"

@app.route("/grades", methods=["GET"])
def grades():
  maths = float(request.args.get("maths", 0))
  english = float(request.args.get("english", 0))
  science = float(request.args.get("science", 0))
  return calculateGrade(maths, english, science)

def splitBill(billAmount, numberOfFriends):
  splitAmount = billAmount / numberOfFriends
  return f"Result: Each friend owes Rs. {int(splitAmount)} against the bill"

@app.route("/split-bills", methods=["GET"])
def split_bills():
  billAmount = float(request.args.get("billAmount", 0))
  numberOfFriends = int(request.args.get("numberOfFriends", 1))
  return splitBill(billAmount, numberOfFriends)

def calculateSalary(totalHours, hourlyWage):
  monthlySalary = hourlyWage * totalHours
  return f"Result: Your monthly salary is ₹{int(monthlySalary)}"

@app.route("/monthly-salaries", methods=["GET"])
def monthly_salaries():
  totalHours = float(request.args.get("totalHours", 0))
  hourlyWage = float(request.args.get("hourlyWage", 0))
  return calculateSalary(totalHours, hourlyWage)



if __name__ == "__main__":
  app.run()
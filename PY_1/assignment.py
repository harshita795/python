from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. String Manipulation Utilities

@app.route("/title-length", methods=["GET"])
def title_length():
  title = request.args.get("title", "")
  title_length = len(title)
  return f" Assignment title length: {title_length}"

@app.route("/extract-initials", methods=["GET"])
def extract_initials():
  name = request.args.get("name", "")
  extract_initials = ''.join(word[0].upper() for word in name.split())
  return f"Student initials: {extract_initials}"

@app.route("/create-slug", methods=["GET"])
def create_slug():
  title = request.args.get("title", "")
  create_slug = title.replace(" ", "-").lower()
  return f"Assignment slug: {create_slug}"

# 2. Calculations

@app.route("/calculate-total-marks", methods=["GET"])
def calculate_total_marks():
  marks1 = float(request.args.get("marks1", 0))
  marks2 = float(request.args.get("marks2", 0))
  marks3 = float(request.args.get("marks3", 0))
  total_marks = marks1 + marks2 + marks3
  return f"Total marks: {int(total_marks)}"

@app.route("/calculate-average-marks", methods=["GET"])
def calculate_average_marks():
  marks1 = float(request.args.get("marks1", 0))
  marks2 = float(request.args.get("marks2", 0))
  marks3 = float(request.args.get("marks3", 0))
  average_marks = (marks1 + marks2 + marks3) / 3
  return f"Average marks: {average_marks:.2f}"

@app.route("/calculate-grade", methods=["GET"])
def calculate_grade():
  totalMarks = float(request.args.get("totalMarks", 0))
  if totalMarks >= 90:
    return "Grade A"
  elif 80 <= totalMarks < 90:
    return "Grade B"
  elif 70 <= totalMarks < 80:
    return "Grade C"
  elif 35 <= totalMarks < 70:
    return "Grade D" 
  elif totalMarks < 35:
    return "Grade F"

# 3. Conditional Checks
  
@app.route("/check-pass-fail", methods=["GET"])
def check_pass_fail():
  marks = float(request.args.get("marks", 0))
  if marks >= 40:
    return 'Pass' 
  if marks < 40:
    return 'Fail' 

@app.route("/check-scholarship", methods=["GET"])
def check_scholarship():
  marks = float(request.args.get("marks", 0))
  attendance = float(request.args.get("attendance", 0))
  if marks >= 85 and attendance >= 90:
    return "Eligible for Scholarship"
  else:
    return "Not Eligible for Scholarship"

# 4. Function-Based

def calculatePenalty(daysLate, penaltyPerDay):
  penalty = daysLate * penaltyPerDay
  return f"Total penalty: {penalty}"

@app.route("/calculate-late-penalty", methods=["GET"])
def calculate_late_penalty():
  daysLate = int(request.args.get("daysLate", 0))
  penaltyPerDay = int(request.args.get("penaltyPerDay", 0))
  return calculatePenalty(daysLate, penaltyPerDay)

def calculateStudyHours(dailyHours, totalDays):
  total_hours = dailyHours * totalDays
  return f"Total study hours: {total_hours}"

@app.route("/estimate-study-hours", methods=["GET"])
def estimate_study_hours():
  dailyHours = int(request.args.get("dailyHours", 0))
  totalDays = int(request.args.get("totalDays", 0))
  return calculateStudyHours(dailyHours, totalDays)

topics_data = {
    'AI': ['Machine Learning', 'Neural Networks', 'Natural Language Processing'],
    'Web Development': ['HTML', 'CSS', 'JavaScript', 'React'],
    'Data Science': ['Data Analysis', 'Visualization', 'Pandas', 'NumPy']
}

def recommendTopics(interest):
   return topics_data.get(interest, [])
  
@app.route("/recommend-topics", methods=["GET"])
def recommend_topics():
  interest = request.args.get("interest", "")
  recommended_topics = recommendTopics(interest) 
  if recommended_topics:
    return f"Recommended Topics: {', '.join(recommended_topics)}"
  else:
    return "No topics found."

if __name__ == "__main__":
  app.run()
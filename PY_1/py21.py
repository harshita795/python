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

@app.route("/book", methods=["GET"])
def get_book():
  return jsonify(book)

def getFullTitleAndAuthor(book):
  return f"{book["title"]} by {book["author"]}"

@app.route("/book/fulltitle-author", methods=["GET"])
def get_book_title_and_author():
  fullTitleAndAuthor = getFullTitleAndAuthor(book)
  return jsonify({"fullTitleAndAuthor": fullTitleAndAuthor})

def getGenreAndAvailability(book):
  return {"genre": book["genre"], "isAvailable": book["isAvailable"]}

@app.route("/book/genre-availability", methods=["GET"])
def get_Genre_And_Availability():
  Genre_And_Availability = getGenreAndAvailability(book)
  return jsonify(Genre_And_Availability)

def calculateBookAge(book):
  return str(2024 - book["publicationYear"])


@app.route("/book/age", methods=["GET"])
def calculate_Book_Age():
  book_age = calculateBookAge(book)
  return jsonify({"age": book_age})

def getBookSummary(book):
  return ( 
    f"Title: {book['title']}, "
    f"Author: {book['author']}, "
    f"Genre: {book['genre']}, "
    f"Published: {book['publicationYear']}"
         )

@app.route("/book/summary", methods=["GET"])
def get_Book_Summary():
  book_summary = getBookSummary(book)
  return jsonify({"summary" : book_summary})

def checkStockAndOrder(book):
  if book["stock"] >= 1:
    return {"status": "In Stock", "stock": book["stock"]}
  else:
    return {"status": "Out of Stock", "stock": book["stock"]}
    
@app.route("/book/stock-status", methods=["GET"])
def check_Stock_And_Order():
  stock_and_order = checkStockAndOrder(book)
  return jsonify(stock_and_order)

# PY_2.1_HW_2

githubPublicData = {
	'username': 'ankit123',
	'fullName': 'Ankit Kumar',
	'email': 'ankit@gmail.com',
	'repositories': 24,
	'gists': 12,
	'joinedOn': 'Sep 2018',
}

def getProfileUrl(githubPublicData):
  return f"https://github.com/{githubPublicData['username']}"

@app.route("/github-profile", methods=["GET"])
def get_Profile_Url():
  profile_url = getProfileUrl(githubPublicData)
  return jsonify({"profileUrl": profile_url})

def getPublicEmail(githubPublicData):
  return f"{githubPublicData["email"]}"

@app.route("/github-public-email", methods=["GET"])
def get_Public_Email():
  email = getPublicEmail(githubPublicData)
  return jsonify({"public_email" : email})

def getReposCount(githubPublicData):
  return f"{githubPublicData["repositories"]}"

@app.route("/github-repos-count", methods=["GET"])
def get_Repos_Count():
  repo_count = getReposCount(githubPublicData)
  return jsonify({"reposCount" : repo_count})

def getGistsCount(githubPublicData):
  return f"{githubPublicData["gists"]}"

@app.route("/github-gists-count", methods=["GET"])
def get_Gists_Count():
  gists_count = getGistsCount(githubPublicData)
  return jsonify({"gistsCount" : gists_count})

def getUserBio(githubPublicData):
  return {'fullName': githubPublicData['fullName'], 'joinedOn': githubPublicData['joinedOn'], 'email': githubPublicData['email']}

@app.route("/github-user-bio", methods=["GET"])
def get_User_Bio():
  user_bio = getUserBio(githubPublicData)
  return jsonify(user_bio)

def getRepoUrl(githubPublicData, repoName):
  return f"https://github.com/{githubPublicData['username']}/{repoName}"

@app.route("/github-repo-url", methods=["GET"])
def get_Repo_Url():
  repo_name = request.args.get("repoName", "")
  repo_url = getRepoUrl(githubPublicData, repo_name)
  return jsonify({"repoUrl" : repo_url})

if __name__ == "__main__":
  app.run()
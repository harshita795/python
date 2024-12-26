from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_3.3_CW

products = [
  { 'productId': 1, 'name': 'Laptop', "price": 1000, 'inStock': True },
  { 'productId': 2, 'name': 'Phone', "price": 25, 'inStock': True },
  { 'productId': 3, 'name': 'Tablet', "price":  200, 'inStock': False },
  { 'productId': 4, 'name': 'Keyboard', "price": 50, 'inStock': False }
]

users = [
  {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "role": "admin"},
  {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "role": "editor"},
  {"id": 3, "name": "Charlie Davis", "email": "charlie@example.com", "role": "viewer"},
  {"id": 4, "name": "Diana Evans", "email": "diana@gmail.com", "role": "admin"}
]

posts = [
  {"id": 1, "author": "Alice Johnson", "content": "Exploring the beauty of nature in the countryside."},
  {"id": 2, "author": "Bob Smith", "content": "Tips and tricks for mastering Python programming."},
  {"id": 3, "author": "Charlie Davis", "content": "Thoughts on the latest trends in technology."},
  {"id": 4, "author": "Diana Evans", "content": "Sharing my favorite recipes for quick and healthy meals."}
]

@app.route("/products/filter", methods=["GET"])
def filter_products():
  min_price = float(request.args.get("min_price", 0))
  max_price = float(request.args.get("max_price", float("inf")))

  filtered_products = []
  for product in products:
    if min_price <= product["price"] <= max_price and product["inStock"]:
      filtered_products.append(product)
  return jsonify(filtered_products)

@app.route("/users/find", methods=["GET"])
def find_users():
  role = request.args.get("role")
  email_domain = request.args.get("email_domain")

  matched_users = []
  for user in users:
    if user["role"] == role or user["email"].endswith(f"@{email_domain}"):
      matched_users.append(user)
  return jsonify(matched_users) 

@app.route("/posts/search", methods=["GET"])
def search_post():
  author = request.args.get("author")
  keyword = request.args.get("keyword")

  matched_posts = []
  for post in posts:
    if post["author"] == author or keyword.lower() in post["content"].lower():
      matched_posts.append(post)
  return jsonify(matched_posts)

if __name__ == "__main__":
  app.run()
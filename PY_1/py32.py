from flask import Flask, jsonify, request

app = Flask(__name__)

# PY_3.2_CW

watchList = [
  {
    "videoId": 1,
    "title": "Javascript Tutorial",
    "watched": False,
    "url": "https://youtu.be/shorturl1"
  },
  {
    "videoId": 2,
    "title": "NodeJS Basics",
    "watched": True,
    "url": "https://youtu.be/shorturl2"
  },
  {
    "videoId": 3,
    "title": "RecatJS Guide",
    "watched": False,
    "url": "https://youtu.be/shorturl3"
  }
]

def update_watched_status_by_id(watch_list, video_id, watched):
  for video in watch_list:
    if video["videoId"] == video_id:
      video["watched"] = watched
      break
  return watch_list

@app.route("/watchlist/update-status", methods=["GET"])
def update_watchlist():
  video_id = int(request.args.get("videoId"))
  watched = request.args.get("watched").lower() == "true"
  result = update_watched_status_by_id(watchList, video_id, watched)
  return jsonify(result)

def update_all_videos_watched_status(watch_list, watched):
  for video in watch_list:
    video["watched"] = watched
  return watch_list
      
@app.route("/watchlist/update-all", methods=["GET"])
def update_all_watchlist_status():
  watched = request.args.get("watched").lower() == "true"
  result = update_all_videos_watched_status(watchList, watched)
  return jsonify(result)

def is_unwatched(video):
  return not video["watched"]

@app.route("/watchlist/delete-watched", methods=["GET"])
def delete_watched_videos():
  final_list = list(filter(is_unwatched, watchList))
  return jsonify(final_list)

# PY_3.2_HW_1

library = [
  { 'bookId': 1, 'title': '1984', 'dueDate': '2023-12-01', 'isOverdue': True },
  { 'bookId': 2, 'title': 'Brave New World', 'dueDate': '2024-01-10', 'isOverdue': False },
  { 'bookId': 3, 'title': 'Fahrenheit 451', 'dueDate': '2023-11-15', 'isOverdue': True }
]

bookList = [
  {'bookId': 1, 'title': 'Python Programming', 'author': 'John Doe', 'completed': False, 'url': '<https://shorturl.to/python>', 'isFavorite': False},
  {'bookId': 2, 'title': 'Flask Framework Guide', 'author': 'Jane Smith', 'completed': True, 'url': '<https://shorturl.to/flask>', 'isFavorite': False},
  {'bookId': 3, 'title': 'Machine Learning Basics', 'author': 'Alan Turing', 'completed': False, 'url': '<https://shorturl.to/ml>', 'isFavorite': False}
]

products = [
  { 'productId': 1, 'name': 'Laptop', 'inStock': True },
  { 'productId': 2, 'name': 'Phone', 'inStock': True },
  { 'productId': 3, 'name': 'Tablet', 'inStock': False }
]

def is_not_overdue(book):
  return not book["isOverdue"]

@app.route("/library/remove-overdue", methods=["GET"])
def delete_overdue_book():
  filtered_library = list(filter(is_not_overdue, library))
  return jsonify(filtered_library)

def markBookAsFavorite(book_list, bookId, isFavorite):
  for book in book_list:
    if book["bookId"] == bookId:
      book["isFavorite"] = isFavorite
      break
  return book_list

@app.route("/book/favorite", methods=["GET"])
def update_booklist():
  bookId = int(request.args.get("bookId"))
  isFavorite = request.args.get("isFavorite").lower() == "true"
  result = markBookAsFavorite(bookList, bookId, isFavorite)
  return jsonify(result)

def updateBookStatusById(book_list, bookId, completed):
  for book in book_list:
    if book["bookId"] == bookId:
      book["completed"] = completed
      break
  return book_list

@app.route("/book/update", methods=["GET"])
def update_book_list():
  bookId = int(request.args.get("bookId"))
  completed = request.args.get("completed").lower() == "true"
  result = updateBookStatusById(bookList, bookId, completed)
  return jsonify(result)

def removeCompletedBooks(book):
  return not book["completed"]

@app.route("/books/remove-completed", methods=["GET"])
def delete_completed_book():
  result = list(filter(removeCompletedBooks, bookList))
  return jsonify({'bookList' : result})

products = [
  { "productId": 1, "name": 'Laptop', "inStock": True },
  { "productId": 2, "name": 'Phone', "inStock": True },
  { "productId": 3, "name": 'Tablet', "inStock": False }
]

def removeOutOfStockProducts(product):
  return product["inStock"]

@app.route("/products/remove-out-of-stock", methods=["GET"])
def delete_out_stock_product():
  result = list(filter(removeOutOfStockProducts, products))
  return jsonify(result)

# PY_3.2_HW_2

movies = [
  {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'available': True},
  {'id': 2, 'title': 'Titanic', 'genre': 'Romance', 'available': False},
  {'id': 3, 'title': 'The Dark Knight', 'genre': 'Action', 'available': True},
  {'id': 4, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'available': True},
]

reviews = [
  {'id': 1, 'product_id': 1, 'rating': 4, 'content': 'Great laptop for work.'},
  {'id': 2, 'product_id': 2, 'rating': 5, 'content': 'Excellent sound quality.'},
  {'id': 3, 'product_id': 3, 'rating': 3, 'content': 'Works fine but feels cheap.'},
  {'id': 4, 'product_id': 4, 'rating': 4, 'content': 'Good value for money.'},
]




if __name__ == "__main__":
  app.run()
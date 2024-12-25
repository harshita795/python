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



if __name__ == "__main__":
  app.run()
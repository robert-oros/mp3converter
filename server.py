from flask import Flask, request, jsonify, request, send_file, make_response
from flask import request, redirect, send_from_directory
import sqlite3
import uuid
import os
import youtube_dl


app = Flask(__name__)


@app.route("/ytconverter/js/<path:path>")
def send_js(path):
  return send_from_directory("js", path)

@app.route("/ytconverter/css/<path:path>")
def send_css(path):
  return send_from_directory("css", path)

# @app.route("/", methods=["GET"])
# def home():
#   return render_template("index.html")

@app.route('/audio', methods=['GET'])
def download_mp3():
  url = request.args.get('url')
  print(url)
  

  # mp3_file_name = get_mp3(url)
  
  # #sending file as response
  # resp = make_response(
  #   send_file("./song.mp3", mimetype='audio/wav', as_attachment=True, attachment_filename="audio.mp3"))

  # return resp

# def get_mp3(url):
#   #gets video information from url
#   video_info = youtube_dl.YoutubeDL().extract_info(
#       url, download=False
#   )
#   file_name = "song.mp3"
#   options = {
#     'format': 'bestaudio/best',
#     'keepvideo': False,
#     'outtmpl': file_name,
#     # conversion
#     'postprocessors': [{
#       'key': 'FFmpegExtractAudio',
#       'preferredcodec': 'mp3',
#       'preferredquality': '192',
#     }]
#   }
  
#   #downloads song with above parameters
#   with youtube_dl.YoutubeDL(options) as download:
#     download.download([url])

#   return file_name


# @app.route("/audio/add", methods=["GET","POST"])
# def add():
#   if request.method == "POST":
#     title = request.form.get("title")
#     autor = request.form.get("autor")
#     file = request.files["file"]

#     file_name = uuid.uuid4()
#     filename, file_extension = os.path.splitext(file.filename)
#     full_name = "songs/" + str(file_name) + file_extension
#     file.save(full_name)
  
#     db = create_connection()
#     db.execute(f'''INSERT INTO mp3player(title, autor, filemp3)
#     VALUES("{title}", "{autor}", "{full_name}")''')
#     db.commit()
#     db.close()
#     return redirect("/audio/")
#   return render_template("add.html")

# @app.route("/audio/delete", methods=["GET","DELETE"])
# def delete():
#   id = request.args.get("id")
#   db = create_connection()
#   db.execute("DELETE FROM mp3player WHERE ID = ? ", id)
#   db.commit()
#   db.close()
#   return Response(mimetype='application/json')

# @app.route("/audio/edit", methods=['GET','POST'])
# def edit():
#   if request.method == "POST":
#     title = request.form.get("title")
#     autor = request.form.get("autor")
#     file = request.form.get("file")
#     db = create_connection()
#     db.execute(f'''UPDATE mp3player SET title="{title}", autor="{autor}", filemp3="{file}"''')
#     db.commit()
#     db.close()
#     return redirect("/audio/")
#   id = request.args.get("id")
#   db = create_connection()
#   cursor = db.cursor()
#   cursor = db.execute("SELECT * FROM mp3player WHERE ID=?", id)
#   row = cursor.fetchall()
#   db.close()
#   return render_template("edit.html", row=row[0])


app.run(port=8000, debug=True)
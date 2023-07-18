from flask import Flask, request, jsonify, request, send_file, make_response
from flask import request, redirect, send_from_directory, render_template
import sqlite3
import uuid
import os


app = Flask(__name__)


@app.route("/ytconverter/js/<path:path>")
def send_js(path):
  return send_from_directory("js", path)

@app.route("/ytconverter/css/<path:path>")
def send_css(path):
  return send_from_directory("css", path)

@app.route("/", methods=["GET"])
def home():
  return render_template("index.html")

app.run(port=8000, host='0.0.0.0', debug=False)

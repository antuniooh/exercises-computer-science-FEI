
from ProcessTwo import ProcessTwo

from flask import Flask, request
app = Flask(__name__)

@app.route("/processo2")
def get_incomes():
  process = ProcessTwo()
  return process.get_message(request)
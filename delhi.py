import os
from flask import Flask, request, render_template
app = Flask("Delhi")
@app.route("/")
def home():
        return render_template("home.html")
app.run()
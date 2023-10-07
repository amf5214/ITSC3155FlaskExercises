from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def checkEven(value):
   try:
      value = int(value)
      return f"{value} is even" if value % 2 == 0 else f"{value} is odd"

   except ValueError:
      return "Please enter a valid integer that is greater than 0"

@app.route('/', methods=['GET','POST'])
def hello_world():
   if request.method == 'POST':
      value = request.form["numcheck"]
      return render_template("index.html", respval=checkEven(value))
   else:
      return render_template("index.html")


if __name__ == '__main__':
   app.run(debug=True)
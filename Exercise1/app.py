from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
   now = datetime.now()
   return render_template("index.html", time = f"{now.strftime('%A, %B %d %Y %H:%M:%S')}")

if __name__ == '__main__':
   app.run(debug=True)
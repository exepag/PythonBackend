from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
        return render_template("welcome.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=9804, debug=True)

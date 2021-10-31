from flask import Flask, render_template
from checkerboard import checkerBoard
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/4")
def four():
    return render_template("index2.html")

# @app.route("/<int:x>/<int:y>")
# def checkerBoard(x,y):
#     results= checkerBoard (x,y)
#     return render_template("index3.html",results=results)



if __name__ == "__main__":
    app.run(debug=True)
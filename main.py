from flask import Flask, render_template, request, session, redirect, url_for




HOST_NAME = "0.0.0.0"
HOST_PORT = 8001
app = Flask(__name__, template_folder='templates', static_folder='static')
#app.register_blueprint(Finishing_Schedule)




@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
  app.run(debug=True)
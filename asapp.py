from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def index():
	return 'welcome'

@app.route("/hello")
def hello():
	return render_template("first.html")


if __name__=='__main__':
	app.run(use_reloader=True)
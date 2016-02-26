from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    """Respond with dashboard web page"""
    return render_template("index.html", 'Title')
    # return redirect("./dashboard/index.html", code=302)

@app.route('/problem1')
def problem1():
    return 'problem1 Page'

@app.route('/problem2')
def problem2():
    return 'problem2 Page'

@app.route('/problem3')
def problem3():
    return 'problem3 Page'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()

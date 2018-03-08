from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/users/<username>')
def show_user_profile(username):
    print(username)
    return render_template("success.html")

@app.route('/users/<username>/<id>')
def show_user_profile2(username, id):
    print(username)
    print(id)
    return render_template("success.html")


app.run(debug=True)
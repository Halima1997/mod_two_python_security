from gitlab_main import getUsernames
from flask import Flask, render_template, request, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/users_projectid/<project_id>")
def get_projectid(project_id):
    usernames = ({"usernames": getUsernames(project_id)})
    return usernames



@app.route("/", methods=["GET"])
def get():
    return render_template("form.html")


# @app.route("/", methods=["POST"])
# def post():
#     project_id = request.form.get('project_id')
#     username = usernames(project_id)
#     return render_template("data.html", usernames=username)


app.run(host='localhost', port=5000)

if __name__ == "__main__":
    app.run(debug=True)


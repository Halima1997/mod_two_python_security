from gitlab_main import getUsernames, projectException, getProjectID
from flask import Flask, render_template, request, jsonify
from flask import json
from werkzeug.exceptions import HTTPException
from flask import abort

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error_status=str(e)), 404

@app.route("/users_projectid/<project_id>")
def get_projectid(project_id):

    try:
        usernames = ({"result": getUsernames(project_id)})
        return usernames
    except projectException: 
        abort(404, description="Resource not found")

    return jsonify(resource)
    
#raise 404
@app.route("/users_username/<user_id>")
def get_projectids(user_id):

    try:
        ids = ({"result": getProjectID(user_id)})
        return ids
    except projectException: 
        abort(404, description="Resource not found")

    return jsonify(resource)



@app.route("/", methods=["GET"])
def get():
    return render_template("form.html")



app.run(host='localhost', port=5000)

if __name__ == "__main__":
    app.run(debug=True)


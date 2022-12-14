from flask import Flask, json, request
from be.kudo.service import Service
from be.kudo.schema import GitHubRepoSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
USER_ID = 'cris'


@app.route("/kudos", methods=["GET"])
def index():
    return json_response(Service(USER_ID).find_all_kudos())


@app.route("/kudos", methods=["POST"])
def create():
    github_repo = GitHubRepoSchema().load(json.loads(request.data))

    kudo = Service(USER_ID).create_kudo_for(github_repo)
    return json_response(kudo)


@app.route("/kudos/<int:repo_id>", methods=["GET"])
def show(repo_id):
    kudo = Service(USER_ID).find_kudo(repo_id)

    if kudo:
        return json_response(kudo)
    else:
        return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudos/<int:repo_id>", methods=["PUT"])
def update(repo_id):
    github_repo = GitHubRepoSchema().load(json.loads(request.data))

    kudo_service = Service(USER_ID)
    if kudo_service.update_kudo_with(repo_id, github_repo):
        return json_response(github_repo.data)
    else:
        return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudos/<int:repo_id>", methods=["DELETE"])
def delete(repo_id):
    kudo_service = Service(USER_ID)
    if kudo_service.delete_kudo_for(repo_id):
        return json_response({})
    else:
        return json_response({'error': 'kudo not found'}, 404)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})

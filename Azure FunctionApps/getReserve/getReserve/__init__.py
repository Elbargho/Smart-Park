import json
import logging
import azure.functions as func
import requests

from . import requestDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    password = req.params.get('password')
    if not (username and password):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            password = req_body.get('password')

    if(username and password):
        try:
            res = requests.get(
                f"https://usersignin.azurewebsites.net/api/login?username={username}&password={password}").json()
            if(res["res"] != 'ok'):
                return func.HttpResponse(json.dumps({"res": "unauthorized"}), mimetype="application/json")
            location, reserver, platenumber, timeLeft = requestDB.main(
                username)
            return func.HttpResponse(json.dumps({"res": "ok", "location": location, "reserver": reserver, "platenumber": platenumber, "timeLeft": timeLeft}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&password")

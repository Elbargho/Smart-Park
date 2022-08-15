import json
import logging
import azure.functions as func
import requests

from . import updateDB


def main(req: func.HttpRequest, signalRMessages: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    password = req.params.get('password')
    location = req.params.get('location')
    if not (username and location):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            password = req_body.get('password')
            location = req_body.get('location')

    if(username and password and location):
        res = requests.get(
            f"https://usersignin.azurewebsites.net/api/login?username={username}&password={password}").json()
        if(res["res"] != 'ok'):
            return func.HttpResponse(json.dumps({"res": "unauthorized"}), mimetype="application/json")
        try:
            updateDB.reservePark(signalRMessages, username, location)
            return func.HttpResponse(json.dumps({"res": "ok"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&password=&location=")

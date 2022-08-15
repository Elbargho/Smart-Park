import json
import logging
import azure.functions as func
import requests

from . import updateDB

def main(req: func.HttpRequest, signalRMessages: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    location = req.params.get('location')
    username = req.params.get('username')
    password = req.params.get('password')

    if not (location and username and password):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            location = req_body.get('location')
            username = req_body.get('username')
            password = req_body.get('password')

    if(location and username and password):
        try:
            res = requests.get(
                f"https://usersignin.azurewebsites.net/api/login?username={username}&password={password}").json()
            if(res["res"] != 'ok'):
                return func.HttpResponse(json.dumps({"res": "unauthorized"}), mimetype="application/json")
            bill = updateDB.getCurrPayment(location)
            updateDB.releasePark(signalRMessages, location)
            return func.HttpResponse(json.dumps({"res": "ok", "bill": bill}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("location=&username=&password=")

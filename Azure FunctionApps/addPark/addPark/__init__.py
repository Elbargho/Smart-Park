import json
import logging
import azure.functions as func
import requests

from . import updateDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    password = req.params.get('password')
    location = req.params.get('location')
    price = req.params.get('price')
    start = req.params.get('start')
    end = req.params.get('end')
    if not (username and location and price and start and end):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            password = req_body.get('password')
            location = req_body.get('location')
            price = req_body.get('price')
            start = req_body.get('start')
            end = req_body.get('end')

    if(username and password and location and price and start and end):
        try:
            res = requests.get(f"https://usersignin.azurewebsites.net/api/login?username={username}&password={password}").json()
            if(res["res"] != 'ok'):
                return func.HttpResponse(json.dumps({"res": "unauthorized"}), mimetype="application/json") 
            updateDB.addPark(username, location, int(price), start, end)
            return func.HttpResponse(json.dumps({"res": "ok"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&password=&location=&price=&start=&end=")

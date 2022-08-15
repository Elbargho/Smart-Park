import json
import logging
import azure.functions as func
import requests

from . import updateDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    oldpassword = req.params.get('oldpassword')
    newpassword = req.params.get('newpassword')
    platenumber = req.params.get('platenumber')
    creditcard = req.params.get('creditcard')
    cclast4 = req.params.get('cclast4')
    if not (username and oldpassword and newpassword and platenumber and creditcard and cclast4):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            oldpassword = req_body.get('oldpassword')
            newpassword = req_body.get('newpassword')
            platenumber = req_body.get('platenumber')
            creditcard = req_body.get('creditcard')
            cclast4 = req_body.get('cclast4')

    if(username and oldpassword and newpassword and platenumber and creditcard and cclast4):
        try:
            res = requests.get(
                f"https://usersignin.azurewebsites.net/api/login?username={username}&password={oldpassword}").json()
            if(res["res"] != 'ok'):
                return func.HttpResponse(json.dumps({"res": "unauthorized"}), mimetype="application/json")
            updateDB.updateUser(username, newpassword, creditcard, platenumber, cclast4)
            return func.HttpResponse(json.dumps({"res": "ok"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&oldpassword=&newpassword=&platenumber=&creditcard=&cclast4=")
import json
import logging
import azure.functions as func

from . import updateDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    password = req.params.get('password')
    acctype = req.params.get('acctype')
    platenumber = req.params.get('platenumber')
    creditcard = req.params.get('creditcard')
    cclast4 = req.params.get('cclast4')
    if not (username and password and acctype and platenumber and creditcard and cclast4):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            password = req_body.get('password')
            acctype = req_body.get('acctype')
            platenumber = req_body.get('platenumber')
            creditcard = req_body.get('creditcard')
            cclast4 = req_body.get('cclast4')

    if(username and password and acctype and platenumber and creditcard and cclast4):
        try:
            if(updateDB.checkUsernameNotExist(username)):
                updateDB.addUser(username, password, acctype, platenumber, creditcard, cclast4)
                return func.HttpResponse(json.dumps({"res": "ok"}), mimetype="application/json")
            else:
                return func.HttpResponse(json.dumps({"res": "userExists"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&password=&acctype=&platenumber=&creditcard=&cclast4=")

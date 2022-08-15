import json
import logging
import azure.functions as func

from . import authUser


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
            if(authUser.checkUsernameExist(username)):
                if(authUser.login(username, password)):
                    accDetails = authUser.getAccountDetails(username)
                    return func.HttpResponse(json.dumps({"res": "ok", "accDetails": accDetails}), mimetype="application/json")
                else:
                    return func.HttpResponse(json.dumps({"res": "wrongPassword"}), mimetype="application/json")
            else:
                return func.HttpResponse(json.dumps({"res": "userNotExist"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&password=")

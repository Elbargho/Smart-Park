import json
import logging
import azure.functions as func

from . import updateDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    if not (username):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')

    if(username):
        try:
            curr_payment = updateDB.getCurrPayment(username)
            return func.HttpResponse(json.dumps({"res": "ok", "currentPayment": curr_payment}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=")

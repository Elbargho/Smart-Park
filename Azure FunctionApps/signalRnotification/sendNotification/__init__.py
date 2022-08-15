import json
import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    message = req.params.get('message')
    if not (username and message):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
            message = req.params.get('message')

    if(username and message):
        try:
            # send signalR [message] to [username]
            return func.HttpResponse(json.dumps({"res": "ok"}), mimetype="application/json")
        except:
            return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")
    else:
        return func.HttpResponse("username=&message=")

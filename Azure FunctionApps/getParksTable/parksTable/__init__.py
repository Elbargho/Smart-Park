import json
import logging
import azure.functions as func

from . import updateDB


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        parksTable = updateDB.getParksTable()
        return func.HttpResponse(json.dumps({"res": "ok", "Parks Table": parksTable}), mimetype="application/json")
    except:
        return func.HttpResponse(json.dumps({"res": "internalError"}), mimetype="application/json")

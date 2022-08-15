from azure.data.tables import TableClient
from datetime import datetime
import pytz
import json


def getOwner(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    owner = list(entities)[0]["PartitionKey"]
    return owner


def getTenant(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    tenant = list(entities)[0]["PartitionKey"]
    return tenant


def getCurrPayment(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    request_date = list(entities)[0]["requestdate"]
    request_date = datetime.strptime(request_date, '%Y-%m-%d %H:%M:%S.%f')
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    price = list(entities)[0]["Price"]
    curr_date = datetime.now(pytz.timezone('Israel')).replace(tzinfo=None)
    tdelta = (curr_date - request_date).total_seconds()
    tdelta = tdelta / (60*60)
    return float("{:.2f}".format(tdelta * price))


def markIsFull(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    updated_entity = list(entities)[0]
    updated_entity["isFull"] = False
    table_client.update_entity(updated_entity)


def releasePark(signalRMessages, location):
    markIsFull(location)
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    entity = list(entities)[0]
    payment = getCurrPayment(location)
    tenant = getTenant(location)
    owner = getOwner(location)
    table_client.delete_entity(entity)
    signalRMessages.set(json.dumps({
        'target': "ReleaseNotify",
        'arguments': [payment, tenant, owner]
    }))

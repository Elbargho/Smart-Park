from azure.data.tables import TableClient
from datetime import datetime
import pytz
import json

def markIsFull(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"Location eq '{location}'")
    updated_entity = list(entities)[0]
    updated_entity["isFull"] = True
    table_client.update_entity(updated_entity)

def getUserPlateNumber(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    return list(entities)[0]["platenumber"]

def getOwner(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    owner = list(entities)[0]["PartitionKey"]
    return owner

def reservePark(signalRMessages,username, location):
    markIsFull(location)
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    new_entity = {
        'RowKey': location,        
        'PartitionKey': username,
        'platenumber': getUserPlateNumber(username),
        'requestdate': str(datetime.now(pytz.timezone('Israel')).replace(tzinfo=None))
    }
    table_client.create_entity(entity=new_entity)
    owner = getOwner(location)
    signalRMessages.set(json.dumps({
        'target': "ReserveNotify",
        'arguments': [ username,owner ]
    }))
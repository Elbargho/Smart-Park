from azure.data.tables import TableClient
from datetime import datetime
import pytz


def getPark(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(
        f"PartitionKey eq '{username}'")
    entity = list(entities)
    if(entity != []):
        return entity[0]['RowKey'], entity[0]['End']  # location, end
    return None, None


def getReserver(location):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    entities = table_client.query_entities(
        f"""RowKey eq '{location}'""")
    entity = list(entities)
    if(entity != []):
        # reserver, pn
        return entity[0]['PartitionKey'], entity[0]['platenumber']
    return None, None


def getMinsLeft(end):
    endHour, endMinute = [int(x) for x in end.split(':')]
    currHour = datetime.now(pytz.timezone('Israel')).replace(tzinfo=None).hour
    currMinute = datetime.now(pytz.timezone(
        'Israel')).replace(tzinfo=None).minute
    reserveEnd = (endHour - currHour) * 60 + endMinute - currMinute
    return reserveEnd


def main(username):
    location, end = getPark(username)
    reserver, platenumber = getReserver(location)
    timeLeft = getMinsLeft(end)
    return location, reserver, platenumber, timeLeft

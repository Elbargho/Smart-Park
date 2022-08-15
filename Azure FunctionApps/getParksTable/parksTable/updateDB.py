from azure.data.tables import TableClient
from datetime import datetime
import pytz


def isParkAvailable(start, end, isFull):
    currHour = datetime.now(pytz.timezone('Israel')).replace(tzinfo=None).hour
    start, end = start.split(':')[0], end.split(':')[0]
    if(isFull):
        return False
    if(currHour < int(start)):
        return False
    if(currHour > int(end) - 1):
        return False
    return True


def getParksTable():
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities("")
    return [{"Location": entity["RowKey"], "Price": entity["Price"], "Starting Time": entity["Start"], "Ending Time": entity["End"]} for entity in entities if isParkAvailable(entity["Start"], entity["End"], entity["isFull"])]
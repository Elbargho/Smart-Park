from azure.data.tables import TableClient
from datetime import datetime
import pytz


def getCurrPayment(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Requests")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    entity = list(entities)[0]
    location = entity["RowKey"]
    request_date = entity["requestdate"]
    request_date = datetime.strptime(request_date, '%Y-%m-%d %H:%M:%S.%f')
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    entities = table_client.query_entities(f"RowKey eq '{location}'")
    price = list(entities)[0]["Price"]
    curr_date = datetime.now(pytz.timezone('Israel')).replace(tzinfo=None)
    tdelta = (curr_date - request_date).total_seconds()
    tdelta = tdelta / (60*60)
    return float("{:.2f}".format(tdelta * price))

print(getCurrPayment('baraa'))
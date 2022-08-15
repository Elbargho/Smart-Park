from azure.data.tables import TableClient


def addPark(username, location, price, start, end):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Parks")
    new_entity = {
        'RowKey': location,
        'PartitionKey': username,
        'Price': price,
        'Start': start,
        'End': end,
        'isFull': False
    }
    table_client.create_entity(entity=new_entity)

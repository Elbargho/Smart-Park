from azure.data.tables import TableClient


def login(username, password):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    entity = list(entities)[0]
    return password == entity["Password"]


def checkUsernameExist(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    return len(list(entities)) == 1


def getAccountDetails(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    entity = list(entities)[0]
    del entity["PartitionKey"]
    del entity["Password"]
    del entity["RowKey"]
    return entity

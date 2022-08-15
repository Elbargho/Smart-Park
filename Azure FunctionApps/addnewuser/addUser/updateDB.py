from azure.data.tables import TableClient


def addUser(username, password, acctype, platenumber, creditcard, cclast4):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    new_entity = {
        'RowKey': "101",
        'PartitionKey': username,
        'Password': password,
        'AccountType': acctype,
        'platenumber': platenumber,
        'CreditCard': creditcard,
        'cclast4': cclast4
    }
    table_client.create_entity(entity=new_entity)


def checkUsernameNotExist(username):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    return len(list(entities)) == 0

from azure.data.tables import TableClient


def updateUser(username, password, creditcard, platenumber, cclast4):
    table_client = TableClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=generalstoragetable;AccountKey=85HME4uxdE6PSsdXv6Dv9UibBpbBg2JRqGj3m8AdVsNdGu8wcw+0zcpOsq4LJDHRUVSiyfAAKz3A+AStgkToBQ==;EndpointSuffix=core.windows.net", table_name="Accounts")
    entities = table_client.query_entities(f"PartitionKey eq '{username}'")
    updated_entity = list(entities)[0]
    print(updated_entity)
    updated_entity["Password"] = password
    updated_entity["CreditCard"] = creditcard
    updated_entity["platenumber"] = platenumber
    updated_entity["cclast4"] = cclast4
    table_client.update_entity(updated_entity)

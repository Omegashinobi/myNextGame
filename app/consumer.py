from redis import Redis
import logging

class consumer:    
    def __init__(self) -> None:
        pass

    def consumeData(dataType, data):
        client = Redis(host='db', port=6379, decode_responses=True)
        acceptedDataTypes = ["genres","prespective"]

        logging.debug(data)
        if data:
            if dataType in acceptedDataTypes:
                fetchedData = client.json().get('fields:'+dataType)
                if fetchedData is None: 
                    client.json().set('fields:'+dataType, '$', data)
                else:
                    for x in data["values"]:
                        fetchedData["values"].append(x)
                    client.json().set('fields:'+dataType, '$', fetchedData)
                return "data set..."
            return "invalid dataType"
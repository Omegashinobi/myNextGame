from redis import Redis
import json
import random

class generator:

    r = Redis(host='localhost', port=6379, decode_responses=True)

    def __init__(self) -> None:
        pass

    def generate():
        dataType = ["genres","prespective","objects","characters"]
        client = Redis(host='db', port=6379, decode_responses=True)
        output = {}

        for x in dataType:
            data = client.json().get('fields:'+x)
            if data != None:
                queue = []
                for instance in data["values"]:
                    for _ in range(instance["probability"]):
                        queue.append(instance["name"])
                allowence = random.randrange(1,data["allowence"]+1)
                dataList = []
                for _ in range(allowence):
                    record = queue[random.randrange(0,len(queue))]
                    if record not in dataList:
                        dataList.append(record)
                        output[x] = dataList

        return output
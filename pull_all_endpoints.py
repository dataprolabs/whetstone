import json
from whetstone import Whetstone 
from datetime import datetime


if __name__ == "__main__":
    
    print("Log Started: {}".format(datetime.now()))

    credentials = json.load(open('private/keys.json', 'r'))
    apicall = Whetstone(credentials['instance'], credentials['key'])

    for item in apicall.endpoints.items():
        try:
            endpoint = item[1]
            filename = 'data/' + endpoint.replace('/api/v2/', '') + '.json'
            results = apicall.get_data(endpoint)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(results)
        except:
            print("Failed on: {}".format(item))

    print("Log Ended: {}".format(datetime.now()))

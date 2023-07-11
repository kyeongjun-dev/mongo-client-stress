import os
import pymongo
import time

if __name__ == '__main__':
    MONGO_URL = os.getenv('MONGO_URL', None)
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', None)
    MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', None)
    QUERY_TIME_INTERVAL = os.getenv('QUERY_TIME_INTERVAL', None)
    QUERY = os.getenv('QUERY', '')
    COLLECTION_SIZE = os.getenv('COLLECTION_SIZE', None)
    if MONGO_URL == None:
        print('MONGO_URL is not set')
        exit()

    if MONGO_DB_NAME == None:
        print('MONGO_DB_NAME is not set')
        exit()

    if MONGO_COLLECTION_NAME == None:
        print('MONGO_DB_NAME is not set')
        exit()
    if COLLECTION_SIZE == None:
        print('COLLECTION_SIZE is not set')
        exit()
    else:
        COLLECTION_SIZE = int(COLLECTION_SIZE)
    if QUERY_TIME_INTERVAL == None:
       print('QUERY_TIME_INTERVAL is not set')
       exit()
    else:
        if QUERY_TIME_INTERVAL.isdigit():
            QUERY_TIME_INTERVAL = int(QUERY_TIME_INTERVAL)
        else:
            QUERY_TIME_INTERVAL = float(QUERY_TIME_INTERVAL)

    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]

    while True:
        try:
            result = collection.find({}).explain()
            if result['executionStats']['executionSuccess'] == True:
                print('Query Success', 'reeturn:', result['executionStats']['nReturned'], result['serverInfo']['host'])
                if result['executionStats']['nReturned'] != COLLECTION_SIZE:
                    print(f'retunred not {COLLECTION_SIZE}')
                    print('Query Success', 'reeturn:', result['executionStats']['nReturned'], result['serverInfo']['host'])
                    break
            else:
                print('Query Failed')
                print(result['executionStats'])
                print()
        except Exception as e:
            print(e)
            print()
        time.sleep(QUERY_TIME_INTERVAL)

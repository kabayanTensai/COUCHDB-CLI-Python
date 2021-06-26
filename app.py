import fire
import couchdb
import json
import os
import urllib.request

DB_NAME = "task_list_"


def internet(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


def connect(db_name):
    server = couchdb.Server('http://admin:iniadmin@13.250.43.79:5984/')
    db = server[db_name]
    return db


def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)


def sync(username):
    db = connect(f"task_list_{username}")
    task_list = []
    for doc in db:
        task_list.append(json.loads(json.dumps(db[doc])))
    with open(f"task_list_{username}.json", "w") as outfile:
        json.dump(task_list, outfile, indent=4)


def list_task(username, mode="online"):
    try:
        filename = f"./{DB_NAME}{username}.json"
        if doesFileExists(filename) and mode == 'offline' or not internet():
            print("Serving From Offline Data")
            if not doesFileExists(filename):
                print("No Offline Data & Internet")
                return
            with open(filename) as json_file:
                data = json.load(json_file)
                for p in data:
                    print("===================================")
                    print(
                        f"rev_id: {p['_rev']}\nId: {p['_id']} \nTask : {p['task']} \nTag : {p['tag']} \nStatus: {p['status']}\nCreated: {p['created']}")
                    print("+++++++++++++++++++++++++++++++++++")
        else:
            db = connect(f"task_list_{username}")
            print(f"Task List for {username}")
            for doc in db:
                print("===================================")
                print(
                    f"rev_id: {db[doc]['_rev']}\nId: {doc} \nTask : {db[doc]['task']} \nTag : {db[doc]['tag']} \nStatus: {db[doc]['status']}")
                print("+++++++++++++++++++++++++++++++++++")
            # If there's no offline data will be sync for 1st time
            if not doesFileExists(filename):
                print(f"Synchronize {username} task list")
                sync(username)
    except:
        print("User Not Found")


def update_task(username, data):
    db = connect(f"task_list_{username}")
    filename = f"./{DB_NAME}{username}.json"
    if doesFileExists(filename):
        if not doesFileExists(filename):
            print("No Offline Data & Internet")
            return
        updated_data = ""
        with open(filename) as json_file:
            data_json = json.load(json_file)
            for p in data_json:
                if p['_id'] == data['id']:
                    updated_data = json.loads(json.dumps(p))
            updated_data.update(data)
            print(db.save(updated_data))
            sync(username)


if __name__ == '__main__':
    fire.Fire({
        'list_task': list_task,
        'update_task': update_task,
        'sync': sync
    })

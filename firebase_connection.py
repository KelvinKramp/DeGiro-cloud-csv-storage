import pyrebase
import os
import json

# get configuration settings firebase
config = os.environ.get('config')
# convert configurations string into dictionary
config = json.loads(config)


def store_on_firebase(file_path_local, file_name_cloud):
    try:
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        storage.child(file_name_cloud).put(file_path_local)
        print("file successfully stored on firebase")
    except Exception as e:
        print("Could not store on firebase")
        print(e)

def get_from_firebase(file_name_cloud, file_name_download):
    try:
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        storage.child(file_name_cloud).download(file_name_download)
        print("file successfully downloaded from firebase")
    except Exception as e:
        print("Could not download from firebase")
        print(e)


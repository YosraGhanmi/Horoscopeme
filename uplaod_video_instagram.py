from instagrapi import Client
from instagrapi.types import Usertag, Location
import json
from datetime import datetime


def upload_insta(path, caption):
    f = open("client_config_insta.json")
    data = json.load(f)
    data = data["insta_credentials"][0]
    username = data["username"]
    password = data["password"]

    cl = Client()
    cl.login(username, password)
    print("Succesfully loged in!")
    cl.clip_upload(
        path = path,
        caption = caption,
    )
    print("Reel Uploaded")

#upload_insta("here2.mp4","hi")


import os
from twilio.rest import Client
import requests, json
import pyimgur


#sends text to recipient saying who opened the door with a picture
#parameters: string name, string url (jpeg or png), string recipeint number starting with "+1"
def sendText(name,url,recipient):
  account_sid = ""
  auth_token = ""
  client = Client(account_sid, auth_token)
  print(name + " has unlocked the door")
  message = client.messages.create(
    body = f"{name} has unlocked the door",
    from_="",
    media_url= [url],
    to=recipient
)

#uploads image to imgur then returns the link
#parameters: string filepath and string name
def uploadimg(filepath, name):
    CLIENT_ID = ""
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(filepath, title = name)
    return uploaded_image.link


#test run




import os
import sys
from steam_web_api import Steam
import steamPyConfig as cfg
import time


# how to get a steam key: https://steamcommunity.com/dev/apikey


print("")
print("Type help for help!")
print("Please use Steam User IDs, to get a user ID, do $ data and pass the username after asked")

if cfg.apiKey != "":
  steam = Steam(cfg.apiKey)
else:
  print("Uh Oh! You dont have an API key, open this script and head to line 8 on instructions")
  time.sleep(3.5)
  print("Heading onto Main, however API will not work!")
  time.sleep(2)
  StopIteration

while True:
   try:
    cmd = input("$ ")
    if cmd == cfg.helpcmd:
      print(cfg.help)
      print("")
    
    elif cmd == "data":
     dataQuery = input("Whose Data (SteamName): ")
     if dataQuery:
       print(cfg.apiContact)
       latestData = steam.users.search_user(dataQuery)
       time.sleep(1)
       print(latestData)
       print("")
    elif cmd == "badges":
      idQuery = input("SteamID: ")
      if idQuery:
       print(cfg.apiContact)
       latestData = steam.users.get_user_badges(idQuery)
       print(latestData)
       print("")
    elif cmd == "friends":
      idQuery = input("SteamID: ")
      if idQuery:
        print(cfg.apiContact)
        latestData = steam.users.get_user_friends_list(idQuery)
        print(latestData)
        print("")

   except ValueError:
     print(f"Value error: {Exception}")
   except TimeoutError:
     print(f"Timeout: {Exception}")

#test = steam.users.search_user("untaco")

#print(test)
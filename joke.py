#!/usr/bin/env python3
import sys
import requests
import json
def joke():
    if int(sys.argv[1])==0:
        r = requests.get('https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke')
        j = r.json()
        #remove new lines
        setup = str(j["setup"]).replace("\n", '')
        punchline = str(j["punchline"]).replace("\n", '')
        # print
        print(setup, " : ", punchline)
    elif int(sys.argv[1])==1:
        r = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
        #sometimes it can't parse the json for some reason
        try:
            j = r.json()
            # print and remove new lines
            print(j["joke"].replace("\n", ''))
        except Error:
            #in that case retry.
            print("error:   ", str(Error))
            #joke()

joke()
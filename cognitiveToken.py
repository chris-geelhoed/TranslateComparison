import requests
import pickle
import time

def forceToken():
    Subscription_Key = "YOUR SUBSCRIPTION KEY GOES HERE!"
    url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken" ##endpoint

    #set the sub key in the post header
    headers = { 
        "Ocp-Apim-Subscription-Key": Subscription_Key
    }

    token = requests.post(url, headers=headers).text #get token from API

    #prepare object to pickle
    tokenObj = { 
        "time": time.time(),
        "token": token
    }

    tokenFile = open("tokenObj.pickle", "wb") #pickle our data
    pickle.dump(tokenObj, tokenFile)
    tokenFile.close()

    return token

def getToken():
    try:
        tokenFile = open("tokenObj.pickle", "rb")
        tokenObj = pickle.load(tokenFile)
        tokenFile.close()
        timePassed = abs( time.time() - tokenObj["time"]  )
        ##as long as token is less than 8 minutes old, go ahead and use it
        if timePassed < 8 * 60: 
            return tokenObj["token"]
    except:
        pass
        
    return forceToken() #otherwise make call to API for token


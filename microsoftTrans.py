import sys
import requests
from xml.etree import ElementTree

import cognitiveToken

def translate(**kwargs):
    try: #make sure we have the 'text' and 'to'
        text = kwargs["text"]
        to = kwargs["to"]
    except: #otherwise throw an error and exit without calling the API
        sys.stderr.write("Must provide 'text' and 'to' as kwargs\n")
        return 1

    url = "https://api.microsofttranslator.com/v2/http.svc/Translate"

    values = {
        "appid": "Bearer " + cognitiveToken.getToken(), #need to get a token, these expire every 10 minutes
        "text": text,
        "to": to
    }

    r = requests.get(url, params=values)
    output = ElementTree.fromstring(r.text.encode('utf-8')) #convert xml response to text
    
    return output.text
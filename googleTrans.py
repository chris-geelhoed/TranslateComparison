import sys
import requests

def translate(**kwargs):
    try: #make sure that all necessary query data has been sent
        q = kwargs["q"]
        source = kwargs["source"]
        target = kwargs["target"]
    except: #if it has not all been set throw an error and exit without calling the API
        sys.stderr.write("Must provide 'q', 'source', and 'target' as kwargs")
        return 1

    url = "https://translation.googleapis.com/language/translate/v2"

    values = {
        'key': "PUT YOUR GOOGLE TRANSLATE API KEY HERE",
        'q': q,
        'source': source,
        'target': target
    }

    r = requests.get(url, params=values)
    json = r.json() #get back a json file from google

    return json["data"]["translations"][0]["translatedText"].encode("ascii", "ignore")
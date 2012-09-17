import requests
import json

payload = dict(req_url="http://us.battle.net/wow/en/forum/topic/6522913729",
               req_character="auchindoun/Aonah",
               region="us",
               language="en",
               query_data=[["x", "3051496", "Thenmal", "auchindoun"],
                           ["x", "549335",  "Preaug",  "auchindoun"],
                           ["x", "600538",  "Aset",  "auchindoun"]])
print json.dumps(payload)

r = requests.post("http://cogshanks.org/alt-o-magic/json", data=json.dumps(payload))
print r.json


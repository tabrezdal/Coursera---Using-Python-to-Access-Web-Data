import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:

    address = raw_input("Enter location: ")

    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false','address':address})

    print 'Retrieving',url

    uh =urllib.urlopen(url)
    data = uh.read()
    print 'Retrived',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    placeid = js["results"][0]['place_id']
    print('Place id', placeId)

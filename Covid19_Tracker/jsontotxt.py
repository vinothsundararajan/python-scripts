import json
import urllib.request as request

with request.urlopen('https://api.covid19india.org/state_district_wise.json') as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        for state in data['Tamil Nadu']['districtData']:
            state = [state]
            for districts in state:
                activevalue = data['Tamil Nadu']['districtData'][districts]['active']
                confvalue = data['Tamil Nadu']['districtData'][districts]['confirmed']
                recovrvalue = data['Tamil Nadu']['districtData'][districts]['recovered']
                decevalue = data['Tamil Nadu']['districtData'][districts]['deceased']
                print('{:15}\t district details \tActive:{} \tConfirmed:{} \tRecovered:{} \tDecreased:{}'.format(districts,activevalue,confvalue,recovrvalue,decevalue))
    else:
        print("Api server unable to reach")
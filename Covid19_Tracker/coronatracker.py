import json
import requests
import pandas as pd
from  win10toast import ToastNotifier

toaster = ToastNotifier()
def main():
    covid_India=requests.get('https://api.covid19india.org/state_district_wise.json')
    data_covid=covid_India.json()
    Pudukkottai=data_covid['Tamil Nadu'] ['districtData'] ['Pudukkottai']
    Chennai=data_covid['Tamil Nadu'] ['districtData'] ['Chennai']
    Total=("Chennai: {} Pudukkottai: {}".format(Chennai,Pudukkottai))
    toaster.show_toast(title="Corona Live Status",msg=Total)

if __name__ == "__main__":
    main()    
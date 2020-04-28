import json
import requests
import pandas as pd
from  win10toast import ToastNotifier

toaster = ToastNotifier()
def main():
    covid_India=requests.get('https://api.covid19india.org/state_district_wise.json')
    data_covid=covid_India.json()
    Pudukkottai=data_covid['Tamil Nadu'] ['districtData'] ['Pudukkottai'] ['active']
    TotalPudukkottai=data_covid['Tamil Nadu'] ['districtData'] ['Pudukkottai'] ['confirmed']
    Chennai=data_covid['Tamil Nadu'] ['districtData'] ['Chennai'] ['active']
    TotalChennai=data_covid['Tamil Nadu'] ['districtData'] ['Chennai'] ['confirmed']
    Current_Active=("Chennai Total Case: {} \nChennai Total Case: {}".format(TotalChennai,Chennai))
    Total_Confirmed=("Pudukkottai Total Case: {} \nPudukkottai Active Case: {}".format(TotalPudukkottai,Pudukkottai))
    toaster.show_toast(title="Corona Live Status",msg=("{} \n{}".format(Current_Active,Total_Confirmed)), duration=15,threaded=False)

if __name__ == "__main__":
    main()     
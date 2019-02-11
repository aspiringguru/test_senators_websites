import pandas as pd
import whois
import wget
import os

data = pd.read_csv("allsenel.csv")
print(data.shape)
print(list(data))
selected_data = data[['Surname', 'First Name']]
print(selected_data.shape)
print(selected_data.head())
selected_data['domain_status'] = 'unknown'
selected_data['domain_tested'] = ''


for index, row in selected_data.iterrows():
    print(row['Surname'], row['First Name'])
    temp = "www."+row['First Name']+row['Surname']+".com.au"
    temp = temp.lower()
    print(temp)
    #w = whois.whois(temp)
    #print("creation_date:", w.creation_date)
    #print("expiration_date:", w.expiration_date)
    url = "http://"+temp
    selected_data.at[index,'domain_tested'] = url
    try:
        filename = wget.download(url)
        print (filename)
        os.remove(filename)
        selected_data.at[index,'domain_status'] = "wget_valid"
        print("wget valid for domain:", url)
    except:
        print("Error while deleting file ", filename)
        selected_data.at[index,'domain_status'] = "wget_fail"
        print("wget _INVALID_ for domain:", url)
print(selected_data)
selected_data.to_csv("results.csv", index=False)

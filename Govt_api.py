# State/UTs-Wise Number Of Students Placed Under Pradhan Mantri Kaushal Vikas Yojana (PMKVY) As On 30.06.2022
# here we use govt api....
import urllib.request
import urllib.error
import urllib.parse
import json
import ssl

# Here are ssl certificate........
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Now Work on this....
#state_name = input('Enter States Name: ')
url = 'https://api.data.gov.in/resource/ad9f8ad2-a6a3-48c8-a92a-8979008ba9d5?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=20'
rtri_url = urllib.request.urlopen(url, context=ctx)
read_data = rtri_url.read().decode()
print('Retrieved', len(read_data), 'Characters')

# recive the json type data....
js_data = json.loads(read_data)
#show_data..
print(json.dumps(js_data, indent=4))
state_name_id = js_data['records']
student_plc_no = js_data['records']
for item in state_name_id:
    print('----------')
    print('State Name: ', item['state_ut'])
    print('Number of students were placed: ', item['students_placed'])

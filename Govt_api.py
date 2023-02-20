# State/UTs-Wise Number Of Students Placed Under Pradhan Mantri Kaushal Vikas Yojana (PMKVY) As On 30.06.2022
# here we use govt api....
import urllib.request
import urllib.error
import urllib.parse
import json
import ssl

# Here are ssl certificate.....
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Now Work on this....
while True:
    state_name = input('Enter States Name: ')
    url = 'https://api.data.gov.in/resource/ad9f8ad2-a6a3-48c8-a92a-8979008ba9d5?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=20'
    rtri_url = urllib.request.urlopen(url, context=ctx)
    read_data = rtri_url.read().decode()
    print('Retrieved', len(read_data), 'Characters')

    # recive the json type data....
    js_data = json.loads(read_data)

    # check Their have any data..
    if not js_data or 'status' not in js_data or js_data['status'] != 'ok':
        print('========= FAIL TO RETRIVE DATA =======')
        print(js_data)
        continue
    # For looking good your data..
    # print(json.dumps(js_data, indent=4))

    # Find the state and how many student are placed in states...
    state_name_id = js_data['records'][0]['state_ut']
    student_plc_no = js_data['records'][0]['students_placed']
    # print all information....
    if state_name == state_name_id:
        print('State Name: ', state_name_id)
        print('Number of student were placed: ', student_plc_no)
    else:
        print('worng Name')

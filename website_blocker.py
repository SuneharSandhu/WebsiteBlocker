import time
from datetime import datetime as dt

# this is for testing purposes
# host_temp = 'hosts'

host_path = '/etc/hosts'

# Path for windows
# host_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = '127.0.0.1'
website_list = ['https://www4.gogoanime.io', 'gogoanime.io']

while True:

    # datetime(year, month, day, hour, minute, second, microsecond)

    year = dt.now().year
    month = dt.now().month
    day = dt.now().day

    if dt(year, month, day, 12) < dt.now() < dt(year, month, day, 15):
        print('Blocking...')
        with open(host_path, 'r+') as file:
            content = file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")     # this is the required format for the host file

    # delete the websites
    # from file when not in
    # working hours
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()          # stores content in a list
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Unblocked...')

    time.sleep(5)

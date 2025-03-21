import time
import requests

current_year = time.strftime("%Y")
current_day = time.strftime("%d")
current_month = time.strftime("%M")

time_ranges = {
    "analog": {"start_year": "1953", "end_year": "1999"},
    "digital": {"start_year": "2000", "end_year": f"{current_year}"},
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '215',
    'Origin': 'https://www.tucson.ars.ag.gov',
    'Connection': 'keep-alive',
    'Referer': 'https://www.tucson.ars.ag.gov/dap/digital/event.asp',
    'Cookie': 'ASPSESSIONIDSCFDDCDB=EOLLGDGDENMLKPANMNAKGEML',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=0, i'
}

payload = {
    "hiddenStartYear": "2000",
    "hiddenEndYear": "1999",
    "Watershed": "63",
    "gages": "1",
    "StartMonth": "1",
    "StartDay": "1",
    "StartYear": "2000",
    "EndMonth": "12",
    "EndDay": "31",
    "EndYear": "1999",
    "all": "ON",
    "type": "breakpoint",
    "format": "text",
    "sortby": "sortby_gage",
    "units": "inches",
    "MinDepth": "",
    "MaxDepth": "",
    "MinDuration": "",
    "MaxDuration": "",
    "submit": "Submit",
}

session = requests.Session()

# payload["EndYear"] = "1999"
# analog_url = "https://www.tucson.ars.ag.gov/dap/eventh.asp"
# resp = session.post(analog_url, headers=headers, data=payload)
# for line in resp.text.split("\n"):
#     print(line)

payload["EndMonth"] = current_month
payload["EndDay"] = current_day
payload["EndYear"] = f"{current_year}"
digital_url = "https://www.tucson.ars.ag.gov/dap/digital/eventh.asp"
resp = session.post(digital_url, headers=headers, data=payload)
for line in resp.text.split("\n"):
    print(line)
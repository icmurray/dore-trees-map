from collections import namedtuple
import csv
import re
import requests
import time

Input = namedtuple('Input', 'job location street species reason replacement')
Output = namedtuple('Output', 'job location street lat lon species reason replacement')

URL = "https://maps.googleapis.com/maps/api/geocode/json"
API_KEY = "REDACTED"

def main(f_in, f_out):
    reader = csv.reader(f_in, delimiter=",", quotechar='"')
    writer = csv.writer(f_out, delimiter=",", quotechar='"')
    for row in reader:
        row = Input(*row)
        geo = geocode(row.location, row.street)
        out = Output(*(row[0:3] + geo + row[3:]))
        writer.writerow(out)

def geocode(location, street):
    time.sleep(0.2)   # rate limit
    address = guess_address(location, street)
    response = requests.get(URL, params={'address': address, 'key': API_KEY})
    if response:
        latlon = response.json()['results'][0]['geometry']['location']
        return tuple(map(str, [latlon['lat'], latlon['lng']]))
    else:
        return ("", "")


def guess_address(location, street):
    house_number = clean_house_number(location)
    return ",".join([house_number, street, "Sheffield", "S17"])


def clean_house_number(cell):
    RE = re.compile(r'[0-9]+')
    match = RE.search(cell)
    return match.group(0) if match else cell


if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)

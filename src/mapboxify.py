from collections import namedtuple
import csv
import json

Input = namedtuple('Input', 'job location street lat lon species reason replacement')
Marker = namedtuple('Marker', 'title description latitude longitude')

def main(f_in, f_out):
    reader = csv.reader(f_in, delimiter=",", quotechar='"')
    writer = csv.writer(f_out, delimiter=",", quotechar='"')
    data = [to_marker(row) for row in reader]

    writer.writerow(["title", "description", "latitude", "longitude"])
    for d in data:
        writer.writerow(d)

def to_marker(row):
    m = Input(*row)
    return Marker(
            title=m.location + "," + m.street,
            description="A {} to be replaced with a {} because of {}".format(
                m.species, m.replacement, m.reason),
            latitude=float(m.lat),
            longitude=float(m.lon))

if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)


import csv

def main(f_in, f_out):
    reader = csv.reader(f_in, delimiter=",", quotechar='"')
    writer = csv.writer(f_out, delimiter=",", quotechar='"')
    reader.next()   # skip header
    for row in reader:
        writer.writerow([clean_cell(c) for c in row[1:]])   # cut first column

def clean_cell(cell):
    return cell.replace("\n"," ").replace("  ", " ")

if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)

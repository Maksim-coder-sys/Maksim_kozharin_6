import csv
import sys
with open("bakery.csv", mode="a", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, lineterminator="\r")
    file_writer.writerow([sys.argv[1]])


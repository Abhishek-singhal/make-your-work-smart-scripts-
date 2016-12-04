import csv
import sys
toCSV = [{'letter':'A','frequency':25},
         {'letter':'B','frequency':31},
         {'letter':'C','frequency':12},
         {'letter':'D','frequency':15},
         {'letter':'E','frequency':45},
         {'letter':'F','frequency':17}]
keys = toCSV[0].keys()
with open('names.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)


csv.field_size_limit(sys.maxsize)
csv.writer(open('data.tsv', 'w+'), delimiter="\t").writerows(csv.reader(open('names.csv')))

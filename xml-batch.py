import os, sys
import re
import csv


def create_output_dir():
    output = "output"
    if not os.path.exists(output):
        os.makedirs(output)

def find_in_file(f):
    f = open(f, 'r')
    if f.mode == 'r':
        content = f.read()
        # result = re.findall(r'[A-Za-z]*\s[^\n]*', content)
        result = re.findall(r'Table\s[^\s]*', content)
        # result = re.findall(r'^\\n', content)
        print("Results:")
        print(result)
        print("")
        f.close()

def find_in_file2(f, regexps):
    f = open(f, 'r')
    if f.mode == 'r':
        content = f.read()
        print("Results:")
        for exp in regexps:
            result = re.findall(exp["Find"], content)
            print(result)
            print("")
        f.close()

def read_csv(f):
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            print(col)
        # print(" ".join(row))

def read_csv_as_dict(f):
    reader = csv.DictReader(f, delimiter=',')
    regexps = []
    for line in reader:
        print("Find: " + line["Find"]),
        print("Replace to: " + line["Replace"] + "\n")
        regexps.append({"Find":line["Find"], "Replace":line["Replace"]})
    return regexps

def main(regexps):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    create_output_dir()
    for f in files:
        extension = re.findall(r'[^\.]\.([a-z]*)', f)
        # print(extension[0])
        if extension[0] == 'txt':
            print(f + " file found. Searching in it...")
            # find_in_file(f)
            find_in_file2(f, regexps)

if __name__ == "__main__":
    # main()
    with open('config.csv', 'r') as f:
        # read_csv(f)
        print("Read config file.")
        regexps = read_csv_as_dict(f)
    main(regexps)

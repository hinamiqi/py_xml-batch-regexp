import os, sys
import re
import csv

OUTPUT_DIR = "output/" #куда складываются обработанные файлы
FILES_EXT = "txt" # раширение файлов, в которых нужно произвести замены

def create_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def write_output_file(filename, data):
    output_file = OUTPUT_DIR + filename
    try:
        with open(output_file, 'w') as f:
            f.write(data)
    except Exception as e:
        print('An error occurred while writing an output file:')
        print(e)

#чтение регулярных выражений из csv
def read_csv_as_dict(f):
    try:
        reader = csv.DictReader(f, delimiter=',')
        regexps = []
        for line in reader:
            print("Find: " + line["Find"]),
            print("Replace to: " + line["Replace"] + "\n")
            regexps.append({"Find":line["Find"], "Replace":line["Replace"]})
        return regexps
    except Exception as e:
        print('An error occurred while reading config.csv:')
        print(e)

# 1. Считывает файл с переданным именем в строку
# 2. Выполняет замены с помощью каждого регулярного выражения в списке regexps
# 3. Записывает итоговую строку в файл с помощью write_output_file
def find_and_replace(filename, regexps, log):
    try:
        f = open(filename, 'r')
        log_info = ""
        if f.mode == 'r': # важно открывать файл только для чтения
            # log_info += "# " + filename + "\n"
            r_list = []
            content = f.read()
            expcounter = 1
            for exp in regexps:
                content, N = re.subn(exp["Find"], exp["Replace"], content)
                # log_info += str(expcounter) + ". " + exp["Find"] + " -> " + exp["Replace"] + " | " + str(N) + "\n"
                r_list.append((exp["Find"], exp["Replace"], str(N)))
                expcounter += 1
            f.close()
            print("Done.")
        write_output_file(filename, content)
        # log.put(log_info)
        log.put_table(filename, r_list)
        log.put_html(filename, r_list)
    except FileNotFoundError:
        print("No " + filename + " file found! Aborting.")
    except Exception as e:
        print("An error occurred while reading " + filename + " file. Aborting.")
        print(e)

class LogObj():
    def __init__(self):
        self.data = ""

        self.output_file = OUTPUT_DIR + "log.md"
        self.output_html = OUTPUT_DIR + "log.html"
        self.data_html = ""

    def put(self, data):
        self.data += data
        self.data += "\n"

    def put_table(self, filename, rlist):
        self.data += "# " + filename
        self.data += "\n"
        self.data += "|Find           |Replace        |Total|\n"
        self.data += "|---------------|---------------|-----|\n"
        for item in rlist:
            self.data += "| " + item[0] + " | " + item[1] + " | " + item[2] + " |\n"
        self.data += "\n"

    def put_html(self, filename, rlist):
        self.data_html += "<!DOCTYPE html><html>\n"

        self.data_html += "<head><style>\n"
        self.data_html += "h1 {color: blue; font: bold 30px Arial, serif;}\n"
        self.data_html += "table, th, td {border: 1px solid grey;}\n"
        self.data_html += "th {text-align: left; font: bold 12px Arial, serif;}\n"
        self.data_html += "td {text-align: left; font: 12px Arial, serif;}\n"
        self.data_html += "</style></head>\n"

        self.data_html += "<body>\n"
        self.data_html += "<h1>" + filename + "</h1>\n"
        self.data_html += "\n"
        self.data_html += '<table style="width:50%">\n'
        self.data_html += "<tr>\n"
        self.data_html += "<th>Find</th><th>Replace</th><th>Total</th>"
        self.data_html += "</tr>\n"
        for item in rlist:
            self.data_html += "<tr>\n"
            self.data_html += "<td>" + item[0] + "</td>" + "<td>" + item[1] + "</td>""<td>" + item[2] + "</td>"
            self.data_html += "</tr>\n"
        self.data_html += '</table>\n'
        self.data_html += '</body></html>'

    def write(self):
        try:
            with open(self.output_file, 'w') as f:
                f.write(self.data)
        except Exception as e:
            print('An error occurred while writing a log:')
            print(e)

    def write_html(self):
        try:
            with open(self.output_html, 'w') as f:
                f.write(self.data_html)
        except Exception as e:
            print('An error occurred while writing a log:')
            print(e)


# Поиск в файле
# def find_in_file(filename):
#     f = open(filename, 'r')
#     if f.mode == 'r':
#         content = f.read()
#         # result = re.findall(r'[A-Za-z]*\s[^\n]*', content)
#         result = re.findall(r'Table\s[^\s]*', content)
#         # result = re.findall(r'^\\n', content)
#         print("Results:")
#         print(result)
#         print("")
#         f.close()

# Поиск в файле по всем выражениям в списке regexps
# def find_in_file2(filename, regexps):
#     f = open(filename, 'r')
#     data = ""
#     if f.mode == 'r':
#         content = f.read()
#         print("Results:")
#         for exp in regexps:
#             result = re.findall(exp["Find"], content)
#             print(result)
#             print("")
#             for i in result:
#                 data += i
#         f.close()
#     write_output_file(filename, data)

def main(regexps):
    print("Files processing started.")
    # Смотрит все файлы в каталоге
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #  Создает папку output если ее еще нет
    create_output_dir()
    log = LogObj()
    # Для каждого файла определяет его раширение. Если совпадает с FILES_EXT, передает имя файла и список выражений regexps функуии find_and_replace(f, regexps)
    k = 0 # счетчик файлов с подходящим расширением
    for f in files:
        extension = re.findall(r'[^\.]\.([a-z]*)', f)
        if extension[0] == FILES_EXT:
            print(f + " file found. Processing...")
            find_and_replace(f, regexps, log)
            k += 1
    if k == 0: # если не было найдено файлов с подходящим расширением
        print("No files found (check extension)")
    else:
        log.write()
        log.write_html()
        print("\n")
        print(str(k) + " files processed.")

if __name__ == "__main__":
    # открывает конфиг и считывает из него регулярные выражения в список regexps
    try:
        with open('config.csv', 'r') as f:
            # read_csv(f)
            print("Read config.csv file. Founded RegExps:")
            regexps = read_csv_as_dict(f)
        # функции должен быть передан список регулярных выражений!
        main(regexps)
    except FileNotFoundError:
        print("No config.csv found!")

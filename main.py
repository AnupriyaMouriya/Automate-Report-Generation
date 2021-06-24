import csv


def automate_report_generation():
    values = ['[TC]_PC_NLP_', '[TC]_PC_GM_', '[TC]_PC+AE_TV_', '[TC]_PC+AE_DV_']

    # files should be csv format
    result_file_name = 'result-1.csv'
    result_file_path = r"path\"
    path_of_aggregate_report_name = r"path\"

    result_file = open(r"{0}\{1}".format(result_file_path, result_file_name), "w")

    for val in values:
        with open('{0}'.format(path_of_aggregate_report_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            result_file.writelines('\n' + val + '\n')
            for row in csv_reader:
                if line_count == 0:
                    str2 = '{0},{1},{2},{3},{4},{5}'.format(row[0], row[1], row[7], row[2], row[8], row[4])
                    result_file.writelines(str2 + '\n')
                    line_count += 1
                else:
                    if val in row[0]:
                        row[0] = row[0].replace(val, '')
                        str1 = '{0},{1},{2},{3},{4},{5}'.format(row[0], row[1], row[7], row[2], row[8], row[4])
                        result_file.writelines(str1 + '\n')
                        line_count += 1
            print(f'Processed {line_count} lines for {val}')

    result_file.close()


if __name__ == '__main__':
    automate_report_generation()

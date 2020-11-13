# программа предназначена для переименования файлов с данными

import os
import pandas

def main():
    for filename in os.listdir("C:\\bioinf_test\\data_again\\"):
        df = pandas.read_csv("C:\\bioinf_test\\data_again\\" + filename, sep="\t")
        new_name = df.columns.values[7]
        os.rename("C:\\bioinf_test\\data_again\\" + filename, "C:\\bioinf_test\\data_again\\" + new_name + ".tsv" )

if __name__ == '__main__':
    main()




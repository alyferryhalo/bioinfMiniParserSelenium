# программа предназначена для считывания данных из файлов

import os
import pandas

def main():
    for filename in os.listdir("C:\\bioinf_test\\data_again\\"):
        df = pandas.read_csv("C:\\bioinf_test\\data_again\\" + filename, sep="\t")
        alt_data = df.iloc[: , [7]]
        #print(alt_data)


if __name__ == '__main__':
    main()




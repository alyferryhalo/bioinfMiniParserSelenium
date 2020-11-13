# программа предназначена для скачивания данных с сайта

from selenium import webdriver
import pandas


factors_data = pandas.read_excel("./data_frame.xlsx")
factor_name_list = factors_data['FACTOR_NAME'].tolist()
    
sites = []

# в цикле генерируем адреса страниц, по которым должен будет пройтись парсер
for factor_name in factor_name_list:
    site = "https://adastra.autosome.ru/search/advanced?tf={}".format(factor_name)
    sites.append(site)

# основная функция программы, которая скачивает данные с сайта
def main():
    driver = webdriver.Chrome()
    for site in sites:
        driver.get(site)
        element = driver.find_element_by_xpath('/html/body/app-root/asb-layout/div/div/div/asb-search-page/div/div[1]/asb-search/div/div[2]/div/div/button[2]/span/span[1]')
        element.click()

if __name__ == '__main__':
    main()

import random
import time
import os
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from settings import STORES


def get_products():
    products = []
    with open(os.path.join('resources', 'Listado_Productos.txt')) as file:
        for line in file:
            product = line.split('        ')
            if len(product) == 3:
                products.append(product[1].split('(')[0].strip())
    return products[1:]


def write(filename, upc, product):
    with open(os.path.join('resources', filename), 'a') as file:
        writer = csv.writer(file)
        writer.writerow([upc, product])


def main():
    driver = webdriver.Chrome(os.path.join('resources', 'chromedriver'))

    for store, properties in STORES.items():
        print(f'Buscando productos en {store}...')
        
        for product in get_products():
            print(f'Buscando producto {product}')
            
            driver.get(properties['url'])

            try:              
                ## Buscar en pagina
                search = driver.find_element_by_xpath(properties['search'])
                search.send_keys(product)
                search.send_keys(Keys.ENTER)
                time.sleep(random.uniform(3.0, 6.0))
                
                ## Ir a primer a tarjeta
                card = driver.find_element_by_xpath(properties['card'])
                url = card.find_element_by_xpath('.//a[@href]')
                url = url.get_attribute('href')
                driver.get(url) 
                time.sleep(random.uniform(3.0, 6.0))

                ## Buscar UPC
                upc = driver.find_element_by_xpath(properties['upc']).text
                upc = upc.split(properties['split'])[1]
                
                ## Guardar UPC
                print(f'upc={upc}, nombre={product}\n')
                write(f'upc_{properties["tag"]}.csv', upc, product)
            except Exception as error:
                print('ERROR', error)


if __name__ == '__main__':
    main()
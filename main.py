import math
import requests
from tqdm import tqdm
import csv
import cookies_and_header

msk_file_path = 'csv/RU-MOW.csv'
spb_file_path = 'csv/RU-SPE.csv'
all_file_path = 'csv/all_lego.csv'


def write_row_to_csv(file_path, write_list, wa='a'):
    with open(file_path, wa) as file:
        writer = csv.writer(file)
        writer.writerow(write_list)


def get_data():

    response = requests.get('https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&exclude=items&meta=*&limit=30', cookies=cookies_and_header.cookies, headers=cookies_and_header.headers).json()

    count_of_pages = response.get('meta')['length']
    count_of_pages = math.ceil(count_of_pages / 30)

    offset = 0
    city = 'RU-MOW'
    loop = tqdm(total=count_of_pages, position=0, leave=False)

    for i in range(count_of_pages):
        try:
            loop.set_description('Loading...'.format(i))
            loop.update(1)

            response = requests.get(f'https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:{city}&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset={offset}&sort=popularity:desc', cookies=cookies_and_header.cookies, headers=cookies_and_header.headers).json()

            products_ids = response.get('items')

            for product in products_ids:

                old_price = product.get('old_price')

                if old_price is None:
                    price = product.get('price')['price']
                else:
                    price = old_price['price']
                    old_price = product.get('price')['price']

                csv_list = [product.get('id'), product.get('title'), price, old_price, product.get('link')['web_url']]
                region_iso_codes = product.get('available')['offline']['region_iso_codes'] 

                if 'RU-MOW' and 'RU-SPE' in region_iso_codes:
                    write_row_to_csv(msk_file_path, csv_list)
                    write_row_to_csv(spb_file_path, csv_list)

                elif 'RU-MOW' in region_iso_codes:
                    write_row_to_csv(msk_file_path, csv_list)

                elif 'RU-SPE' in region_iso_codes:
                    write_row_to_csv(spb_file_path, csv_list)

                write_row_to_csv(all_file_path, csv_list)

            offset += 30
        except ConnectionError:
            print(f"error in offset {offset}")

    loop.close()


def create_csv():
    header_list = ('id', 'title', 'price', 'promo_price', 'url')

    write_row_to_csv(msk_file_path, header_list, 'w')
    write_row_to_csv(spb_file_path, header_list, 'w')
    write_row_to_csv(all_file_path, header_list, 'w')


def main():
    create_csv()
    get_data()


if __name__ == '__main__':
    main()

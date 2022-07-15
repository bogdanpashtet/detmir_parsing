import math
import requests
from tqdm import tqdm
import csv


def get_data():
    cookies = {
        'ab2_90': 'ab2_90old90',
        'ab2_33': 'ab2_33new33',
        'ab2_50': '44',
        'ab3_75': 'ab3_75new20',
        'ab3_33': 'ab3_33new17',
        'ab3_20': 'ab3_20_10_1',
        'cc': '0',
        'uid': 'X6NyHmLQP+NzybgJBZqsAg==',
        '_ym_uid': '165781501337422707',
        '_ym_d': '1657815013',
        '_gcl_au': '1.1.291032571.1657815013',
        '_ym_isad': '2',
        '_ga': 'GA1.2.1537964662.1657815017',
        '_gid': 'GA1.2.2004469579.1657815017',
        'geoCityDM': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
        'geoCityDMIso': 'RU-MOW',
        'geoCityDMCode': '',
        'JSESSIONID': '92e58f7b-427b-4f93-9e0a-3c50e23a7694',
        'detmir-cart': '730ff22b-912b-4c84-8f23-9ba924059ce1',
        'auid': 'a1271274-10ef-48a0-9688-9a2c661f399c',
        'srv_id': 'cubic-front17-prod',
        'dm_s': 'L-92e58f7b-427b-4f93-9e0a-3c50e23a7694|kH730ff22b-912b-4c84-8f23-9ba924059ce1|Vja1271274-10ef-48a0-9688-9a2c661f399c|gqcubic-front17-prod|qa1c833135-eb19-4918-ade1-6acd850fbb30|RK1657815016883#8HvI9IE_sgOELLyqe3gUW_SA6ipmBDrs_ZuZoCS1HtY',
        'qrator_msid': '1657828166.960.kwRxsxeCmdN0sCvn-rqfi9vdth8jci4683l5ukpcorn0699ne',
        '_sp_ses.2b21': '*',
        '_ym_visorc': 'w',
        '_sp_id.2b21': '517f83c9-de6f-4321-8336-72ee1f550689.1657815017.4.1657828695.1657825983.f2474d52-4d2d-4efe-8c22-74e8e95a2e47',
    }

    headers = {
        'authority': 'api.detmir.ru',
        'accept': '*/*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7',
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ab2_90=ab2_90old90; ab2_33=ab2_33new33; ab2_50=44; ab3_75=ab3_75new20; ab3_33=ab3_33new17; ab3_20=ab3_20_10_1; cc=0; uid=X6NyHmLQP+NzybgJBZqsAg==; _ym_uid=165781501337422707; _ym_d=1657815013; _gcl_au=1.1.291032571.1657815013; _ym_isad=2; _ga=GA1.2.1537964662.1657815017; _gid=GA1.2.2004469579.1657815017; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMIso=RU-MOW; geoCityDMCode=; JSESSIONID=92e58f7b-427b-4f93-9e0a-3c50e23a7694; detmir-cart=730ff22b-912b-4c84-8f23-9ba924059ce1; auid=a1271274-10ef-48a0-9688-9a2c661f399c; srv_id=cubic-front17-prod; dm_s=L-92e58f7b-427b-4f93-9e0a-3c50e23a7694|kH730ff22b-912b-4c84-8f23-9ba924059ce1|Vja1271274-10ef-48a0-9688-9a2c661f399c|gqcubic-front17-prod|qa1c833135-eb19-4918-ade1-6acd850fbb30|RK1657815016883#8HvI9IE_sgOELLyqe3gUW_SA6ipmBDrs_ZuZoCS1HtY; qrator_msid=1657828166.960.kwRxsxeCmdN0sCvn-rqfi9vdth8jci4683l5ukpcorn0699ne; _sp_ses.2b21=*; _ym_visorc=w; _sp_id.2b21=517f83c9-de6f-4321-8336-72ee1f550689.1657815017.4.1657828695.1657825983.f2474d52-4d2d-4efe-8c22-74e8e95a2e47',
        'if-none-match': 'W/"58349-fOIuiLax6eCem9OaUwL5f++mh+E"',
        'origin': 'https://www.detmir.ru',
        'referer': 'https://www.detmir.ru/',
        'sec-ch-ua': '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 OPR/89.0.4447.38',
        'x-requested-with': 'detmir-ui',
    }

    response = requests.get(
        'https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&exclude=items&meta=*&limit=30',
        cookies=cookies, headers=headers).json()

    count_of_pages = response.get('meta')['length']
    count_of_pages = math.ceil(count_of_pages / 30)

    offset = 0
    city = 'RU-MOW'
    loop = tqdm(total=count_of_pages, position=0, leave=False)

    for i in range(count_of_pages):
        try:
            loop.set_description('Loading...'.format(i))
            loop.update(1)

            response = requests.get(
                f'https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:{city}&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset={offset}&sort=popularity:desc',

                cookies=cookies, headers=headers).json()

            products_ids = response.get('items')

            for person in products_ids:

                old_price = person.get('old_price')

                if old_price is None:
                    price = person.get('price')['price']
                else:
                    price = old_price['price']
                    old_price = person.get('price')['price']

                if 'RU-MOW' and 'RU-SPE' in person.get('available')['offline']['region_iso_codes']:

                    with open('RU-MOW.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [person.get('id'), person.get('title'), price, old_price, person.get('link')['web_url']]
                        )

                    with open('RU-SPE.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [person.get('id'), person.get('title'), price, old_price, person.get('link')['web_url']]
                        )

                elif 'RU-MOW' in person.get('available')['offline']['region_iso_codes']:

                    with open('RU-MOW.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [person.get('id'), person.get('title'), price, old_price, person.get('link')['web_url']]
                        )

                elif 'RU-SPE' in person.get('available')['offline']['region_iso_codes']:

                    with open('RU-SPE.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [person.get('id'), person.get('title'), price, old_price, person.get('link')['web_url']]
                        )

            offset += 30
        except ConnectionError:
            print(f"error in offset {offset}")

    loop.close()


def create_csv():
    with open('RU-MOW.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            ('id', 'title', 'price', 'promo_price', 'url')
        )

    with open('RU-SPE.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            ('id', 'title', 'price', 'promo_price', 'url')
        )


def main():
    create_csv()
    get_data()


if __name__ == '__main__':
    main()

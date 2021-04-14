# Website for test: https://www.upcitemdb.com/api/explorer#!/lookup/get_trial_lookup
# This website translates barcodes into a host of information, including product's name and brand

import requests
import json

if __name__ == '__main__':
    baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
    # To look at PS4 barcode: 711719051275
    # PS5: 711719541028
    parameters = {'upc': '711719051275'}
    response = requests.get(baseUrl, params=parameters)
    # print(response.url)

    content = response.content
    # converts json loads into python dictionary
    info = json.loads(content)
    # print(type(info))
    # print(info)

    item = info['items']
    itemInfo = item[0]
    title = itemInfo['title']
    brand = itemInfo['brand']
    print(title)
    print(brand)

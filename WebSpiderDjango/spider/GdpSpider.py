import requests
import json

resp = requests.get(
    url="https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020101%22%7D%5D&dfwds=%5B%5D&k1=1724768048050&h=1",
    headers={
        'User-Agent': 'Mozilla/5.0'
    }
)
data = resp.json()
codeRegionMapping = {}
gdp_data = data['returndata']['datanodes']
reg_data = data['returndata']['wdnodes'][1]['nodes']
gdps = []
for gdp in gdp_data:
    gdps.append([gdp['data']['data'], gdp['wds'][1]['valuecode'], gdp['wds'][2]['valuecode']])
for reg in reg_data:
    codeRegionMapping[reg['code']] = reg['cname']

result_data = []
for gdp in gdps:
    result_data.append(([gdp[0], codeRegionMapping[gdp[1]], gdp[2]]))
# print(result_data)
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(result_data, f, ensure_ascii=False)

import requests
import json
from typing import Union, List, Dict, Tuple


def get_latest_data() -> List[Dict]:
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
    print(gdps)
    result_data = []
    for gdp in gdps:
        info = {
            "region_name": codeRegionMapping[gdp[1]],
            "year": gdp[2],
            "value": gdp[0],
            'type': "GDP"
        }
        result_data.append(info)
    return result_data


def getNationalData() -> List[Dict]:
    resp = requests.get(
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0201%22%7D%5D&k1=1724861584529&h=1')
    data = resp.json()
    name_code_mapping = {
        "A020102": "国内生产总值",
        "A020101": "国民总收入",
        "A020106": "人均国内生产总值"
    }
    result_data = []
    for _ in data['returndata']['datanodes']:
        if _['wds'][0]['valuecode'] in name_code_mapping.keys():
            __ = {
                "year": _['wds'][1]['valuecode'],
                "value": _['data']['data'],
                "type": name_code_mapping[_['wds'][0]['valuecode']]
            }
            result_data.append(__)
    print(result_data)
    return result_data


if __name__ == '__main__':
    # get_latest_data()
    getNationalData()

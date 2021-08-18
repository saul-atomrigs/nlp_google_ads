from bs4 import BeautifulSoup
import time
import json
from typing import AsyncGenerator
import requests

params = {'suppress_response_codes': True,
          'callback': 'jQuery1124005705702844427485_1629261815444',
          'q': 'NEWS[ne_417_0000726114] | NEWS_SUMMARY[417_0000726114] | JOURNALIST[76236(period)] | NEWS_MAIN[ne_417_0000726114]',
          'isDuplication': False,
          '_': 1629261815445
          }


response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)
print(response.text)
print('*'*50)

# TODO:
oid = '001'
aid = '0012604850'
params = {
    # ,'callback': 'jQuery1124005705702844427485_1629261815444'
    'suppress_response_codes': True, 'q': f'''NEWS[ne_{oid}_{aid}]|NEWS_SUMMARY[{oid}_{aid}]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_{oid}_{aid}]''', 'isDuplication': False, '_': 1629261815445
}
response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)
data = json.loads(response.text)
result = []
for d in data['contents'][0]['reactions']:
    result.append({
        d['reactionType']: d['count']
    })
print(result)
print('*'*50)

# TODO: jungle.co.kr
magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0
for i in range(10):  # 0~9
    params = {
        'magazineOffset': magazineOffset, 'contestOffset': contestOffset, 'exhibitOffset': exhibitOffset, 'galleryOffset': galleryOffset
    }
    response = requests.get(
        "https://www.jungle.co.kr/recent.json", params=params)
    data = json.loads(response.text)
    for d in data['moreList']:
        print(d['title'])
        print(d['targetCode'])
    magazineOffset = data['magazineOffset']  # 0
    contestOffset = data['contestOffset']  # 6
    exhibitOffset = data['exhibitOffset']  # 0
    galleryOffset = data['galleryOffset']  # 0
    time.sleep(1)
# print(data['moreList'])


# TODO: rochetpunch.com
results = []
page = 1
while page < 3:
    response = requests.get(
        'https://www.rocketpunch.com/api/jobs/template?page=' + str(page) + '&q=')
    data = json.loads(response.text)
    bs = BeautifulSoup(data['data']['template'], 'html.parser')
    for company in bs.select(".company.item"):
        result = {
            'name': company.select_one(".company-name strong").text, 'description': company.select_one(".description").text, 'jobs': []
        }
        #name = company.select_one(".company-name strong").text
        #description = company.select_one(".description").text
        for job in company.select(".job-detail > div > a.job-title"):
            result['jobs'].append(job.text)
        results.append(result)
    print(results)
    page += 1

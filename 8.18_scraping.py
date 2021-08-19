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


def getTweet(query):

    headers = {
        'accept': '*/*'
        #,'accept-encoding': 'gzip, deflate, br'
        #,'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
        ,'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        #,'content-type': 'application/json'
        #,'cookie': '_ga=GA1.2.443444804.1615563358; _gid=GA1.2.457209665.1629116764; G_ENABLED_IDPS=google; kdt=Lp98UdnEy0tpxDqvVwU2t9lH6l5zA9HyNnOFHZsA; mbox=session#984bf879573b4efea62ffc86ea0d61bf#1629121941|PC#984bf879573b4efea62ffc86ea0d61bf.32_0#1692366092; dnt=1; lang=en; _sl=1; personalization_id="v1_Q3SpJaz6SfmfYvkjjRLRJA=="; guest_id=v1%3A162934951370851813; undefined; G_AUTHUSER_H=0; gt=1428221493305962497; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D'
        #,'referer': 'https://twitter.com/metaversekorea_'
        #,'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
        #,'sec-ch-ua-mobile': '?0'
        #,'sec-fetch-dest': 'empty'
        #,'sec-fetch-mode': 'cors'
        #,'sec-fetch-site': 'same-origin'
        ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        #,'x-csrf-token': '0834ca21b9f4b7389da8dbe07b299062'
        ,'x-guest-token': '1428221493305962497'
        #,'x-twitter-active-user': 'yes'
        #,'x-twitter-client-language': 'ko'
    }

    variables = {
        "screen_name": query
        ,"withSafetyModeUserFields": True
        ,"withSuperFollowsUserFields": False
    }

    # Dict -> JSON(text)
    # json.dumps(dict)
    # JSON(text) -> Dict
    # json.loads("")

    params = {
        'variables': json.dumps(variables)
    }

    response = requests.get("https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName", headers=headers, params=params)
    data = json.loads(response.text)
    rest_id = data['data']['user']['result']['rest_id']


    # variables = {
    #     "userId": rest_id,
    #     "count": 20,
    #     "withTweetQuoteCount": True,
    #     "includePromotedContent": True,
    #     "withSuperFollowsUserFields": False,
    #     "withUserResults":True,
    #     "withBirdwatchPivots": False,
    #     "withReactionsMetadata": False,
    #     "withReactionsPerspective": False,
    #     "withSuperFollowsTweetFields": False,
    #     "withVoice": True
    # }

    # params = {
    #     'variables': json.dumps(variables)
    # }


    # response2 = requests.get("https://twitter.com/i/api/graphql/PIt4K9PnUM5DP9KW_rAr0Q/UserTweets", params=params, headers=headers)
    # tweet_data = json.loads(response2.text)

    # # get tweeet
    # for tweet in tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:

    #     try:
    #         print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
    #     except:
    #         pass

    # cursor = tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']

    cursor = ''

    for i in range(5):
        #두번째
        variables = {
            "userId": rest_id,
            "count": 20,
            "withTweetQuoteCount": True,
            "includePromotedContent":True,
            "withSuperFollowsUserFields": False,
            "withUserResults":True,
            "withBirdwatchPivots":False,
            "withReactionsMetadata":False,
            "withReactionsPerspective":False,
            "withSuperFollowsTweetFields":False,
            "withVoice":True
        }

        if cursor != '':
            variables["cursor"] = cursor

        params = {
            'variables': json.dumps(variables)
        }


        response2 = requests.get("https://twitter.com/i/api/graphql/PIt4K9PnUM5DP9KW_rAr0Q/UserTweets", params=params, headers=headers)
        tweet_data = json.loads(response2.text)

        # get tweeet
        for tweet in tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:

            try:
                print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            except:
                pass

        cursor = tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']
        # print(cursor)


getTweet("dondaeji")

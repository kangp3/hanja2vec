#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import json

import requests

processed = set()
with open('radicals.txt') as f:
    for line in f:
        processed.add(line.split('=')[0])

with open('hanja.json') as f:
    hanmun_dict = json.load(f)

with open('radicals.txt', 'a') as f:
    for key in hanmun_dict.keys():
        if key in processed:
            print(f"Skipping {key}")
            continue

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
                #'Accept': 'application/json, text/javascript, */*; q=0.01',
                #'Accept-Language': 'en-US,en;q=0.5',
                #'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://hanja.dict.naver.com/',
                #'Alldict-Locale': 'ko',
                #'X-Requested-With': 'XMLHttpRequest',
                #'Connection': 'keep-alive',
                #'Cookie': 'NNB=IMG7OBZ65UIGM; JSESSIONID=736EF2C0141F90244B7AD61091ECE5A8',
                #'Sec-Fetch-Dest': 'empty',
                #'Sec-Fetch-Mode': 'cors',
                #'Sec-Fetch-Site': 'same-origin',
                #'TE': 'trailers',
            }
            resp = requests.get(f'https://hanja.dict.naver.com/api3/ccko/search?query={key}&m=pc&range=entrySearch', headers=headers)
            entry_id = resp.json()['searchResultMap']['searchResultListMap']['LETTER']['items'][0]['entryId']

            headers = {
                #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
                #'Accept': 'text/html, */*; q=0.01',
                #'Accept-Language': 'en-US,en;q=0.5',
                #'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://hanja.dict.naver.com/',
                #'Alldict-Locale': 'ko',
                #'X-Requested-With': 'XMLHttpRequest',
                #'Connection': 'keep-alive',
                #'Cookie': 'NNB=IMG7OBZ65UIGM; JSESSIONID=736EF2C0141F90244B7AD61091ECE5A8',
                #'Sec-Fetch-Dest': 'empty',
                #'Sec-Fetch-Mode': 'cors',
                #'Sec-Fetch-Site': 'same-origin',
                #'TE': 'trailers',
            }
            resp = requests.get(f'https://hanja.dict.naver.com/api/platform/ccko/entry?entryId={entry_id}&isConjsShowTTS=true&searchResult=false', headers=headers)
            radicals = resp.json()['entry']['members'][0]['show_entry_composition']
            f.write(f"{key}={radicals}\n")
            f.flush()
        except Exception as e:
            print(f"Error processing {key}: {e}")

'''
curl 'https://hanja.dict.naver.com/api3/ccko/search?query=%E8%BC%9D&m=pc&range=entrySearch'
    --compressed
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
    -H 'Accept: application/json, text/javascript, */*; q=0.01'
    -H 'Accept-Language: en-US,en;q=0.5'
    -H 'Accept-Encoding: gzip, deflate, br'
    -H 'Referer: https://hanja.dict.naver.com/'
    -H 'Alldict-Locale: ko'
    -H 'X-Requested-With: XMLHttpRequest'
    -H 'Connection: keep-alive'
    -H 'Cookie: NNB=IMG7OBZ65UIGM; JSESSIONID=736EF2C0141F90244B7AD61091ECE5A8'
    -H 'Sec-Fetch-Dest: empty'
    -H 'Sec-Fetch-Mode: cors'
    -H 'Sec-Fetch-Site: same-origin'
    -H 'TE: trailers'
'''


'''
curl 'https://hanja.dict.naver.com/api/platform/ccko/entry?entryId=9cf3ed45f66d44aabd3e2385c7e23500&isConjsShowTTS=true&searchResult=false&hid=171246753815947970'
    --compressed
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
    -H 'Accept: text/html, */*; q=0.01'
    -H 'Accept-Language: en-US,en;q=0.5'
    -H 'Accept-Encoding: gzip, deflate, br'
    -H 'Referer: https://hanja.dict.naver.com/'
    -H 'Alldict-Locale: ko'
    -H 'X-Requested-With: XMLHttpRequest'
    -H 'Connection: keep-alive'
    -H 'Cookie: NNB=IMG7OBZ65UIGM; JSESSIONID=736EF2C0141F90244B7AD61091ECE5A8'
    -H 'Sec-Fetch-Dest: empty'
    -H 'Sec-Fetch-Mode: cors'
    -H 'Sec-Fetch-Site: same-origin'
    -H 'TE: trailers'
'''

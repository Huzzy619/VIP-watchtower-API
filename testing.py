import requests
import random
import json
from pprint import pprint

# url = "https://instagram47.p.rapidapi.com/web_profile_info"

# querystring = {"username":"huzzy_on_fire"}

# headers = {
# 	"X-RapidAPI-Key": "3df2045bdfmsh20b4d1aa0fb1d60p131f60jsn94f1ab70e4f8",
# 	"X-RapidAPI-Host": "instagram47.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

usernames = ["jio", "shakira", "beyonce", "katyperry"]
proxy = "http://username:password@PROXY_SERVER:PORT"
output = {}


def get_headers(username):
    headers = {
        "authority": "www.instagram.com",
        "method": "GET",
        "path": "/{0}/".format(username),
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "user-agent": random.choice([

            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.169 Safari/537.36",


        ])
    }
    return headers


def main():
    for username in usernames:
        url = f"https://instagram.com{username}/__a=1&__d=dis"

        response = requests.get(url, headers=get_headers(
            username), proxies={"http": proxy, "https": proxy})

        if response.status_code == 200:
            try:
                resp_json = json.loads(response.text)
            except:
                print("Failed. Response was not json")
                continue
            else:
                user_data = resp_json['graphql']['user']
                parse_data(username, user_data)
        elif response.status_code == 301 or response.status_code == 302:
            print("Failed. Redirected to login")
        else:
            print("Request failed. Status: " + str(response.status_code))


def parse_data(username, user_data):
    captions = []
    if len(user_data['edge_owner_to_timeline_media']['edges']) > 0:
        for node in user_data['edge_owner_to_timeline_media']['edges']:
            if len(node['node']['edge_media_to_caption']['edges']) > 0:
                if caption := node['node']['edge_media_to_caption']['edges'][0]['node']['text']:

                    captions.append(caption)
    
    output[username] = {
        'name': user_data['full_name'],
        'category': user_data['category_name'],
        'followers': user_data['edge_followed_by']['count'],
        'posts': captions
    }

if __name__ == '__main__':
    main()
    pprint(output)
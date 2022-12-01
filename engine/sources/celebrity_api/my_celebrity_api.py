from decouple import config
import requests
from .occupation_json import occupation_categories

headers = {"X-Api-Key": config("NINJA_API")}
base_url = "https://api.api-ninjas.com/v1/celebrity?name="


class MyCelebrityAPI:

    def process(self, search_query, *args, **kwargs):

        response = requests.get(
            url=base_url+search_query['name'], headers=headers)
        
        

        result = response.json()

        new_dict = dict()

        new_list = list()

        for item in result:

            new_dict['name'] = item['name']
            new_dict['age'] = item.get('age', None)
            new_dict['gender'] = item.get('gender', None)
            new_dict['occupation'] = item.get('occupation', [])
            new_dict['vip_score'] = 10  # initial vip score
            new_dict['networth'] = item.get('net_worth', 1)

            new_list.append(new_dict.copy())

        return self.vip_score(new_list)
        # return []

    def vip_score(self, filtered_list):
        """Calculates the VIP score
        It using the occupation of the celebrity to calculate the vip score

        Args:
            filtered_list (List): the list of filtered result

        Return:
            List of VIPs with their VIP scores.

        """

        for celeb in filtered_list:
            if celeb['occupation']:
                # occupation present

                celeb_occ_scores = [0]

                for occupation in celeb['occupation']:
                    for category in occupation_categories:
                        if occupation in occupation_categories[category]['occupations']:
                            celeb_occ_scores.append(
                                occupation_categories[category]['popularity_score'])

                celeb['vip_score'] = max(celeb_occ_scores)

        return filtered_list

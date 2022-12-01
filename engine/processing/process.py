import asyncio
from engine.data.dataclass import DataClass
from engine.sources.forbes_scraper.forbes import ForbesVip
from engine.sources.sports_source.services import SearchService
from engine.sources.wikipedia.scrape import Wiki_Source
from engine.sources.celebrity_api.my_celebrity_api import MyCelebrityAPI
from engine.sources.twitter.twitter import TwitterAPI


class Process():
    """
    This Class Process the user input which can either be a dict  or a list

    Main Method: main()

    Args
        search_info (list) || (dict): VIP (celebrity) name to lookup.

    Return 
        List of List  || List of Dictionaries

    """

    def __init__(self, search_info):
        self.search_info = search_info

    async def search_vip(self):
        """
        Main method 
        """
        
        try:
            if type(self.search_info) == list:
                response = []
                for info in self.search_info:
                    service_response = await self.get_service_response(info)
                    data_response = DataClass(service_response, **info)
                    result = data_response.initiate()
                    response.append(result)
            else:
                # print('search info is '+self.search_info)
                service_response = await self.get_service_response(self.search_info)
                # print('results from service classes' + service_response)
                data_response = DataClass(service_response, **self.search_info)
                response = data_response.initiate()
                # print('result from data class', + response)

            return response
        except Exception as e:
            print(f"There was an error somewhere in the process class {e}")
            raise Exception

    async def runService(self, Service, info):
        response = Service().process(info)
        return response

    async def get_service_response(self, info):
        service1, service2, service3, service4 = await asyncio.gather(
            self.runService(ForbesVip, info), 
            self.runService(MyCelebrityAPI, info), 
            self.runService(SearchService, info),
            # self.runService(Wiki_Source, info),
            self.runService(TwitterAPI, info)
        )
        return [service1, service2, service3, service4]

    async def get_service_response2(self, info):
        return await self.runService(ForbesVip, info)


# process = Process()

# result = asyncio.run(process.search_vip())


# print(result)
import asyncio

from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from engine.processing.process import Process

from .models import VIP, History
from .serializers import HistorySerializer, VIPSerializer

# Create your views here.

# Send search parameters
# Check database if result is already there
# if true return result
# else
# process search with engine
# store in history model either ways
# if results, store in VIP model
# else return detail not found

# @sync_to_async


class Search (APIView):

    def get(self, request):

        return Response('ok')

    def post(self, request):
        search_query = request.data
        name = search_query.get('name', None)
        age = search_query.get('age', None)
        gender = search_query.get('gender', None)


        if name == '':

            return Response('name is required', status=status.HTTP_400_BAD_REQUEST)

        data = dict(request.data)

        try:
            #in case forms are sent
            params = {key: value[0] if isinstance(value, list) else value for key, value in data.items()}
        except:
            #in case of raw JSON sent
            params = data

        results = asyncio.run(Process(params).search_vip())


        # Check database if result is already there



        # if age is not None:
        #     filter = VIP.objects.filter(name__icontains=name, age=age)

        # elif gender is not None:
        #     filter = VIP.objects.filter(name__icontains=name, gender=gender)

        # elif age is not None and gender is not None:
        #     filter = VIP.objects.filter(
        #         name__icontains=name, age=age, gender=gender)

        # else:
        #     filter = VIP.objects.filter(name__icontains=name)

        # if filter:
        #     serializer = VIPSerializer(filter, many=True)
        #     return Response(serializer.data, status=status.HTTP_200_OK)

        # else:
        #     data = dict(request.data)
        #     params = {key: value[0] for key, value in data.items()}

        #     results = asyncio.run(Process(params).search_vip())

            # if results:
            #     vips = [VIP(
            #         name=item['name'],
            #         age=item['age'],
            #         gender=item['gender'],
            #         occupation=item['occupation'],

            #     )for item in results]

            #     VIP.objects.bulk_create(vips)
            #     print('saved')

        return Response(results, status=status.HTTP_200_OK)


@api_view()
def get_user_history(request):
    mine = History.objects.filter(user_id=1).order_by('-timestamp')

    serializer = HistorySerializer(instance=mine, many=True)

    return Response(serializer.data)


@sync_to_async
@api_view()
def search_vip(request, name):

    result = asyncio.run(Process({'name': name}).search_vip())

    return Response(result)

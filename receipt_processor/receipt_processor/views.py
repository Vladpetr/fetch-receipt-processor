from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import uuid
import datetime
import math


receipts = {}
class ProcessReceiptApiView(APIView):
    def post(self, request):
        serializer = ReceiptSerializer(data=request.data)
        # ensure not only data format but also values (year, month, day) are valid
        if serializer.is_valid():
            try:
                split_date = request.data["purchaseDate"].split("-")
                year, month, day = int(split_date[0]), int(split_date[1]), int(split_date[2])
                date_valid = datetime.datetime(year, month, day)
            except ValueError:
                return Response("The receipt is invalid", status=status.HTTP_400_BAD_REQUEST)
            # generate a unique ID for the receipt
            receipt_id = str(uuid.uuid4())
            # calculate the number of awarded points
            points = self.calculate_points(request.data)
            # store points in a dictionary
            receipts[receipt_id] = points
            response_data = {"id": receipt_id}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response("The receipt is invalid", status=status.HTTP_400_BAD_REQUEST)
        
    def calculate_points(self, data):
        points = 0
        # one point for every alphanumeric character in the retailer name
        for ch in data["retailer"]:
            if ch.isalnum():
                points += 1
        # 50 points if the total is a round dollar amount with no cents
        if float(data["total"]).is_integer():
            points += 50
        # 25 points if the total is a multiple of 0.25
        if float(data["total"]) % 0.25 == float("0"):
            points += 25
        # 5 points for every two items on the receipt
        pairs = len(data["items"]) // 2
        points += (pairs * 5)
        # if the trimmed length of the item description is a multiple of 3, 
        # multiply the price by 0.2 and round up to the nearest integer
        for item in data["items"]:
            if len(item["shortDescription"].strip()) % 3 == 0:
                points += math.ceil(float(item["price"]) * 0.2)
        # 6 points if the day in the purchase date is odd
        if int(data["purchaseDate"].split("-")[2]) % 2 != 0:
            points += 6
        # 10 points if the time of purchase is after 2:00pm and before 4:00pm
        split_time = data["purchaseTime"].split(":")
        hour, minute = int(split_time[0]), int(split_time[1])
        if hour == 14:
            if minute > 0:
                points += 10
        elif hour == 15:
            points += 10
            
        return points


class PointsByIdApiView(APIView):
    def get(self, request, id):
        if id:
            try:
                points = receipts[id]
                response_data = {"points": points}
                return Response(response_data, status=status.HTTP_200_OK)
            except KeyError:
                return Response("No receipt found for that id", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No receipt found for that id", status=status.HTTP_400_BAD_REQUEST)


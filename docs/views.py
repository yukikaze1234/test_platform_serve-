
import redis
from allpairspy import AllPairs
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .RedisPublic import HandleRedis

# Create your views here.
#处理正交用例设计的请求
class OrthogonalApi(APIView):

    def get(self,request):
        return Response(data={"方法不对":"使用post"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self,request):
        tempList=[]
        resValue=[]
        resKey=[]
        for i in request.data:
            for key in i:
                if key == 'key':
                    resKey.append(i[key])
                if key == 'value':
                    tempList.append(i[key].strip().split('/'))
        try:
            for i in AllPairs(tempList):
                resValue.append(dict(zip(resKey,i)))
            data = {
                "res": resValue
            }
        except ValueError:
            data ={
                "res":"因素不能是1个"
            }

        return Response(data=data,status=status.HTTP_200_OK)


#处理Redis相关的请求
class RedisApi(APIView):

    def get(self,request):
        return Response(data={"方法不对":"使用post"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self,request):
        data = request.data
        host = data['Ip']
        port = data['Port']
        password = data['password']
        decode_responses = True
        db = data['db']
        conn = HandleRedis.HandleRedis(host,port,db,decode_responses,password).getConnect()
        if isinstance(conn,redis.StrictRedis):
            return Response(data={"signal":True}, status=status.HTTP_200_OK)
        else:
            return Response(data={"signal":False}, status=status.HTTP_200_OK)
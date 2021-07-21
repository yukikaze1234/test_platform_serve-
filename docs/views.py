import random
from time import sleep

import redis
from allpairspy import AllPairs
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .RedisPublic import HandleRedis
from ps.batchRegister import BatchRegister


# Create your views here.
# 处理正交用例设计的请求
class OrthogonalApi(APIView):

    def get(self, request):
        return Response(data={"方法不对": "使用post"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        tempList = []
        resValue = []
        resKey = []
        for i in request.data:
            for key in i:
                if key == 'key':
                    resKey.append(i[key])
                if key == 'value':
                    tempList.append(i[key].strip().split('/'))
        try:
            for i in AllPairs(tempList):
                resValue.append(dict(zip(resKey, i)))
            data = {
                "res": resValue
            }
        except ValueError:
            data = {
                "res": "因素不能是1个"
            }

        return Response(data=data, status=status.HTTP_200_OK)


# 处理Redis相关的请求
class RedisApi(APIView):

    def get(self, request):
        return Response(data={"方法不对": "使用post"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        data = request.data
        host = data['Ip']
        port = data['Port']
        password = data['password']
        decode_responses = True
        db = data['db']
        conn = HandleRedis.HandleRedis(host, port, db, decode_responses, password).getConnect()
        if isinstance(conn, redis.StrictRedis):
            return Response(data={"signal": True}, status=status.HTTP_200_OK)
        else:
            return Response(data={"signal": False}, status=status.HTTP_200_OK)


# 处理批量注册相关的请求
class batchRegister(APIView):

    def get(self, request):
        return Response(data={"方法不对": "使用post"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def post(self, request):
        data = request.data
        sType = data[0]
        teacherTel = data[1]
        beginTel = data[2]
        endTel = data[3]
        n1 = ['赵', '钱', '孙', '李', '胡', '周', '吴', '魏', '王', '樊', '孙', '邱', '仇']
        n2 = ['小', '中', '大', '一', '二', '三', '四', '五', '六', '七', '九']
        n3 = ['国', '芳', '花', '华', '祯', '东', '我', '杰', '瑶', '光', '毅']
        beginTel = int(beginTel)
        endTel = int(endTel)
        if sType == '小学学生':
            for i in range(beginTel, endTel+1):
                username = random.choice(n1) + random.choice(n2) + random.choice(n3)
                test = BatchRegister()
                test.register(teacherTel=teacherTel, username=username, parentTel=i)
            return Response(data={"批量注册成功"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"目前不支持中学学生的批量注册"}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def executeRedis(request):
    if request.method == 'GET':
        return Response(data={"方法不对": "使用post"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    elif request.method == 'POST':
        data = request.data
        host = data['Ip']
        port = data['Port']
        password = data['password']
        decode_responses = True
        db = data['db']
        rvalue = data['rvalue']
        inputkey = data['inputkey']
        inputvalue = data['inputvalue']
        othervalue = data['othervalue']
        conn = HandleRedis.HandleRedis(host, port, db, decode_responses, password).getConnect()
        if isinstance(conn, redis.StrictRedis):
            if rvalue == 'set':
               result = conn.set(inputkey,inputvalue)
               return Response(data={"msg": result}, status=status.HTTP_200_OK)
            elif rvalue == 'get':
               result = conn.get(inputkey)
               return Response(data={"msg": result}, status=status.HTTP_200_OK)
            elif rvalue == 'del':
               result = conn.delete(inputkey)
               return Response(data={"msg": result}, status=status.HTTP_200_OK)
        else:
            return Response(data={"msg": "建立连接失败，请检查redis连接信息"}, status=status.HTTP_200_OK)

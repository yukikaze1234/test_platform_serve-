from allpairspy import AllPairs
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


#处理正交用例设计的请求
class HandleOrthogonal(APIView):

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
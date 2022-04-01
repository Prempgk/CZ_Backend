"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import *
from .serializers import *

# Create your views here.
@csrf_exempt

def staffprofileApi(request,id=0):
    if request.method == 'GET':
        ref_prof = staff_profile.objects.all()
        prof_serializer = staff_profile_serializer(ref_prof, many=True)
        return JsonResponse(prof_serializer.data, safe=False)
    elif request.method == 'POST':
        prof_data = JSONParser().parse(request)
        prof_serializer = staff_profile_serializer(data=prof_data)
        print(prof_data)
        if prof_serializer.is_valid():
            prof_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        prof_data = JSONParser().parse(request)
        profile_data = staff_profile.objects.get(staff_id=prof_data['staff_id'])
        prof_serializer = staff_profile_serializer(profile_data, data=prof_data)
        if prof_serializer.is_valid():
            prof_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to update')
    elif request.method == 'DELETE':
        prof_data = staff_profile.objects.get(id=id)
        prof_data.delete()
        return JsonResponse("Deleted Successfully", safe=False)
"""

from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from.models import staff_profile,staff_experience,staff_qualification
from.serializers import staff_profile_serializer,staff_exp_serializer,staff_qual_serializer


class staffprofileviewset(GenericViewSet):
    serializer_class = staff_profile_serializer
    queryset = staff_profile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        data = staff_profile.objects.get(pk=pk)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self,request,pk=None):
        putdata = request.data
        details = staff_profile.objects.get(pk=pk)
        serializer = staff_profile_serializer(details,data=putdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        data = staff_profile.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class staffqualviewset(GenericViewSet):
    queryset = staff_qualification.objects.all()
    serializer_class = staff_qual_serializer

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            a = request.data['staff_id']
            try:
                staff_profile.objects.get(staff_id=a)
                serializer.save()
                return Response(serializer.data)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def list(self,request):
        data = staff_qualification.objects.get(staff_id=1)
        serializer = self.get_serializer(data)
        return Response(serializer.data)



class staffexpviewset(GenericViewSet):
    queryset = staff_experience.objects.all()
    serializer_class = staff_exp_serializer

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            a = request.data['staff_id']
            try:
                staff_profile.objects.get(staff_id=a)
                serializer.save()
                return Response(serializer.data)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def list(self,request):
        data = staff_experience.objects.get(staff_id=1)
        serializer = self.get_serializer(data)
        return Response(serializer.data)


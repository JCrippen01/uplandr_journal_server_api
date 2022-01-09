from uplandrapi.models.journal_user import JournalUser
from django.core.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from  uplandrapi.models import Dog, DogEntry
from rest_framework.decorators import action


class DogView(ViewSet):
    def list(self,request):
        dogs = Dog.objects.all().order_by('name')
        serializer = DogSerializer(dogs, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
            serializer = DogSerializer(dog, many=False, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
            dog.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Dog.DoesNotExist as ex:
            return Response({"Message", "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request):
        try:
            Dog.objects.create(
                name = request.data['name'],
                breed = request.data['breed'],
                sex = request.data['sex'],
                age = request.data['age'],
                description = request.data['description']
            )
            return Response({"Message": "Dog Created"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def update(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
            dog.name = request.data['name']
            dog.breed = request.data['breed']
            dog.sex = request.data['sex']
            dog.age = request.data['age']
            dog.description = request.data['description']
            dog.save()
            return Response({"Message":"Updated Dog"}, status=status.HTTP_204_NO_CONTENT)
        except Dog.DoesNotExist as ex:
            return Response({"Message": ex.ars[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ("id","name","age", "breed", "sex", "description")
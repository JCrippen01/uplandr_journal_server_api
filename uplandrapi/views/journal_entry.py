"""View module for handling requests about games"""
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
# from django.db.models import Count, Q
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from uplandrapi.models import JournalEntry, JournalUser, DogEntry, Dog
# from rest_framework.decorators import action
from django.contrib.auth.models import User
from datetime import datetime, time



class JournalEntryView(ViewSet):
    def list(self, request):

        entrys = JournalEntry.objects.all()
        # if request.auth.user.is_admin:
        #     entrys = JournalEntry.objects.all()
        # else:
        #     entrys = JournalEntry.objects.all().filter(approved=True)

        serializer = JournalEntrySerializer(
            entrys, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        # user = JournalUser.objects.get(user=request.auth.user)
        try:
            entry = JournalEntry.objects.get(pk=pk)
            # entry.is_author = entry.user == user
            serializer = JournalEntrySerializer(entry, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk):
        #TODO: if commented out feature is broken, if not tested good.
            #TODO Set up dogs / Test Dogs
        try:
            entry = JournalEntry.objects.get(pk=pk)

            entry.dogs = Dog.objects.get(
                pk=request.data['dog_id'])
            entry.title = request.data['title']
            entry.entry_date = entry.entry_date
            entry.duration = entry.duration
            entry.party = request.data['party']
            entry.location = request.data['location']
            # entry.weather = request.data['weather']
            # entry.species.set = (request.data['speciesId'])
            entry.gear = request.data['gear']
            entry.hunt_highlights=request.data['hunt_highlights']
            entry.user = entry.user
            entry.save()
            return Response({"message": "Updated Post"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def partial_update(self, request, pk):
        
        try:
            entry = JournalEntry.objects.get(pk=pk)
            entry.dogs.set(request.data['dogs'])
            entry.save()
            return Response({"message": "Updated Entry"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            entry = JournalEntry.objects.get(pk=pk)
            entry.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except JournalEntry.DoesNotExist as ex:
            return Response({"Message": "Entry does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        user = JournalUser.objects.get(user=request.auth.user)
        try:
            entry = JournalEntry.objects.create(
                user=user,
                # dog=Dog.objects.get(pk=request.data['dog_id']),
                title=request.data['title'],
                entry_date=datetime.now().strftime("%Y-%m-%d"),
                duration = time(),
                party=request.data['party'],
                location=request.data['location'],
                hunt_highlights=request.data['hunt_highlights'],
                # weather=request.data['weather'],
                gear=request.data['gear'],
            )
            # entry.species.set(request.data['speciesIds'])
            serializer = JournalEntrySerializer(
                entry, many=False, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DogEntry
        fields = ('id', 'entry', 'dog')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class JournalUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = JournalUser
        fields = ('id', 'user')


class JournalEntrySerializer(serializers.ModelSerializer):
    # user = JournalUserSerializer()
    # is_author = serializers.BooleanField(required=False)

    class Meta:
        model = JournalEntry
        fields = ('id', 'user', 'title', 'entry_date', 'duration', 'party',
                  'location', 'weather', 'gear', 'hunt_highlights','dogs')
        depth = 1

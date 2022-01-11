from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from  uplandrapi.models import DogEntry
from uplandrapi.models.journal_entry import JournalEntry


class DogEntryView(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            dog_entry = DogEntry.objects.get(pk=pk)
            serializer = DogEntrySerializer(dog_entry, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        dog_entrys = DogEntry.objects.all()

        # Note the additional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = DogEntrySerializer(
            dog_entrys, many=True, context={'request': request})
        return Response(serializer.data)
    
    


class DogEntrySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    Arguments:
        serializers
    """
    class Meta:
        model = DogEntry
        fields = ('id', 'dog', 'entry' )
        depth = 1
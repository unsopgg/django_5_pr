from rest_framework import generics


from applications.ranobe.models import Ranobe


from applications.ranobe.serializer import RanobeSerializer


class RanobeListView(generics.ListAPIView):
    queryset = Ranobe.objects.all()
    serializer_class = RanobeSerializer

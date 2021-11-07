from rest_framework import generics


from applications.car.models import Car


from applications.car.serializer import CarSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

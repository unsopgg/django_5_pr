from django.urls import path


from applications.car.views import CarListView


urlpatterns = [
    path('car-list/', CarListView.as_view())
]
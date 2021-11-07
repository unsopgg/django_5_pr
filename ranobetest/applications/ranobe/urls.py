from django.urls import path


from applications.ranobe.views import RanobeListView


urlpatterns = [
    path('ranobe-list/', RanobeListView.as_view()),
]
from django.urls import path


from applications.film.views import FilmListView


urlpatterns = [
    path('film-list/', FilmListView.as_view())
]
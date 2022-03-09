from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserView, FilmView, SearchView, SearchDetailsView, AddFilmView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register('user', UserView, basename='user')
router.register('films', FilmView, basename='films')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('search', SearchView.as_view(), name='search'),
    path('searchdetails', SearchDetailsView.as_view(), name='search'),
    path('addfilm/', AddFilmView.as_view(), name='search'),
    path('api/token/', obtain_auth_token, name = 'obtain')
]

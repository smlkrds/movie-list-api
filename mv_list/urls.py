"""mv_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.views import MovieListAPIView, CustomListAddMovieAPIView, CustomListMoviesAPIView, CreateCustomListAPIView, \
    MovieDetailView

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<str:primaryTitle>/', MovieDetailView.as_view(), name='movie_detail'),
    path('custom-list/create/<str:name>/', CreateCustomListAPIView.as_view(), name='create-custom-list'),
    path('custom-list/<str:name>/add-movie/', CustomListAddMovieAPIView.as_view(), name='custom-list-add-movie'),
    path('custom-list/<int:custom_list_id>/movies/', CustomListMoviesAPIView.as_view(), name='custom-list-movies'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

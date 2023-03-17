from rest_framework import generics, authentication, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Movie, CustomList
from api.serializers import MovieSerializer, CustomListSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CreateCustomListAPIView(APIView):
    def post(self, request, *args, **kwargs):
        name = kwargs.get('name')
        if not name:
            return Response({'error': 'Please provide a list name'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the authenticated user
        user = request.user

        # Check if the list name already exists for the authenticated user
        try:
            CustomList.objects.get(name=name, user=user)
            return Response({'error': f'A list with the name {name} already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        except CustomList.DoesNotExist:
            pass

        # Create a new movie list for the authenticated user
        movie_list = CustomList.objects.create(name=name, user=user)
        return Response({'id': movie_list.id, 'name': movie_list.name}, status=status.HTTP_201_CREATED)



class CustomListMoviesAPIView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        custom_list = get_object_or_404(CustomList, id=self.kwargs.get('custom_list_id'))
        return custom_list.movies.all()

    def get_object(self):
        user = self.request.user
        custom_list_id = self.kwargs['custom_list_id']
        custom_list = CustomList.objects.get(user=user, id=custom_list_id)
        return custom_list.movies.all()

    def retrieve(self, request, *args, **kwargs):
        movies = self.get_object()
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

class CustomListAddMovieAPIView(generics.UpdateAPIView):
    serializer_class = CustomListSerializer

    def get_object(self):
        user = self.request.user
        name = self.kwargs['name']
        custom_list = CustomList.objects.get(user=user, name=name)
        return custom_list

    def put(self, request, *args, **kwargs):
        movie_id = request.data['movie_id']
        custom_list = self.get_object()
        custom_list.movies.add(movie_id)
        custom_list.save()
        serializer = self.get_serializer(custom_list)
        return Response(serializer.data)

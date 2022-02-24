from rest_framework import generics, status, pagination
from .serializers import *
from rest_framework.response import Response
import django_filters.rest_framework
from django.core.exceptions import ObjectDoesNotExist


class User_Data_ListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = user_data.objects.all()
    serializer_class = user_data_serializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['first_name', 'age']
    ordering_fields = ['age', 'first_name']


class User_Data_UpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_data.objects.all()
    serializer_class = user_data_serializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = user_data.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            queryset = user_data.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(queryset, data=self.request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = user_data.objects.get(id=self.kwargs["id"])
            instance.delete()
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)


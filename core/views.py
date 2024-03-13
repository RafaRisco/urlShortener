from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import redirect



from .models import ShortsUrl
from .serializers import ShortsUrlSerializer

# Create your views here.

class ShortUrlsSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ShortsUrlSerializer
    queryset = ShortsUrl.objects.all().order_by('counter')[0:100:]


# class ShortUrlViewApi(RetrieveAPIView):
#     serializer_class = ShortsUrlSerializer
#     lookup_field = 'short_url'
#     queryset = ShortsUrl.objects.all().order_by('counter')

#     def get_object(self):
#         obj = ShortsUrl.objects.filter(short_url=self.kwargs.get('short_url')).first()
#         print(obj.url, 'obj.url')
#         # PENDING: increase the counter
#         return redirect(f"{obj.url}")
#         # return super().get_object()
    
def optout(request, short_url):
    obj = ShortsUrl.objects.filter(short_url=short_url).first()
    obj.counter += 1
    obj.save()
    print(obj.url, 'obj.url')
    # PENDING: increase the counter
    return redirect(f"{obj.url}")
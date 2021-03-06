
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from uplandrapi.models import JournalUser
from rest_framework import routers
from uplandrapi.views import register_user, login_user, JournalEntryView,DogView


router=routers.DefaultRouter(trailing_slash=False)
router.register(r'entrys', JournalEntryView, 'entry')
router.register(r'dogs', DogView, 'dog')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
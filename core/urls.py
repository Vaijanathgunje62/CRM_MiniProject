
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('account.urls','account'))),
    path('crm', include(('client_relationship_manager.urls', 'crm'))),
   
]
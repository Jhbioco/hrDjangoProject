
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('employees.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'), name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'HR Management'
admin.site.site_title = 'Administration'
admin.site.index_title = "Version 1.0"
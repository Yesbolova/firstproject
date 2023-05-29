from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path ('',include ('main.urls')),

]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)


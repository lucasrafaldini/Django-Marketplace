from django.conf.urls import url, include
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    #url(r'^s3direct/', include('s3direct.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('portal.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('billing.urls')),

]

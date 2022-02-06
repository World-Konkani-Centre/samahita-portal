from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from samahita import settings
# import users.urls as user_url
from .views import index

handler404 = 'samahita.views.handler404'
handler500 = 'samahita.views.handler500'
handler400 = 'samahita.views.handler400'
handler403 = 'samahita.views.handler403'


urlpatterns = [
    path('', index, name='index'),
    # path('grappelli/', include('grappelli.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    # path('users/', include(user_url)),
    # path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

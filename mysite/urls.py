from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
 
from rest_api import rest_views, serializers

router = routers.DefaultRouter()

router.register(r'user-wallet', rest_views.WalletViewSet,'user-wallet')

# router.register(r'ref-user', rest_views.WalletViewSet,'ref-user')


schema_view = get_schema_view(title='Opinverse Rest API',renderer_classes=[OpenAPIRenderer,SwaggerUIRenderer])

urlpatterns = [ 
     
    #Rest Api..
    path('api-', include(router.urls)),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

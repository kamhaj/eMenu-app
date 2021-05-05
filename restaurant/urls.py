from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


# for Swagger UI
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   ## admin
   path('admin/', admin.site.urls),

   ## eMenu app
   path('', include('eMenu.urls', namespace='eMenu')),
   path('api/eMenu/', include('eMenu.api_urls', namespace='eMenuAPI')),

    
   ## Swagger
   # This exposes 4 endpoints:

   #     A JSON view of your API specification at /swagger.json
   #     A YAML view of your API specification at /swagger.yaml
   #     A swagger-ui view of your API specification at /swagger/
   #     A ReDoc view of your API specification at /redoc/
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('accounts/', include('rest_framework.urls')), # to enable Django login


]

## according to Django docs, this way is okay when NOT IN PRODUCTION
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
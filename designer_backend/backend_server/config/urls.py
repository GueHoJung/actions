"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django REST Framework API Auto create
from django.urls import include, path, re_path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_url_v1_patterns = [
    path('v1/', include('designer_server.urls', namespace='designer_server_api')),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    # path('customer/', include('customer.urls', namespace='customer')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Mobile Designer App Backend Server Open API",
        default_version='v1',
        description="Softstone Designer App Backend Server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gh.jung@softstoneinc.com"),
        license=openapi.License(name="Softstone Inc"),
    ),
    validators=['flex',  'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('designer_server.urls')),
    path('', include('web.urls')),
    path('reservation/', include('reservation.urls')),
    # path('customer/', include('customer.urls')),

    # Auto DRF API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]


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
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    """
    # CLASS : BothHttpAndHttpsSchemaGenerator
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 11:41 AM
    # DESCRIPTION
        - HTTP and HTTPS
        - https://stackoverflow.com/questions/55568431/how-can-i-configure-https-schemes-with-the-drf-yasg-auto-generated-swagger-pag
    """

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_url_v1_patterns = [
    path('v1/', include('designer_server.urls', namespace='designer_server_api')),
    path('archi/', include('hexagonal_archi_template.urls', namespace='hexagonal_archi_template')),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('analysis/', include('analysis.urls', namespace='analysis')),
    path('employ/', include('employ.urls', namespace='employ')),
    path('order/', include('order.urls', namespace='order')),
    path('stats/', include('stats.urls', namespace='stats')),
    path('itsr/', include('itsr.urls', namespace='itsr')),

]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Mobile Designer App Backend Server Open API",
        default_version='v1',
        description="Softstone Designer App Backend Server\n"
                    "---\n"
                    "## API PARAMS INFO DESCRIPTION\n"
                    "---\n"
                    "|           PARAM NAME          |        PARAM TYPE         |        MAX LENGTH    |          REQUIRED         |                 DESC                |                    ETC                             |\n"
                    "|:-----------------------------:|:-------------------------:|:---------------------:|:-------------------------:|:-----------------------------------:|:--------------------------------------------------:|\n"
                    "|			cpID			    |			varchar			|			200			|			TRUE			|			기업아이디                   |          JN			                              |\n"
                    "|			loginShopId		    |			varchar			|			200			|			TRUE			|			로그인매장                   |          149			                              |\n"
                    "|			loginId			    |			varchar			|			200			|			TRUE			|			로그인아이디                 |          11273			                          |\n"
                    "|			path			    |			varchar			|			200			|			TRUE			|			메뉴패스			        |           /crm/anlys/cust-anlys-inflw			     |\n"
                    "|			name			    |			varchar			|			200			|			TRUE			|			메뉴명			            |			cust-anlys-inflw			             |\n"
                    "|			standard		    |			varchar			|			200			|			TRUE			|			조회기준=>매장/디자이너		    |			DSGN			                         |\n"
                    "|			shopNm			    |			varchar			|			200			|			TRUE			|			매장이름			        |           가든서현역점			                     |\n"
                    "|			shopId			    |			varchar			|			200			|			TRUE			|			매장아이디			         |          103			                              |\n"
                    "|			shopList		    |			varchar			|			200			|			TRUE			|			매장아이디목록			      |         '10'			                           |\n"
                    "|			shopCnt			    |			varchar			|			200			|			TRUE			|			매장수			            |           1			                             |\n"
                    "|			term			    |			varchar			|			200			|			TRUE			|			월/주/일=>month/week/day, 월/분기/연도 => month/qrtr/year    |           week			                         |\n"
                    "|			searchStDt		    |			varchar			|			200			|			TRUE			|			조회시작일			         |          20022009			                      |\n"
                    "|			searchEdDt		    |			varchar			|			200			|			TRUE			|			조회종료일			         |          2002211			                           |\n"
                    "|			searchQrtr		    |			varchar			|			200			|			TRUE			|			조회분기			        |						                              |\n"
                    "|			searchWeek		    |			varchar			|			200			|			TRUE			|			조회주차			        |           3			                              |\n"
                    "|			empBuyYn		    |			varchar			|			200			|			TRUE			|			직원오더여부			              |						                                |\n"
                    "|			ordTpCd			    |			varchar			|			200			|			TRUE			|			오더유형코드			              |						                                |\n"
                    "|			trmTpCd			    |			varchar			|			200			|			TRUE			|			시술유형코드			              |						                                |\n"
                    "|			payDivCd		    |			varchar			|			200			|			TRUE			|			결제유형코드			              |						                                |\n"
                    "|			custClsfcCd		    |			varchar			|			200			|			TRUE			|			고객유형코드			              |						                                |\n"
                    "|			mbrGrdCd		    |			varchar			|			200			|			TRUE			|			멤버십등급코드			              |						                                |\n"
                    "|			prpTpCd			    |			varchar			|			200			|			TRUE			|			회원권유형코드	              |						                                |\n"
                    "|			tktTpCd			    |			varchar			|			200			|			TRUE			|			횟수권유형코드			      |						                                |\n"
                    "|			prdcBrndCd		    |			varchar			|			200			|			TRUE			|			점판브랜드코드	              |         null			                            |\n"
                    "|			gndrCd			    |			varchar			|			200			|			TRUE			|			성별코드			        |           'F','M'			                           |\n"
                    "|			joinTpCd		    |			varchar			|			200			|			TRUE			|			유입경로코드			     |          '01','02','03','04','05','06','07','08','09','10','11','99' |\n"
                    # "|                              |                           |                       |                           |                                       |[ 01 : 포털검색, 02 : 네이버예약, 03 : 인스타그램, 04 : 유튜브, 05 : 페이스북, 06 : 카카오헤어, 07 : 오프라인광고, 08 : 지인추천, 09 : 자택근처, 10 : 직장근처, 11 : 근처지역방문, 99 : 기타 ]	|\n"
                    "|			ageGrpCd		    |			varchar			|			200			|			TRUE			|			연령대코드			         |          'A10','A30','A60'			               |\n"
                    "|			userNm			    |			varchar			|			200			|			TRUE			|			디자이너이름			     |						                                |\n"
                    "|			userId			    |			varchar			|			200			|			TRUE			|			디자이너아이디			      |						                                |\n"
                    "|			userList		    |			varchar			|			200			|			TRUE			|			디자이너아이디목록			   |            '9829','127','10786','113'               |\n"
                    "|			userCnt			    |			varchar			|			200			|			TRUE			|			디자이너수			         |          4                                          |\n"
                    "|			realAgeGrpCd	    |			varchar			|			200			|			TRUE			|			연령대코드			              |         '0','10','30','60','70','80','90'			|\n"
                    "|			custAnlysDiv	    |			varchar			|			200			|			TRUE			|			-			              |         Inflow                                      |\n"
                    "<br/>"
                    "<br/>",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gh.jung@softstoneinc.com"),
        license=openapi.License(name="Softstone Inc"),
    ),
    validators=['flex', 'ssv'],
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,  # HTTP and HTTPS
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('designer_server.urls')),
    path('', include('web.urls')),
    path('archi/', include('hexagonal_archi_template.urls')),
    path('reservation/', include('reservation.urls')),
    path('customer/', include('customer.urls')),
    path('analysis/', include('analysis.urls')),
    path('employ/', include('employ.urls')),
    path('order/', include('order.urls')),
    path('stats/', include('stats.urls')),
    path('itsr/', include('itsr.urls')),

    # Auto DRF API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

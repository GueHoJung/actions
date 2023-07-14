from django.contrib import admin

# Register your models here.
# Django admin 페이지에 DesignerTest 모델을 등록 하는 코드

from .models import DesignerTest

admin.site.register(DesignerTest)


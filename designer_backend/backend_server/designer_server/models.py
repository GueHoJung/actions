from django.db import models

# 모델 클래스를 정의할 때, Meta 클래스를 정의하여 모델 클래스에 대한 옵션을 지정할 수 있습니다.
# ordering 옵션은 데이터베이스의 객체 목록을 가져올 때 정렬 순서를 의미합니다.
# 예시의 ["name", "age"]은 name과 age를 위주로 각각 오름차순으로 정렬합니다.
# 만약, name은 내림차순, age는 오름차순으로 정렬할 경우, -을 붙여 ["-name", "age"]로 사용합니다.
# 출처 : https://076923.github.io/posts/Python-Django-5/

# Create your models here.
class DesignerTest(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'designer_test'


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

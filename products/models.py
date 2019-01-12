from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    # 后台管理admin看到的内容
    title = models.CharField(default='例：抖音—用短视频记录美好生活', max_length=50)
    intro = models.TextField(default='在这里写APP介绍')
    url   = models.CharField(default='Http://', max_length=100)
    # default文件应首先从MEDIA_URL去找,选择的图片则会被放到uooad_to路径
    icon  = models.ImageField(default='default_icon.png', upload_to='image/')
    image = models.ImageField(default='default_image.png', upload_to='image/')

    votes = models.IntegerField(default=1)
    pub_date  = models.DateField()
    # 绑定外键（一删都删）
    Hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def short_intro(self):
        return self.intro[:60]

from user_control.models import UserModel
from django.db import models


class ArticleCategoryModel(models.Model):
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class ArticleModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(ArticleCategoryModel, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField()
    image = models.ImageField(upload_to="images/article/", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    totalViewCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_title + " by " + self.article_author.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

from django.contrib import admin
from .models import *

admin.site.register(CommunityPostModel)
admin.site.register(CommunityPostLikeModel)
admin.site.register(CommunityPostCommentModel)

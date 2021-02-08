from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

# from bookmark.views import BookmarkLV, BookmarkDV

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('bookmark/',BookmarkLV.as_view(), name='index'),
#     path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'), #메인페이지
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]

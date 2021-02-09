from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

from django.conf.urls.static import static
from django.conf import settings
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
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

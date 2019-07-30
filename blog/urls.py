from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')), # 게시판 urls
    path('portfolio/', include('portfolio.urls')), # 포트폴리오 urls
    path('accounts/', include('accounts.urls')), # 로그인 urls
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

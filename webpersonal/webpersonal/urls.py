# Django utilities
from django.contrib import admin
from django.urls import path
from django.conf import settings as st

# Views
from portfolio import views as portfolio_views
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('contact/', core_views.contact, name="contact"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('admin/', admin.site.urls),
]

if st.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)    

from django.conf.urls import url
from django.contrib import admin
import face_detector.views

urlpatterns = [
    # Examples:

    url(r'^face_detection/detect/$', 'face_detector.views.detect'),

    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
]

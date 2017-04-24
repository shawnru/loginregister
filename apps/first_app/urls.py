from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    # url(r'^session-test/$', views.session_test_1),
    # url(r'^session-test/done/$', views.session_test_2),

]

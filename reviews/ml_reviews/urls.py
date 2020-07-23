from django.urls import path

from . import views

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import EndpointViewSet
from .views import MLAlgorithmViewSet
from .views import MLAlgorithmStatusViewSet
from .views import MLRequestViewSet
from .views import PredictView
from .views import ABTestViewSet
from .views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(
    r"mlalgorithmstatuses",
    MLAlgorithmStatusViewSet,
    basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    # path('reviews', views.index, name='index'),
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('<int:review_id>/review/', views.review, name='review'),
    path('<int:opinion_id>/opinion/', views.opinion, name='opinion'),
    url(
        r"^api/v1/",
        include(router.urls)
    ),
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$",
        PredictView.as_view(),
        name="predict"
    ),
    url(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)",
        StopABTestView.as_view(),
        name="stop_ab"
    ),
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$",
        PredictView.as_view(),
        name="predict"
    ),
    url(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)",
        StopABTestView.as_view(),
        name="stop_ab"
    ),
    ]

from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

'''from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='articleListView'),
    path('create/', ArticleCreateView.as_view(), name='articleCreateView'),
    path('<pk>', ArticleDetailView.as_view(), name='articleDetailView'),
    path('<pk>/update/', ArticleUpdateView.as_view(), name='articleUpdateView'),
    path('<pk>/delete/', ArticleDeleteView.as_view(), name='articleDeleteView'),

]'''

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentListCreateView, CommentRetrieveUpDateDestroyView

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comment/', CommentListCreateView.as_view(), name='comment'),
    path('comment/<int:pk>', CommentRetrieveUpDateDestroyView.as_view(), name='comment_detail'),
]

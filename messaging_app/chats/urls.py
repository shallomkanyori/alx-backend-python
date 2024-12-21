from .views import ConversationViewSet, MessageViewSet

urlpatterns = [
    path('conversations/', ConversationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('conversations/<int:pk>/', ConversationViewSet.as_view({
        'get': 'retrieve'
    })),
    path('conversations/<int:pk>/add_message/', ConversationViewSet.as_view({
        'post': 'add_message'
    })),
    path('messages/', MessageViewSet.as_view({
        'get': 'list'
    })),
    path('messages/<int:pk>/', MessageViewSet.as_view({
        'get': 'retrieve'
    })),
]

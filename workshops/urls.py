from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import WorkshopListView, WorkshopDetailView, WorkshopCreateView, WorkshopUpdateView
from . import views

urlpatterns = [
    path('', login_required(WorkshopListView.as_view()), name='workshops'),
    path('<int:pk>/', login_required(WorkshopDetailView.as_view()), name='workshop-detail'),
    path('new/', WorkshopCreateView.as_view(), name='workshop-create'),
    path('<int:pk>/update', login_required(WorkshopUpdateView.as_view()), name='workshop-update'),
]
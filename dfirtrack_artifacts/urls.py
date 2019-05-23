from django.urls import include, path
from . import views

urlpatterns = (
    # urls for Artifact
    path(r'artifact/', views.ArtifactListView.as_view(), name='artifacts_artifact_list'),
    path(r'artifact/create/', views.ArtifactCreateView.as_view(), name='artifacts_artifact_create'),
    path(r'artifact/detail/<int:pk>/', views.ArtifactDetailView.as_view(), name='artifacts_artifact_detail'),
    path(r'artifact/update/<int:pk>/', views.ArtifactUpdateView.as_view(), name='artifacts_artifact_update'),
)

urlpatterns += (
    # urls for Artifactstatus
    path(r'artifactstatus/', views.ArtifactstatusListView.as_view(), name='artifacts_artifactstatus_list'),
    path(r'artifactstatus/create/', views.ArtifactstatusCreateView.as_view(), name='artifacts_artifactstatus_create'),
    path(r'artifactstatus/detail/<int:pk>/', views.ArtifactstatusDetailView.as_view(), name='artifacts_artifactstatus_detail'),
    path(r'artifactstatus/update/<int:pk>/', views.ArtifactstatusUpdateView.as_view(), name='artifacts_artifactstatus_update'),
)
urlpatterns += (
    # urls for Artifacttype
    path(r'artifacttype/', views.ArtifacttypeListView.as_view(), name='artifacts_artifacttype_list'),
    path(r'artifacttype/create/', views.ArtifacttypeCreateView.as_view(), name='artifacts_artifacttype_create'),
    path(r'artifacttype/detail/<int:pk>/', views.ArtifacttypeDetailView.as_view(), name='artifacts_artifacttype_detail'),
    path(r'artifacttype/update/<int:pk>/', views.ArtifacttypeUpdateView.as_view(), name='artifacts_artifacttype_update'),
)

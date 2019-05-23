from django.urls import include, path
from dfirtrack_artifacts.views import artifact_view, artifactstatus_view, artifacttype_view

urlpatterns = (
    # urls for Artifact
    path(r'artifact/', artifact_view.ArtifactListView.as_view(), name='artifacts_artifact_list'),
    path(r'artifact/create/', artifact_view.ArtifactCreateView.as_view(), name='artifacts_artifact_create'),
    path(r'artifact/detail/<int:pk>/', artifact_view.ArtifactDetailView.as_view(), name='artifacts_artifact_detail'),
    path(r'artifact/update/<int:pk>/', artifact_view.ArtifactUpdateView.as_view(), name='artifacts_artifact_update'),
)

urlpatterns += (
    # urls for Artifactstatus
    path(r'artifactstatus/', artifactstatus_view.ArtifactstatusListView.as_view(), name='artifacts_artifactstatus_list'),
    path(r'artifactstatus/create/', artifactstatus_view.ArtifactstatusCreateView.as_view(), name='artifacts_artifactstatus_create'),
    path(r'artifactstatus/detail/<int:pk>/', artifactstatus_view.ArtifactstatusDetailView.as_view(), name='artifacts_artifactstatus_detail'),
    path(r'artifactstatus/update/<int:pk>/', artifactstatus_view.ArtifactstatusUpdateView.as_view(), name='artifacts_artifactstatus_update'),
)
urlpatterns += (
    # urls for Artifacttype
    path(r'artifacttype/', artifacttype_view.ArtifacttypeListView.as_view(), name='artifacts_artifacttype_list'),
    path(r'artifacttype/create/', artifacttype_view.ArtifacttypeCreateView.as_view(), name='artifacts_artifacttype_create'),
    path(r'artifacttype/detail/<int:pk>/', artifacttype_view.ArtifacttypeDetailView.as_view(), name='artifacts_artifacttype_detail'),
    path(r'artifacttype/update/<int:pk>/', artifacttype_view.ArtifacttypeUpdateView.as_view(), name='artifacts_artifacttype_update'),
)

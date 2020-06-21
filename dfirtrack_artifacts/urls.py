from django.urls import path
from dfirtrack_artifacts.exporter.spreadsheet import xls as spreadsheet_xls
from dfirtrack_artifacts.views import artifact_view, artifactstatus_view, artifacttype_view

urlpatterns = (
    # urls for Artifact
    path(r'artifact/', artifact_view.ArtifactListView.as_view(), name='artifacts_artifact_list'),
    path(r'artifact/create/', artifact_view.ArtifactCreateView.as_view(), name='artifacts_artifact_create'),
    path(r'artifact/detail/<int:pk>/', artifact_view.ArtifactDetailView.as_view(), name='artifacts_artifact_detail'),
    path(r'artifact/update/<int:pk>/', artifact_view.ArtifactUpdateView.as_view(), name='artifacts_artifact_update'),
    path(r'artifact/exporter/spreadsheet/xls/artifact/', spreadsheet_xls.artifact, name='artifact_exporter_spreadsheet_xls'),
)

urlpatterns += (
    # urls for Artifactstatus
    path(r'artifactstatus/', artifactstatus_view.ArtifactstatusListView.as_view(), name='artifacts_artifactstatus_list'),
    path(r'artifactstatus/detail/<int:pk>/', artifactstatus_view.ArtifactstatusDetailView.as_view(), name='artifacts_artifactstatus_detail'),
)

urlpatterns += (
    # urls for Artifacttype
    path(r'artifacttype/', artifacttype_view.ArtifacttypeListView.as_view(), name='artifacts_artifacttype_list'),
    path(r'artifacttype/create/', artifacttype_view.ArtifacttypeCreateView.as_view(), name='artifacts_artifacttype_create'),
    path(r'artifacttype/detail/<int:pk>/', artifacttype_view.ArtifacttypeDetailView.as_view(), name='artifacts_artifacttype_detail'),
    path(r'artifacttype/update/<int:pk>/', artifacttype_view.ArtifacttypeUpdateView.as_view(), name='artifacts_artifacttype_update'),
)

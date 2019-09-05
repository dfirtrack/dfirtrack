from django.contrib import admin
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
# Register your models here.
admin.site.register(Artifact)
admin.site.register(Artifactstatus)
admin.site.register(Artifacttype)
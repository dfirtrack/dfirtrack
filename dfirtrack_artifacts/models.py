from django.contrib.auth.models import User
from django.db import models
import logging
from time import strftime

#initialize logger
stdlogger = logging.getLogger(__name__)

# Create your models here.
class Artifact(models.Model):
    ''' Model used for storing a forensic artifact '''

    # primary key
    artifact_id = models.AutoField(primary_key=True)

    # foreing key(s)
    #TODO: Check if we need a seperate app for Case begin with dfirtrack_main.Case
    #TODO: Create ArtifactType
    #artifact_type = models.ForeignKey()
    #TODO: Create ArtifactStatus
    #artifact_status
    #case ForeignKey('dfirtrack_main.Case', related_name='artifact_case', on_delete=models.Protect, blank=True, null=True)
    system = models.ForeignKey('System', on_delete=models.Protect)

    # meta information
    artifact_create_time = models.DateTimeField(auto_now_add=True)
    artifact_modify_time = models.DateTimeField(auto_now_add=True)
    artifact_created_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifact_created_by')
    artifact_modified_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifact_modified_by')

    # string representation
    def __str__(self):
        return 'Artifact {0} ({1})'.format(str(self.artifact_id), self.system)

class Artifactstatus(models.Modell):
    ''' Artifactstatus that shows the current status of the artifact like: New, Requested, Processed, Imported...'''

    # primary key
    artifactstatus_id = models.AutoFieldField(primary_key=True)

    # main entity information
    artifactstatus_name = models.CharField(max_length=255, blank=False, unique=True)
    artifactstatus_description = models.CharField(max_length=2048, blank=False, null=False, unique=True)
    artifactstatus_slug = models.CharField(max_length=255, blank=False, null=False, unique=True)

    # meta information
    artifactstatus_create_time = models.DateTimeField(auto_now_add=True)
    artifactstatus_modify_time = models.DateTimeField(auto_now_add=True)
    artifactstatus_created_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifactstatus_created_by')
    artifactstatus_modified_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifactstatus_modified_by')

    # string representation
    def __str__(self):
        return 'Artifacstatus {0}'.format(str(self.artifactstatus_id))

    #define logger
    def logger(artifactstatus, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifactstatus_id:" + str(artifactstatus.artifactstatus_id) +
            "|artifactstatus_name:" str(artfiactstatus.artifactstatus_name) +
            "|artifactstatus_description:" str(artfiactstatus.artifactstatus_description) +
            "|artifactstatus_slug:" str(artfiactstatus.artifactstatus_slug)
        )

class Artifacttype(models.Modell):
    ''' Artifacttype like File, Registry-Key, Registry-Hive, etc. '''

    # primary key
    artifacttype_id = models.AutoFieldField(primary_key=True)

    # main entity information
    artifacttype_name = models.CharField(max_length=255, blank=False, unique=True)
    artifacttype_description = models.CharField(max_length=2048, blank=False, null=False, unique=True)
    artifacttype_slug = models.CharField(max_length=255, blank=False, null=False, unique=True)

    # meta information
    artifacttype_create_time = models.DateTimeField(auto_now_add=True)
    artifacttype_modify_time = models.DateTimeField(auto_now_add=True)
    artifacttype_created_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifacttype_created_by')
    artifacttype_modified_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifacttype_modified_by')

    # string representation
    def __str__(self):
        return 'Artifacstatus {0}'.format(str(self.artifacttype_id))

    #define logger
    def logger(artifactstatus, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifacttype_id:" + str(artifactstatus.artifacttype_id) +
            "|artifacttype_name:" str(artfiactstatus.artifacttype_name) +
            "|artifacttype_description:" str(artfiactstatus.artifacttype_description) +
            "|artifacttype_slug:" str(artfiactstatus.artifacttype_slug)
        )

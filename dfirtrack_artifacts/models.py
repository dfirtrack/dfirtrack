from django.contrib.auth.models import User
from django.db import models
import logging
from time import strftime
import uuid

#initialize logger
stdlogger = logging.getLogger(__name__)

# Create your models here.
class Artifact(models.Model):
    ''' Model used for storing a forensic artifact '''

    # primary key
    artifact_id = models.AutoField(primary_key=True)

    # foreing key(s)
    artifacttype = models.ForeignKey('Artifacttype', on_delete=models.PROTECT)
    artifactstatus = models.ForeignKey('Artifactstatus', on_delete=models.PROTECT, default=1)
    case = models.ForeignKey('Case', on_delete=models.PROTECT, blank=True, null=True)
    system = models.ForeignKey('System', on_delete=models.PROTECT)

    # main entity information
    artifact_description = models.CharField(max_length=4096, blank=False, null=False)
    artifact_md5 = models.CharField(max_length=4096, blank=False, null=False)
    artifact_name = models.CharField(max_length=255, blank=False, null=False)
    artifact_sha1 = models.CharField(max_length=4096, blank=False, null=False)
    artifact_sha256 = models.CharField(max_length=4096, blank=False, null=False)
    artifact_slug = models.CharField(max_length=255, blank=False, null=False)
    artifact_storage_path = models.CharField(max_length=4096, blank=False, null=False, unique=True)
    artifact_uuid = models.UUIDField(editable=False, null=False, blank=False)

    # set the ordering criteria
    Class Meta:
        ordering = ('artifact_name', )
    # meta information
    artifact_create_time = models.DateTimeField(auto_now_add=True)
    artifact_modify_time = models.DateTimeField(auto_now_add=True)
    artifact_created_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifact_created_by')
    artifact_modified_by_user_id = models.ForeignKey(User, on_delete=models.Protect, related_name='artifact_modified_by')

    # string representation
    def __str__(self):
	#TODO: Ask Stuhli, all ForeignKeys should be included here?
        return 'Artifact {0} ({1})'.format(str(self.artifact_id), self.system)

    #define logger
    def logger(artifact, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifact_id:" + str(artifact.artifact_id) +
            "|artifact_name:" + str(artifact.artifact_name) +
            "|artifact_description:" + str(artifact.artifact_description) +
            "|artifact_slug:" + str(artifact.artifact_slug) +
	    "|artifact_md5" + str(artifact.artifact_md5) +
	    "|artifact_sha1" + str(artifact.artifact_sha1) +
	    "|artifact_sha256" + str(artifact.artifact_sha256) +
	    "|artifact_storage_path" + str(artifact.artifact_storage_path) +
	    "|artifact_uuid" + str(artifact.artifact_uuid)
        )

    # # define some artifact routines
    #TODO: Implement them
    #   def create_artifact_directory(self, system_uuid, artifact_type, artifact_uuid):
    #     """ Generates the directory in which the artifact will be stored """
    #     # we generate the path for the evidence file
    #     artifact_evidence_path = (EVIDENCE_PATH+'/'+ str(system_uuid)+'/'+ artifact_type + '/' + str(artifact_uuid))
    #     if os.path.exists(artifact_evidence_path):
    #         print("Artifact-Path: {} already exists.".format(artifact_evidence_path))
    #         return artifact_evidence_path
    #     else:
    #         os.makedirs(artifact_evidence_path)
    #         return artifact_evidence_path

    # def save(self,*args,**kwargs):
    #     # generate slug
    #     self.slug = slugify(self.name)

    #     # we check if we have a new artifact
    #     if not self.pk:
    #         # generate uuid tpye 4 (completely random)
    #         self.artifact_uuid = uuid.uuid4()

    #         # set hashes to calculating while tasks are performed
    #         self.hashsum_md5 = 'Calculating...'
            # self.hashsum_sha1 = 'Calculating...'
            # self.hashsum_sha256 = 'Calculating...'

            # # we generate the artifact dir
            # system_uuid = self.system.uuid
            # artifact_type = self.artifact_type.slug
            # artifact_uuid = self.artifact_uuid
            
            # # we generate the artifact path in the EVIDENCE_PATH
            # artifact_evidence_path = self.create_artifact_directory(system_uuid, artifact_type, artifact_uuid)

            # # check if the storage_path from the form is equal to the artifact_evidence_path
            # if self.storage_path != artifact_evidence_path:
            #     # check if we have a folder than we create an archive
            #     if os.path.isdir(self.storage_path):
            #         pass
            #     elif os.path.isfile(self.storage_path):
            #         # if not we will copy the artifact to the artifact_evidence_path
            #         destination = shutil.copy(self.storage_path, artifact_evidence_path)
            #     self.storage_path = destination
            # else:
            #     self.storage_path = artifact_evidence_path

        # super().save(*args,**kwargs)

    # def get_absolute_url(self):
    #     return reverse('system_artifact_detail', args=(self.pk,))

    # def get_update_url(self):
    #     return reverse('system_artifact_update', args=(self.pk,))


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
            "|artifactstatus_name:" str(artifactstatus.artifactstatus_name) +
            "|artifactstatus_description:" str(artifactstatus.artifactstatus_description) +
            "|artifactstatus_slug:" str(artifactstatus.artifactstatus_slug)
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
            "|artifacttype_name:" str(artifactstatus.artifacttype_name) +
            "|artifacttype_description:" str(artifactstatus.artifacttype_description) +
            "|artifacttype_slug:" str(artifactstatus.artifacttype_slug)
        )

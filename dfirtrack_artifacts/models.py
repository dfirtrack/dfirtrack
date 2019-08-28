from django.db import models
from django.db.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
import logging
from time import strftime
import uuid
from django.utils.text import slugify
import os
import shutil
from dfirtrack_main import models as main_models
from dfirtrack.config import EVIDENCE_PATH

#Get active user model
User = get_user_model()

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
    case = models.ForeignKey('dfirtrack_main.Case', related_name='artifact_case',on_delete=models.PROTECT, blank=True, null=True)
    system = models.ForeignKey('dfirtrack_main.System', related_name='artifact_system',on_delete=models.PROTECT)

    # main entity information
    artifact_acquisition_time = models.DateTimeField(blank=True, null=True)
    artifact_description = models.CharField(max_length=4096, blank=True, null=True)
    artifact_md5 = models.CharField(max_length=32, blank=True, null=True)
    artifact_name = models.CharField(max_length=4096, blank=False, null=False)
    artifact_sha1 = models.CharField(max_length=40, blank=True, null=True)
    artifact_sha256 = models.CharField(max_length=64, blank=True, null=True)
    artifact_slug = models.CharField(max_length=4096, blank=False, null=False)
    artifact_storage_path = models.CharField(max_length=4096, blank=False, null=False, unique=True)
    artifact_uuid = models.UUIDField(editable=False, null=False, blank=False)

    # meta information
    artifact_create_time = models.DateTimeField(auto_now_add=True)
    artifact_modify_time = models.DateTimeField(auto_now=True)
    artifact_created_by_user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='artifact_created_by')
    artifact_modified_by_user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='artifact_modified_by')

    # set the ordering criteria
    class Meta:
        ordering = ('artifact_name', )

    # string representation
    def __str__(self):
        return 'Artifact {0} ({1})'.format(str(self.artifact_id), self.system)
        
    def __unicode__(self):
        return u'%s' % self.artifact_name

    #define logger
    def logger(artifact, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifact_id:" + str(artifact.artifact_id) +
            "|artifact_name:" + str(artifact.artifact_name) +
            "|artifact_description:" + str(artifact.artifact_description) +
            "|artifact_slug:" + str(artifact.artifact_slug) +
            "|artifact_acquisition_time:" + str(artifact.artifact_acquisition_time) +
	    "|artifact_md5" + str(artifact.artifact_md5) +
	    "|artifact_sha1" + str(artifact.artifact_sha1) +
	    "|artifact_sha256" + str(artifact.artifact_sha256) +
	    "|artifact_storage_path" + str(artifact.artifact_storage_path) +
	    "|artifact_uuid" + str(artifact.artifact_uuid)
        )

    def save(self, *args, **kwargs):
        # generate slug
        self.artifact_slug = slugify(self.artifact_name)

        # we check if we have a new artifact
        if not self.pk:
            # generate uuid type4 (completely random type)
            self.artifact_uuid = uuid.uuid4()

        # set hashes to calculating while hash calculating is performed in background
        # self.artifact_md5 = 'Calculating...'
        # self.artifact_sha1 = 'Calculating...'
        # self.artifact_sha256 = 'Calculating...'

        # we generate the artifact path in the EVIDENCE_PATH
        artifact_evidence_path = self.create_artifact_directory(self.system.system_uuid, self.artifacttype.artifacttype_slug, self.artifact_uuid)

        ## check if the storage_path from the form is equal to the artifact_evidence_path
        #if self.artifact_storage_path != artifact_evidence_path:
        #    #TODO: We mnust change this logic, so that exception will be thrown if file does not exist
        #    #TODO: Check if we do not have file at the beginning --> calculate evidence path --> edit use new path testen
        #    # os.path.exists(self.artifact_storage_path)
        #    # check if we have a folder, then we do not need to create the dir
        #    if os.path.isdir(self.artifact_storage_path):
        #        pass
        #    elif os.path.isfile(self.artifact_storage_path):
        #        # if not we will copy the artifact to the artifact_evidence_path
        #        destination = ''
        #        destination = shutil.copy(self.artifact_storage_path, artifact_evidence_path)
        #    self.artifact_storage_path = destination
        #else:
        #    self.artifact_storage_path = artifact_evidence_path
        ##TODO: check if this works or if wee need
        ## super().save(*args,**kwargs)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('artifacts_artifact_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('artifacts_artifact_update', args=(self.pk,))

    def create_artifact_directory(self, system_uuid, artifacttype, artifact_uuid):
            """ Generates the directory in which the artifact will be stored """
            # we generate the path for the evidence file
            artifact_evidence_path = (EVIDENCE_PATH+'/'+ str(system_uuid)+'/'+ artifacttype + '/' + str(artifact_uuid))
            if os.path.exists(artifact_evidence_path):
                print("Artifact-Path: {} already exists.".format(artifact_evidence_path))
                return artifact_evidence_path
            else:
                os.makedirs(artifact_evidence_path)
                return artifact_evidence_path

class Artifactstatus(models.Model):
    ''' Artifactstatus that shows the current status of the artifact like: New, Requested, Processed, Imported...'''

    # primary key
    artifactstatus_id = models.AutoField(primary_key=True)

    # main entity information
    artifactstatus_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    artifactstatus_description = models.CharField(max_length=2048, blank=True, null=True)
    artifactstatus_slug = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        ordering = ('artifactstatus_name',)

    # string representation
    def __str__(self):
        return 'Artifactstatus {0}'.format(str(self.artifactstatus_name))

    #define logger
    def logger(self,artifactstatus, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifactstatus_id:" + str(artifactstatus.artifactstatus_id) +
            "|artifactstatus_name:" + str(artifactstatus.artifactstatus_name) +
            "|artifactstatus_description:" + str(artifactstatus.artifactstatus_description) +
            "|artifactstatus_slug:" + str(artifactstatus.artifactstatus_slug)
        )

    def save(self, *args, **kwargs):
        # generate slug
        self.artifactstatus_slug = slugify(self.artifactstatus_name)
        #TODO: check if this works or if wee need
        # super().save(*args,**kwargs)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('artifacts_artifactstatus_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('artifacts_artifactstatus_update', args=(self.pk,))

class Artifacttype(models.Model):
    ''' Artifacttype like File, Registry-Key, Registry-Hive, etc. '''

    # primary key
    artifacttype_id = models.AutoField(primary_key=True)

    # main entity information
    artifacttype_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    artifacttype_description = models.CharField(max_length=2048, blank=True, null=True)
    artifacttype_slug = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        ordering = ('artifacttype_name',)

    # string representation
    def __str__(self):
        return 'Artifacttype {0}'.format(str(self.artifacttype_name))

    #define logger
    def logger(self, artifactstatus, request_user, log_text):
        stdlogger.info(
            request_user +
            log_text +
            " artifacttype_id:" + str(artifacttype.artifacttype_id) +
            "|artifacttype_name:" + str(artifacttype.artifacttype_name) +
            "|artifacttype_description:" + str(artifacttype.artifacttype_description) +
            "|artifacttype_slug:" + str(artifacttype.artifacttype_slug)
        )

    def get_absolute_url(self):
            return reverse('artifacts_artifacttype_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('artifacts_artifacttype_update', args=(self.pk,))
    
    # override save()-method
    def save(self, *args, **kwargs):
        self.artifacttype_slug = slugify(self.artifacttype_name)
        super().save(*args, **kwargs)

#TODO: Signals for DjangoQ reciever that creates the hassums
#def artifact_created()

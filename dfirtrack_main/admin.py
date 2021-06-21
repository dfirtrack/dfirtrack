from django.contrib import admin
from dfirtrack_main.models import Analysisstatus
from dfirtrack_main.models import Analystmemo
from dfirtrack_main.models import Case
from dfirtrack_main.models import Casepriority
from dfirtrack_main.models import Casestatus
from dfirtrack_main.models import Casetype
from dfirtrack_main.models import Company
from dfirtrack_main.models import Contact
from dfirtrack_main.models import Division
from dfirtrack_main.models import Dnsname
from dfirtrack_main.models import Domain
from dfirtrack_main.models import Domainuser
from dfirtrack_main.models import Entry
from dfirtrack_main.models import Headline
from dfirtrack_main.models import Ip
from dfirtrack_main.models import Location
from dfirtrack_main.models import Note
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Os
from dfirtrack_main.models import Osarch
from dfirtrack_main.models import Osimportname
from dfirtrack_main.models import Reason
from dfirtrack_main.models import Recommendation
from dfirtrack_main.models import Reportitem
from dfirtrack_main.models import Serviceprovider
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Systemtype
from dfirtrack_main.models import Systemuser
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Task
from dfirtrack_main.models import Taskname

# all registered models will show up in admin app
admin.site.register(Analysisstatus)
admin.site.register(Analystmemo)
admin.site.register(Case)
admin.site.register(Casepriority)
admin.site.register(Casestatus)
admin.site.register(Casetype)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Division)
admin.site.register(Dnsname)
admin.site.register(Domain)
admin.site.register(Domainuser)
admin.site.register(Entry)
admin.site.register(Headline)
admin.site.register(Ip)
admin.site.register(Location)
admin.site.register(Note)
admin.site.register(Notestatus)
admin.site.register(Os)
admin.site.register(Osarch)
admin.site.register(Osimportname)
admin.site.register(Reason)
admin.site.register(Recommendation)
admin.site.register(Reportitem)
admin.site.register(Serviceprovider)
admin.site.register(System)
admin.site.register(Systemstatus)
admin.site.register(Systemtype)
admin.site.register(Systemuser)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Taskname)

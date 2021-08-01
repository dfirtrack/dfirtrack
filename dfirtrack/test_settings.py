"""
Test settings for DFIRTrack project.
"""

import logging
import sys

from dfirtrack.settings import Q_CLUSTER

# disable logging while testing (don't want the log file to be cluttered with test log entries, also don't want to see django-q logs while testing)
if len(sys.argv) > 1 and sys.argv[1] == "test":
    logging.disable(logging.CRITICAL)

# enable synchronous execution for django-q, async_task() won't work otherwise
Q_CLUSTER["sync"] = True

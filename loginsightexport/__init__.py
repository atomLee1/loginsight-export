#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VMware vRealize Log Insight Exporter
# Copyright © 2017 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an “AS IS” BASIS, without warranties or
# conditions of any kind, EITHER EXPRESS OR IMPLIED. See the License for the
# specific language governing permissions and limitations under the License.


__title__ = 'loginsightexport'
__build__ = None
__author__ = 'Alan Castonguay'
__license__ = 'Apache Software License 2.0'


try:
    from .__version__ import version as __version__
except ImportError:
    __version__ = "0.dev0"  # Mirrors setup.py. Should only be used if the package was installed from source.


USERAGENT = "LogInsightExport/" + __version__

# Set default logging handler to avoid "No handler found" warnings.
# import logging
# try:  # Python 2.7+
#    from logging import NullHandler
# except ImportError:
#    class NullHandler(logging.Handler):
#        def emit(self, record):
#            pass
#
# logging.getLogger(__name__).addHandler(NullHandler())

#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""General configuration for core Desktop features (authentication, etc)"""

from desktop.lib.conf import Config, ConfigSection, UnspecifiedConfigSection, coerce_bool
from desktop.lib.paths import get_desktop_root
import os
import socket

HTTP_HOST = Config(
  key="http_host",
  help="HTTP Host to bind to",
  type=str,
  default="0.0.0.0")
HTTP_PORT = Config(
  key="http_port",
  help="HTTP Port to bind to",
  type=int,
  default=8088)
SSL_CERTIFICATE = Config(
  key="ssl_certificate",
  help="Filename of SSL Certificate",
  default=None)
SSL_PRIVATE_KEY = Config(
  key="ssl_private_key",
  help="Filename of SSL RSA Private Key",
  default=None)
ENABLE_CHERRYPY_SERVER = Config(
  key="enable_cherrypy_server",
  help="If set to false, runcpserver will not actually start the web server.  Used if Apache is being used as a WSGI container.",
  type=coerce_bool,
  default=True)
CHERRYPY_SERVER_THREADS = Config(
  key="cherrypy_server_threads",
  help="Number of threads used by the CherryPy web server.",
  type=int,
  default=10)
SECRET_KEY = Config(
  key="secret_key",
  help="Used in hashing algorithms for sessions.",
  default="")

USER_ACCESS_HISTORY_SIZE = Config(
  key="user_access_history_size",
  help="Number of user access to remember per view per user.",
  type=int,
  default=10)

def is_https_enabled():
  return bool(SSL_CERTIFICATE.get() and SSL_PRIVATE_KEY.get())

#
# Email (SMTP) settings
#
_default_from_email = None
def default_from_email():
  """Email for hue@<host-fqdn>"""
  global _default_from_email
  if _default_from_email is None:
    try:
      fqdn = socket.getfqdn()
    except:
      fqdn = 'localhost'
    _default_from_email = "hue@" + fqdn
  return _default_from_email


SMTP = ConfigSection(
  key='smtp',
  help='Configuration options for connecting to an external SMTP server',
  members=dict(
    HOST = Config(
      key="host",
      help="The SMTP server for email notification delivery",
      type=str,
      default="localhost"
    ),

    PORT = Config(
      key="port",
      help="The SMTP server port",
      type=int,
      default=25
    ),

    USER = Config(
      key="user",
      help="The username for the SMTP host",
      type=str,
      default=""
    ),

    PASSWORD = Config(
      key="password",
      help="The password for the SMTP user",
      type=str,
      default=""
    ),

    USE_TLS = Config(
      key="tls",
      help="Whether to use a TLS (secure) connection when talking to the SMTP server",
      type=coerce_bool,
      default=False
    ),

    DEFAULT_FROM= Config(
      key="default_from_email",
      help="Default email address to use for various automated notification from Hue",
      type=str,
      dynamic_default=default_from_email
    ),
  )
)

DATABASE = ConfigSection(
  key='database',
  help="""Configuration options for specifying the Desktop Database.
          For more info, see http://docs.djangoproject.com/en/1.1/ref/settings/#database-engine""",
  members=dict(
    ENGINE=Config(
      key='engine',
      help='Database engine, eg postgresql, mysql, sqlite3, or oracle',
      type=str,
      default='sqlite3',
    ),
    NAME=Config(
      key='name',
      help='Database name, or path to DB if using sqlite3',
      type=str,
      default=get_desktop_root('desktop.db'),
    ),
    USER=Config(
      key='user',
      help='Database username',
      type=str,
      default='',
    ),
    PASSWORD=Config(
      key='password',
      help='Database password',
      type=str,
      default='',
    ),
    HOST=Config(
      key='host',
      help='Database host',
      type=str,
      default='',
    ),
    PORT=Config(
      key='port',
      help='Database port',
      type=int,
      default=0,
    ),
  )
)

# See python's documentation for time.tzset for valid values.
TIME_ZONE = Config(
  key="time_zone",
  help="Time zone name",
  type=str,
  default=os.environ.get("TZ", "America/Los_Angeles")
)

SERVER_USER = Config(
  key="server_user",
  help="Username to run servers as",
  type=str,
  default="hue")
SERVER_GROUP = Config(
  key="server_group",
  help="Group to run servers as",
  type=str,
  default="hue")


AUTH = ConfigSection(
  key="auth",
  help="Configuration options for user authentication into the web application",
  members=dict(
    BACKEND=Config("backend",
                   default="desktop.auth.backend.AllowFirstUserDjangoBackend",
                   help="Authentication backend.  Common settings are "
                        "django.contrib.auth.backends.ModelBackend (fully Django backend), " + 
                        "desktop.auth.backend.AllowAllBackend (allows everyone), " +
                        "desktop.auth.backend.AllowFirstUserDjangoBackend (relies on Django and user manager, after the first login), "),
    USER_AUGMENTOR=Config("user_augmentor",
                   default="desktop.auth.backend.DefaultUserAugmentor",
                   help="Class which defines extra accessor methods for User objects."),
))

LOCAL_FILESYSTEMS = UnspecifiedConfigSection(
  key="local_filesystems",
  help="Paths on the local file system that users should be able to browse",
  each=ConfigSection(
    members=dict(
      PATH=Config("path",
                  required=True,
                  help="The path on the local FS"))))

def default_feedback_url():
  """A version-specific URL."""
  return "http://groups.google.com/a/cloudera.org/group/hue-user"
  
FEEDBACK_URL = Config(
  key="feedback_url",
  help="Link for 'feedback' tab.",
  type=str,
  dynamic_default=default_feedback_url
)

DATABASE_LOGGING = Config(
  key="database_logging",
  help="If true, log all database requests.",
  type=coerce_bool,
  default=False)

DJANGO_DEBUG_MODE = Config(
  key="django_debug_mode",
  help="Enable or disable django debug mode.",
  type=coerce_bool,
  default=True
)

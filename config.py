from os import environ


_ = environ.get

COUCHDBURL = _("COUCHDBURL",'http://admin:iniadmin@13.250.43.79:5984/')
COUCHDB_DATABASE = _("COUCHDB_DATABASE","task_list_")
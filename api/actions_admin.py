# import csv
# import json
# from google.cloud import ndb
# from models import GameNight, Vote
# from .utils import *
# from .decorators import *
# from datetime import datetime, date
# import logging
#
#
# class DataImportPythonScriptHandler(webapp2.RequestHandler):
#     @require_admin
#     def get(self):
#         self.response.out.write("# FULL PYTHON SCRIPT: <br/>")
#         self.response.out.write("<br/>")
#
#         self.response.out.write("# IMPORTS: <br/>")
#         self.response.out.write("from models import * <br/>")
#         self.response.out.write("from datetime import datetime, date <br/>")
#         self.response.out.write("from google.cloud import ndb <br/>")
#         self.response.out.write("<br/>")
#
#         self.response.out.write("# CLEAR DB: <br/>")
#         self.response.out.write("ndb.delete_multi(User.query().fetch(keys_only=True)) <br/>")
#         self.response.out.write("ndb.delete_multi(GameNight.query().fetch(keys_only=True)) <br/>")
#         self.response.out.write("ndb.delete_multi(Vote.query().fetch(keys_only=True)) <br/>")
#
#         self.response.out.write("<br/>")
#         self.response.out.write("# Users: <br/>")
#         for obj in User.query().fetch():
#             self.response.out.write(self._get_data_dump_string_of_object(obj) + "<br><br>")
#
#         self.response.out.write("<br/>")
#         self.response.out.write("# GameNights: <br/>")
#         for obj in GameNight.query().fetch():
#             self.response.out.write(self._get_data_dump_string_of_object(obj) + "<br><br>")
#
#         self.response.out.write("<br/>")
#         self.response.out.write("# Votes: <br/>")
#         for obj in Vote.query().fetch():
#             self.response.out.write(self._get_data_dump_string_of_object(obj) + "<br><br>")
#
#         # Uncomment below to download as file, not really practical but keeping code
#         # self.response.headers['Content-Type'] = 'text/csv'
#         # self.response.headers['Content-Disposition'] = "attachment; filename=siage_import_script.py"
#
#     def _get_data_dump_string_of_object(self, obj):
#         data_string = "%s(id=%s, " % (type(obj).__name__, obj.id)
#         # __dict__['_values'] contains all class object variables
#         for variable_name in list(obj.__dict__["_values"].keys()):
#             variable_value = getattr(obj, variable_name, None)
#
#             if variable_value is None:
#                 data_string += "%s=None, " % variable_name
#             elif type(variable_value) is list:
#                 continue
#             elif type(variable_value) in (int, bool, float):
#                 data_string += "%s=%s, " % (variable_name, variable_value)
#             elif type(variable_value) is str:
#                 escaped_value = variable_value.replace("'", "\\'").replace('"', '\\"')
#                 data_string += "%s=u'%s', " % (variable_name, escaped_value)
#             elif type(variable_value) is date:
#                 data_string += "%s=date.fromtimestamp(%s), " % (
#                     variable_name,
#                     date_to_epoch(variable_value),
#                 )
#             elif type(variable_value) is datetime:
#                 data_string += "%s=datetime.fromtimestamp(%s), " % (
#                     variable_name,
#                     date_to_epoch(variable_value),
#                 )
#             elif type(variable_value) is ndb.Key:
#                 data_string += "%s=ndb.Key(%s, %s), " % (
#                     variable_name,
#                     variable_value.kind(),
#                     variable_value.id(),
#                 )
#             else:
#                 raise Exception("Type not handled: " + type(variable_value).__name__)
#
#         data_string = data_string[:-2]
#         data_string += ").put()"
#         return data_string
#
#
# class RunImportPythonScriptHandler(webapp2.RequestHandler):
#     @require_admin
#     def get(self):
#         # Paste generated script from DataImportPythonScript here and run it in dev
#         pass
#
#
# class RecalcluateGameNightSumsHandler(webapp2.RequestHandler):
#     @require_admin
#     def post(self):
#         [gn.calculate_and_save_sum() for gn in GameNight.query()]
#         ok_204(self.response)
#
#
# # class Migrate1Handler(webapp2.RequestHandler):
# #    @require_admin
# #    def get(self):
# #        for vote in Vote.query():
# #            vote.present = True
# #            vote.put()
# #        ok_204(self.response)
#
# # class Migrate2Handler(webapp2.RequestHandler):
# #    @require_admin
# #    def get(self):
# #        for vote in Vote.query():
# #            if 'date' in vote._properties:
# #                del vote._properties['date']
# #                vote.put()
# #        ok_204(self.response)
#
#
# app = webapp2.WSGIApplication(
#     [
#         (r"/api/actions/admin/dataimportpythonscript/", DataImportPythonScriptHandler),
#         (r"/api/actions/admin/runimportpythonscript/", RunImportPythonScriptHandler),
#         (r"/api/actions/admin/recalculategnsums/", RecalcluateGameNightSumsHandler),
#         # (r'/api/actions/admin/migrate/1', Migrate1Handler),
#         # (r'/api/actions/admin/migrate/2', Migrate2Handler),
#     ],
#     debug=True,
# )

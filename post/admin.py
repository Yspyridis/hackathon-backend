from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Coordinate, farms

from import_export import resources

class CoordinateImportExport(ImportExportModelAdmin):
#	pass
    class Meta:
        model = Coordinate

admin.site.register(Coordinate, CoordinateImportExport)
admin.site.register(farms)

from django.contrib import admin

from witness.models import (
    Editor,
    EditorAdmin,
    EditorProfile,
    Viewer,
    ViewerAdmin,
    ViewerProfile
)

admin.site.register(Editor, EditorAdmin)
admin.site.register(Viewer, ViewerAdmin)

admin.site.register(EditorProfile)
admin.site.register(ViewerProfile)

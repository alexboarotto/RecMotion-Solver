from . import panel
from . import generate_animation_op
from . import csv_select_ot
from . import set_cursor_op

bl_info = {
    "name": "CSV Rotations",
    "blender": (3, 0, 0),
    "category": "Object",
    "support": "COMMUNITY",
}

def register():
    panel.register()
    generate_animation_op.register()
    csv_select_ot.register()
    set_cursor_op.register()

def unregister():
    panel.unregister()
    generate_animation_op.unregister()
    csv_select_ot.unregister
    set_cursor_op.unregister()
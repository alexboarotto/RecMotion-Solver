import bpy
from bpy.types import Operator

from . data import Data

def apply_modifiers(obj):
    ctx = bpy.context.copy()
    ctx['object'] = obj
    for _, m in enumerate(obj.modifiers):
        try:
            ctx['modifier'] = m
            bpy.ops.object.modifier_apply(ctx, modifier=m.name)
        except RuntimeError:
            print(f"Error applying {m.name} to {obj.name}, removing it instead.")
            obj.modifiers.remove(m)

    for m in obj.modifiers:
        obj.modifiers.remove(m)

class SetCursorOP(Operator):
    """Set Cursor Location"""
    bl_idname = "csv_rotations.set_cursor"
    bl_label = "Set Cursor Location"

    cursor_pos: bpy.props.FloatVectorProperty(name="Cursor Position")

    def execute(self, context):
        apply_modifiers(Data.vehicle)
        Data.set_cursor(self.cursor_pos[0], self.cursor_pos[1], self.cursor_pos[2])
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SetCursorOP)

def unregister():
    bpy.utils.unregister_class(SetCursorOP)
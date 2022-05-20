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

class SetOriginOP(Operator):
    """Set Origin Location"""
    bl_idname = "csv_rotations.set_origin"
    bl_label = "Set Origin Location"


    def execute(self, context):
        if Data.vehicle is not None:
            apply_modifiers(Data.set_vehicle())
            Data.set_origin()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SetOriginOP)

def unregister():
    bpy.utils.unregister_class(SetOriginOP)
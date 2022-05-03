import bpy
from bpy.types import Operator

from .data import Data


# Operation to create new interaction zone of the specified type
class GenerateAnimationOP(Operator):
    """Generate Animation"""
    bl_idname = "csv_rotations.generate_animation"
    bl_label = "Generate Animation"

    @classmethod
    def poll(self, context):
        return Data.csv is not None

    def execute(self, context):
        Data.set_vehicle()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(GenerateAnimationOP)

def unregister():
    bpy.utils.unregister_class(GenerateAnimationOP)
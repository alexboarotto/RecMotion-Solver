import math
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
        bpy.context.active_object.animation_data_clear()
        Data.frame_interval = bpy.context.scene.frame_interval
        Data.rotation_multipliers = bpy.context.scene.rotation_multipliers
        Data.lock_axis = bpy.context.scene.lock_axis
        object = Data.set_vehicle()
        bpy.data.scenes[0].frame_end = len(Data.csv)*Data.frame_interval

        for index, elem in enumerate(reversed(Data.csv)):
            if not Data.lock_axis[0]:
                object.rotation_euler[1] = math.radians(elem["roll"]*Data.rotation_multipliers[0])
            if not Data.lock_axis[1]:
                object.rotation_euler[0] = math.radians(elem["pitch"]*Data.rotation_multipliers[1])
            if not Data.lock_axis[2]:
                object.rotation_euler[2] = math.radians(elem["yaw"]*Data.rotation_multipliers[2])
            object.keyframe_insert(data_path = "rotation_euler", frame = index*Data.frame_interval)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(GenerateAnimationOP)

def unregister():
    bpy.utils.unregister_class(GenerateAnimationOP)
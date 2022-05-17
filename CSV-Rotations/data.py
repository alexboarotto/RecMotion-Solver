import bpy


# Shared Data Accessor
class Data:
    csv = None
    vehicle = None

    frame_interval = 1
    initial_yaw = 0
    rotation_multipliers = []

    @classmethod
    def set_vehicle(self):
        vehicle = bpy.data.objects[bpy.context.scene.vehicle]
        return vehicle

    @classmethod
    def set_origin(self):
        bpy.context.view_layer.objects.active = self.vehicle
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

   
        
import bpy


# Shared Data Accessor
class Data:
    csv = None
    vehicle = None

    @classmethod
    def set_vehicle(self):
        vehicle = bpy.data.objects[bpy.context.scene.vehicle]
        return vehicle

   
        
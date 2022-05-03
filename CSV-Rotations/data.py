import bpy


# Shared Data Accessor
class Data:
    csv = None
    vehicle = None

    frame_interval = 1

    @classmethod
    def set_vehicle(self):
        vehicle = bpy.data.objects[bpy.context.scene.vehicle]
        return vehicle

    @classmethod
    def set_cursor(self, x, y, z):
        bpy.context.scene.cursor.location = (x, y, z)
        print(bpy.context.scene.cursor.location)

   
        
import bpy


# Shared Data Accessor
class Data:
    data = None
    csv = None
    vehicle = None

    frame_interval = 1
    fps = 24
    initial_yaw = 0
    rotation_multipliers = []
    lock_axis = []

    current_timecode = "00:00:00:00"

    @classmethod
    def set_vehicle(self):
        if not bpy.context.scene.vehicle == "":
            self.vehicle = bpy.data.objects[bpy.context.scene.vehicle]
            return self.vehicle

    @classmethod
    def set_origin(self):
        if self.vehicle is not None:
            bpy.context.view_layer.objects.active = self.vehicle
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    @classmethod
    def set_timecode(self, frame):
        index = round(frame/self.frame_interval)
        if self.csv is not None and index < len(self.csv):
            self.current_timecode = self.csv[index]["timecode"]

   
        
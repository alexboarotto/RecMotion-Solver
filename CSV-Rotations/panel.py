from email.policy import default
import bpy

from . data import Data


class CSVRotationsPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_csv_rotations"
    bl_label = ""
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="CSV Rotations")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("csv_rotations.import_csv", text = "Import CSV")

        layout.row()
        layout.row()

        layout.prop_search(scene, "vehicle", scene, "objects")

        layout.row()
        layout.row()

        layout.label(text="Apply all modifiers of vehicle and set origin to 3D cursor:")
        layout.operator("csv_rotations.set_origin", text = "Set Origin")

        col = layout.column()
        col.prop(scene, "rotation_multipliers", text = "Rotation Multipliers")

        layout.row()
        layout.row()
        layout.row()
        layout.prop(scene, "frame_interval", text = "Frame Interval")
        layout.operator("csv_rotations.generate_animation", text="Generate Animation")


def register():
    bpy.utils.register_class(CSVRotationsPanel)
    bpy.types.Scene.vehicle = bpy.props.StringProperty()
    bpy.types.Scene.frame_interval = bpy.props.IntProperty(default = 1, min = 1)
    bpy.types.Scene.rotation_multipliers = bpy.props.FloatVectorProperty(default = (1.0, 1.0, 1.0), min = -2.0, max = 2.0, subtype = 'XYZ')

def unregister():
    bpy.utils.unregister_class(CSVRotationsPanel)
    del bpy.types.Scene.vehicle
    del bpy.types.Scene.frame_interval
    del bpy.types.Scene.rotation_multipliers
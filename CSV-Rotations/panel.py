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

        layout.prop(scene, "cursor_pos", text = "Cursor Location")
        layout.operator("csv_rotations.set_cursor", text = "Set Cursor")

        if not Data.csv == None:
            layout.row()
            layout.row()
            layout.row()
            layout.prop(scene, "frame_interval", text = "Frame Interval")
            layout.operator("csv_rotations.generate_animation", text="Generate Animation")


def register():
    bpy.utils.register_class(CSVRotationsPanel)
    bpy.types.Scene.vehicle = bpy.props.StringProperty()
    bpy.types.Scene.cursor_pos = bpy.props.FloatVectorProperty()
    bpy.types.Scene.frame_interval = bpy.props.IntProperty(default = 1, min = 1)

def unregister():
    bpy.utils.unregister_class(CSVRotationsPanel)
    del bpy.types.Object.vehicle
    del bpy.types.Scene.cursor_pos
    del bpy.types.Scene.frame_interval
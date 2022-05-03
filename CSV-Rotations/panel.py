import bpy

from . data import Data


class CSVROtationsPanel(bpy.types.Panel):
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
        layout.operator("csv_rotations.import_csv", text = "Import CSV")

        row = layout.row()
        row.operator("csv_rotations.generate_animation", text="Generate Animation")


def register():
    bpy.utils.register_class(CSVROtationsPanel)

def unregister():
    bpy.utils.unregister_class(CSVROtationsPanel)
import bpy
import blf
from bpy.app.handlers import persistent

from . data import Data
    
def drawing_list():
    font_id = 0
    blf.size(font_id, 20, 72)
    blf.position(font_id, 30, 30, 0)
    blf.draw(font_id, Data.current_timecode)

@persistent
def load_handler(context):
    bpy.ops.csv_rotations.display_timecode('INVOKE_DEFAULT')
            
class DisplayTimecodeOP(bpy.types.Operator):
    bl_idname = "csv_rotations.display_timecode"
    bl_label = "Display Timecode"

    def __init__(self):
        self.draw_handle = None
        self.draw_event = None
        self.widgets = []

    def draw_callback_px(self, op, context):
        drawing_list()

    def modal(self, context, event):
        if context.area:
            context.area.tag_redraw()

        Data.set_timecode(bpy.data.scenes[0].frame_current)

        if event.type == "ESC":
            self.unregister_handlers(self, context)
            return {"CANCELLED"}
        
        return {'PASS_THROUGH'}
    
    def invoke(self, context, event):
        args = (self, context)
        self.register_handlers(args, context)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def register_handlers(self, args, context):
        self.draw_handle = bpy.types.SpaceView3D.draw_handler_add(self.draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
        self.draw_event = context.window_manager.event_timer_add(0.1, window = context.window) 

    def unregister_handlers(self, args, context):
        bpy.types.SpaceView3D.draw_handler_remove(self.draw_handle, 'WINDOW')
        context.window_manager.event_timer_remove(self.draw_event)
        self.draw_handle = None
        self.draw_event = None
        
addon_keymaps = []

def register():
    bpy.utils.register_class(DisplayTimecodeOP)
    bpy.app.handlers.load_post.append(load_handler)
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new("csv_rotations.display_timecode", 'F', 'PRESS', shift = True, ctrl = True)
        addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(DisplayTimecodeOP)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    


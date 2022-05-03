import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty

from . data import Data


class ImportCSV_OT(Operator, ImportHelper):
    """Import CSV"""
    bl_idname = 'csv_rotations.import_csv'
    bl_label = 'import csv'
 
    filename_ext = '.txt'
    
    filter_glob: StringProperty(
        default='*.txt;*.csv',
        options={'HIDDEN'}
    )
 
    def execute(self, context):
        print('imported file: ', self.filepath)
        Data.csv = 1
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportCSV_OT)

def unregister():
    bpy.utils.unregister_class(ImportCSV_OT)
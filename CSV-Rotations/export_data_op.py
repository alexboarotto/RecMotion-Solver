import enum
import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator
from bpy.props import StringProperty
import csv

from . data import Data

# Load and return json file
def load_data(path):
    with open(path, mode='w') as csv_file:
        spamwriter = csv.writer(csv_file)

        first_row = Data.data[0]
        
        for i in range(0,6):
            first_row.append("axis"+str(i))

        spamwriter.writerow(first_row)


class ExportCSV_OT(Operator, ExportHelper):
    """Export CSV"""
    bl_idname = 'csv_rotations.export_csv'
    bl_label = 'export csv'
 
    filename_ext = '.csv'
    
    filter_glob: StringProperty(
        default='*.csv',
        options={'HIDDEN'}
    )
 
    def execute(self, context):
        try:
            load_data(self.filepath)
            error = None
        except Exception as err:
            error = err.args[0]
        if error is not None:
            self.report({'ERROR'}, str(error))
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExportCSV_OT)

def unregister():
    bpy.utils.unregister_class(ExportCSV_OT)
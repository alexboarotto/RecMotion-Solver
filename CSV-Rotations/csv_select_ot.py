import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty

from . data import Data

# Load and return json file
def load_data(path):
    file = open(path, mode='r')
    data = file.readlines()
    file.close()

    roll_index = None
    pitch_index = None
    yaw_index = None

    for index, elem in enumerate(data[0].split(",")):
        if elem.strip() == "Roll":
            roll_index = index
        if elem.strip() == "Pitch":
            pitch_index = index
        if elem.strip() == "Yaw":
            yaw_index = index
    
    data.pop(0)

    rotations = []

    for i in data:
        rotation = []
        list = i.split(",")
        rotation.append(list[roll_index])
        rotation.append(list[pitch_index])
        rotation.append(list[yaw_index])
        rotations.append(rotation)
    

    return rotations


class ImportCSV_OT(Operator, ImportHelper):
    """Import CSV"""
    bl_idname = 'csv_rotations.import_csv'
    bl_label = 'import csv'
 
    filename_ext = '.txt'
    
    filter_glob: StringProperty(
        default='*.txt',
        options={'HIDDEN'}
    )
 
    def execute(self, context):
        try:
            Data.csv = load_data(self.filepath)
            error = None
        except Exception as err:
            error = err.args[0]
        if error is not None:
            self.report({'ERROR'}, error)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportCSV_OT)

def unregister():
    bpy.utils.unregister_class(ImportCSV_OT)
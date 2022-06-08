import enum
import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty
import csv

from . data import Data

# Load and return json file
def load_data(path):
    with open(path, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        
        data = []

        for i in reader:
            data.append(i)

        roll_index = None
        pitch_index = None
        yaw_index = None

        for index, elem in enumerate(data[0]):
            if elem == "roll":
                roll_index = index
            if elem == "pitch":
                pitch_index = index
            if elem == "yaw":
                yaw_index = index

        rotations = []

        data.pop(0)

        Data.initial_yaw = data[0][yaw_index]


        for i in data:
            rotation = {
                "roll": 0,
                "pitch": 0,
                "yaw": 0,
                "timecode": ""
            }
            rotation["roll"] = float(i[roll_index])
            rotation["pitch"] = float(i[pitch_index])
            rotation["yaw"] = float(i[yaw_index])-float(Data.initial_yaw)
            rotation["timecode"] = i[0]
            rotations.append(rotation)
        

        return rotations


class ImportCSV_OT(Operator, ImportHelper):
    """Import CSV"""
    bl_idname = 'csv_rotations.import_csv'
    bl_label = 'import csv'
 
    filename_ext = '.csv'
    
    filter_glob: StringProperty(
        default='*.csv',
        options={'HIDDEN'}
    )
 
    def execute(self, context):
        try:
            Data.csv = load_data(self.filepath)
            error = None
        except Exception as err:
            error = err.args[0]
        if error is not None:
            self.report({'ERROR'}, str(error))
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportCSV_OT)

def unregister():
    bpy.utils.unregister_class(ImportCSV_OT)
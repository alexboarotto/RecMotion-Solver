import enum
import math
import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator
from bpy.props import StringProperty
import csv

from . data import Data

yellow_distances = []
green_distances = []
light_blue_distances = []
blue_distances = []
red_distances = []
orange_distances = []

axis = ['yellow', 'green', 'light_blue', 'blue', 'red', 'orange']

# Load and return json file
def load_data(path):
    with open(path, mode='w') as csv_file:
        spamwriter = csv.writer(csv_file)

        first_row = Data.data[0]

        for i in range(0,6):
            first_row.append("axis_"+str(axis[i]))

        spamwriter.writerow(first_row)

        for i in range(1, len(Data.data)):
            Data.data[i].append(yellow_distances[i-1])
            Data.data[i].append(green_distances[i-1])
            Data.data[i].append(light_blue_distances[i-1])
            Data.data[i].append(blue_distances[i-1])
            Data.data[i].append(red_distances[i-1])
            Data.data[i].append(orange_distances[i-1])

            spamwriter.writerow(Data.data[i])

def get_min_y(obj):
    vertices = [v.co for v in obj.data.vertices]

    min_y = vertices[0]

    for i in vertices:
        if i[1]<min_y[1]:
            min_y = i
    
    return obj.matrix_world @ min_y

def get_min_x(obj):
    vertices = [v.co for v in obj.data.vertices]

    min_x = vertices[0]

    for i in vertices:
        if i[0]<min_x[0]:
            min_x = i
    
    return obj.matrix_world @ min_x

def get_distance(piston, cylinder):
    p_vert = get_min_y(piston)
    c_vert = get_min_x(cylinder)
    return math.dist(c_vert, p_vert)


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
        Data.axis_ext = bpy.context.scene.max_extension

        # OBJECT NAMES
        yellow = ["Body_1_5", "Body_2_16"]
        green = ["Body_1_4", "Body_2_17"]
        light_blue = ["Body_1_3", "Body_2_18"]
        blue = ["Body_1_6", "Body_2_19"]
        red = ["Body_1_8", "Body_2_20"]
        orange = ["Body_1_7", "Body_2_15"]

        #Handle to objects
        #============================================================
        yellow_piston = bpy.data.objects[yellow[1]]
        yellow_cylinder = bpy.data.objects[yellow[0]]

        green_piston = bpy.data.objects[green[1]]
        green_cylinder = bpy.data.objects[green[0]]

        light_blue_piston = bpy.data.objects[light_blue[1]]
        light_blue_cylinder = bpy.data.objects[light_blue[0]]

        blue_piston = bpy.data.objects[blue[1]]
        blue_cylinder = bpy.data.objects[blue[0]]

        blue_piston = bpy.data.objects[blue[1]]
        blue_cylinder = bpy.data.objects[blue[0]]

        red_piston = bpy.data.objects[red[1]]
        red_cylinder = bpy.data.objects[red[0]]

        orange_piston = bpy.data.objects[orange[1]]
        orange_cylinder = bpy.data.objects[orange[0]]
        #============================================================

        for frame in range(0, bpy.data.scenes[0].frame_end, Data.frame_interval):

            bpy.context.scene.frame_set(frame)

            yellow_distances.append(int(get_distance(yellow_piston, yellow_cylinder)*1000))
            green_distances.append(int(get_distance(green_piston, green_cylinder)*1000))
            light_blue_distances.append(int(get_distance(light_blue_piston, light_blue_cylinder)*1000))
            blue_distances.append(int(get_distance(blue_piston, blue_cylinder)*1000))
            red_distances.append(int(get_distance(red_piston, red_cylinder)*1000))
            orange_distances.append(int(get_distance(orange_piston, orange_cylinder)*1000))

        Data.check_extension(yellow_distances)
        Data.check_extension(green_distances)
        Data.check_extension(light_blue_distances)
        Data.check_extension(blue_distances)
        Data.check_extension(red_distances)
        Data.check_extension(orange_distances)

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
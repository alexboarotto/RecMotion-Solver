# CSV-blender-rotations
Addon that reads rotation data from a csv file and creates an animation rotating a specific object

## Installation
Download this repo as a zip file clicking on Code > Download ZIP
![image](https://user-images.githubusercontent.com/59767130/166458698-16596287-9647-4719-b024-bbec422f9175.png)

Copy the *CSV-Rotations* folder into your Blender *"addons"* directory (In Windows it's usually C:\Program Files\Blender Foundation\Blender 3.0\3.0\scripts\addons)
To find the Blender directory on your system check out: https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html

In Blender, go to Edit > Preferences > Add-Ons and search for *"Object: CSV Rotations"*

![image](https://user-images.githubusercontent.com/59767130/166459127-ed6723f7-c29c-4661-9cbd-6c4031de744f.png)

Activate it by clicking on the checkbox

## UI
In the properties panel open the scene tab. There you will find a Header called *"CSV Rotations"*. Click on it to see the plugin's UI.

![image](https://user-images.githubusercontent.com/59767130/166459851-4ed30bc4-a7b1-4ef7-828a-4738e07f56ac.png)

![image](https://user-images.githubusercontent.com/59767130/166460288-1b3d8c6c-101b-456a-ae36-8c6234021678.png)

The _Import CSV_ button will open a file browser where you will be able to select the .txt file containing the rotation data.
The _Vehicle_ input will allow you to select the object in the scene that you would like to be animated. You can drag and drop objects from the outliner or just click and select objects directly in here
The _Set Origin_ button will apply all modifiers on the current object selected as the vehicle as well as set the objects origin to the 3D Cursor's location.

Once you've imported the .txt file 2 more fields will appear at the bottom of the plugin's UI

![image](https://user-images.githubusercontent.com/59767130/166461062-932fafba-5f51-47de-be1c-6570e373e12a.png)

The _Frame Interval_ field will allow you to input how many frames you would like there to be between each value read from the csv.
The _Generate Animation_ button will create a keyframe each *Frame Interval* frames with the rotational data

## Moving 3D Cursor
In the top-right side of the viewport click on the little arrow hanging from the side to open the additional tools. (Shortcut: *N*)

![image](https://user-images.githubusercontent.com/59767130/166462224-03232adc-5d55-4ca4-9ce9-2b655e6a819b.png)

Navigate to the view tab and there you can find the input fields to edit the location value of the 3D cursor. (You can click and drag over the fields to use them as a slider)

![image](https://user-images.githubusercontent.com/59767130/166462546-fb924f99-7a1d-4928-ad41-d08be5b0fd9a.png)




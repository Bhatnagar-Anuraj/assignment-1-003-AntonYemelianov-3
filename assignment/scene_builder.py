"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
#I changed the building's position to fit the rest of my scene, hope that's ok.
building_width = 4
building_height = 6
building_depth = 4
building_x = -20
building_z = -10

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
BigTreeHeight = 10
BigTreeRadius = 3
BigTreeXPosition = 8
BigTreeZPosition = 5
#These variables define the various parameters of the big tree. Variables are used so that the parameters can be easily changed in the future if needed.
#I chose to use a cone for a pine tree, which has a height and a radius
BigTree=cmds.polyCone(
name="BigTree",
radius=BigTreeRadius,
height=BigTreeHeight
 )
cmds.move(BigTreeXposition, BigTreeHeight/2.0, BigTreeZPosition, BigTree)
#Here, the variables are used to indicate the big tree's size and position. 
#Since all objects appear at world center, halfway under the ground plane, they can be raised above it by using their height/2 as the y position.
# ---------------------------------------------------------------------------
# TODO: Add Object 3
# ---------------------------------------------------------------------------
#I added another, smaller pine tree, which is also a cone, and is created similarly to the big tree using variables.
SmallTreeHeight = 5
SmallTreeRadius = 2
SmallTreeXPosition = -5
SmallTreeZPosition = -3
SmallTree=cmds.polyCone(
name="SmallTree",
radius=SmallTreeRadius,
height=SmallTreeHeight
 )
cmds.move(SmallTreeXposition, SmallTreeHeight/2.0, SmallTreeZPosition, SmallTree)
#Basically, everything is the same as for the big tree, just with different numbers.
# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------
#I then added a person to the scene. The character consists of a rectangle for the body and a sphere for the head.
#I started with the body, creating a rectangle/irregular cube
PersonBodyHeight = 2
PersonBodyWidth = 1
PersonBodyDepth = 1
PersonBodyXPosition=3
PersonBodyZPosition=2
PersonBody=cmds.polyCube(
    name="PersonBody",
    height=PersonBodyHeight,
width=PersonBodyWidth,
depth=PersonBodyDepth
)
cmds.move(PersonBodyXPosition, PersonBodyHeight/2.0, PersonBodyZPosition, PersonBody)
#The person would be walking between the two trees towards the building
# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------
PersonHeadRadius = 0.5
PersonHead=cmds.polySphere(
    name="PersonHead",
    radius=PersonHeadRadius
)
cmds.move(PersonBodyXPosition, PersonBodyHeight+PersonHeadRadius, PersonBodyZPosition, PersonHead)
#I added the person's head, which is a sphere. Since it would sit right on top of the body, it would use the body's x and y position.
#I made the head's width/diameter the same as the body's, which is 1, so the radius needed to be 0.5, half the diameter.
#The head would go right on top of the body so I raised it to the body's height.
#But this is not enough since the head is also created halfway under the ground plane like all objects
#So it needed to be raised an additional half of its diameter or, in other words, its radius, making its final y position the body's height+the head's radius.
# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------
#Finally, I went back to the building because it did not look like an actual house being just a box. I decided to add a roof to make it more recognizable.
#The roof would be a pyramid, which has side length and a number of sides as its parameters.
RoofSideLength = 6
RoofSides = 4
Roof=cmds.polyPyramid(
    name="Roof",
    sideLength=RoofSideLength,
numberOfSides= RoofSides
)
cmds.scale(1,0.25,1, Roof)
#There is no height parameter for pyramids. The height is the same as side length. I wanted it to be 1 unit tall so I scaled it by 0.25 or 1/4 vertically.
cmds.rotate (0,45,0,Roof)
#Also, the pyramid gets created rotated by 45 degrees with the world axis facing its angles rather than sides like other figures. 
#I solved the problem by rotating it back.
cmds.move(building_x, building_height+RoofHeight/2.0, building_z, Roof)
#Similarly to the head being on top of the body, the roof goes on top of the building+half of he pyramid's height to compensate for it being created halfway under the ground plane.
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")

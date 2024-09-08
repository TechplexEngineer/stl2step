import FreeCAD
import Mesh
import Part
import sys
import os

# Read command line arguments
if len(sys.argv) == 1 +2:
    stl_file = sys.argv[1 +1]
    step_file = os.path.splitext(stl_file)[0] + ".step"
elif len(sys.argv) == 2 +2:
    stl_file = sys.argv[1 +1]
    step_file = sys.argv[2 +1]
else:
    print("Please provide STL and STEP file paths as command line arguments.")
    sys.exit(1)

if (os.path.isdir(step_file)):
    step_file = os.path.join(step_file, os.path.splitext(os.path.basename(stl_file))[0] + ".step")

print("Converting STL to STEP...")
print("STL file:", stl_file)
print("STEP file:", step_file)

print("->>>Mesh.open")
Mesh.open(stl_file)
print("Mesh.open done")
print()

doc = FreeCAD.activeDocument()
meshObj = doc.ActiveObject

print("Begin command Part_ShapeFromMesh")
partShape = Part.Shape()
partShape.makeShapeFromMesh(meshObj.Mesh.Topology, 0.001, True)

partObj = doc.addObject('Part::Feature')
partObj.Shape = partShape
partObj.purgeTouched()
print("End command Part_ShapeFromMesh")
print()


print("Begin command Part_RefineShape")
refinedObj = doc.addObject('Part::Refine')
refinedObj.Source = partObj
doc.recompute()
print("End command Part_RefineShape")
print()


print("Begin command Part_MakeSolid")
solidObj= FreeCAD.ActiveDocument.addObject("Part::Feature")
solidObj.Shape = Part.Solid(refinedObj.Shape)
print("End command Part_MakeSolid")
print()


print("Begin command Std_Export")
Part.export([solidObj], step_file)
print("End command Std_Export")

print("Done!")
print(step_file)

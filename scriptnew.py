import FreeCAD
import Mesh
import Part

print("Converting STL to STEP...")
stl_file = "/home/techplex/projects/pers/stl2step/in/Half_Inch_Hex_Bridgeport_Adapter.stl"
step_file = "/home/techplex/projects/pers/stl2step/out/Half_Inch_Hex_Bridgeport_Adapter.step"

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
print("Done!")

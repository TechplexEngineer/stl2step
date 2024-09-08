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
meshObj = doc.getObject('Half_Inch_Hex_Bridgeport_Adapter')

print("Begin command Part_ShapeFromMesh")
partShape = Part.Shape()
partShape.makeShapeFromMesh(meshObj.Mesh.Topology, 0.001, True)

partObj = doc.addObject('Part::Feature', 'Half_Inch_Hex_Bridgeport_Adapter001')
partObj.Shape = partShape
partObj.purgeTouched()
del partShape
print("End command Part_ShapeFromMesh")
print()

print("Begin command Part_RefineShape")
doc.addObject('Part::Refine','Half_Inch_Hex_Bridgeport_Adapter_refined')
doc.ActiveObject.Source = doc.getObject('Half_Inch_Hex_Bridgeport_Adapter001')
doc.ActiveObject.Label = doc.getObject('Half_Inch_Hex_Bridgeport_Adapter001').Label
doc.getObject('Half_Inch_Hex_Bridgeport_Adapter001').Visibility = False
doc.recompute()
print("End command Part_RefineShape")
print()


print('object list')
for obj in FreeCAD.ActiveDocument.Objects:
    if hasattr(obj,"Shape"):
        print(obj.Name)
print()

print("Begin command Part_MakeSolid")
__s__=doc.getObject('Half_Inch_Hex_Bridgeport_Adapter_refined').Shape
__s__=Part.Solid(__s__)
__o__=FreeCAD.ActiveDocument.addObject("Part::Feature","Half_Inch_Hex_Bridgeport_Adapter002_solid")
__o__.Label="Half_Inch_Hex_Bridgeport_Adapter002 (Solid)"
__o__.Shape=__s__
del __s__, __o__
print("End command Part_MakeSolid")
print()



print("Begin command Std_Export")
__objs__ = []
__objs__.append(doc.getObject("Half_Inch_Hex_Bridgeport_Adapter002_solid"))

Part.export(__objs__,step_file)

print("Done!")

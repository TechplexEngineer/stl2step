import FreeCAD
import Mesh
import Part

print("Converting STL to STEP...")
stl_file = "/home/techplex/projects/pers/stl2step/in/Half_Inch_Hex_Bridgeport_Adapter.stl"
step_file = "/home/techplex/projects/pers/stl2step/out/Half_Inch_Hex_Bridgeport_Adapter.step"

print("->>>>>> Mesh.open")
Mesh.open(stl_file)
print("Mesh.open done")
print()

print("Begin command Part_ShapeFromMesh")
print(1)
FreeCAD.getDocument('Unnamed').addObject('Part::Feature', 'Half_Inch_Hex_Bridgeport_Adapter001')
print(2)
__shape__ = Part.Shape()
print(3)
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter').Mesh.Topology, 0.010000, True)
print(4)
FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').Shape = __shape__
print(5)
FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').purgeTouched()
print(6)
del __shape__
print("End command Part_ShapeFromMesh")
print()


# print("Begin command Part_RefineShape")
# FreeCAD.getDocument('Unnamed').addObject('Part::Refine','Half_Inch_Hex_Bridgeport_Adapter001')
# FreeCAD.getDocument('Unnamed').ActiveObject.Source = FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001')
# FreeCAD.getDocument('Unnamed').ActiveObject.Label = FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').Label
# FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').Visibility = False
# # FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.ShapeAppearance=getattr(FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').getLinkedObject(True).ViewObject,'ShapeAppearance',FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.ShapeAppearance)
# # FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.LineColor=getattr(FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').getLinkedObject(True).ViewObject,'LineColor',FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.LineColor)
# # FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.PointColor=getattr(FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').getLinkedObject(True).ViewObject,'PointColor',FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter002').ViewObject.PointColor)
# a = FreeCAD.ActiveDocument.recompute()
# print(a)
# print("End command Part_RefineShape")
# print()



print("Begin command Part_MakeSolid")
__s__=FreeCAD.getDocument('Unnamed').getObject('Half_Inch_Hex_Bridgeport_Adapter001').Shape
__s__=Part.Solid(__s__)
__o__=FreeCAD.ActiveDocument.addObject("Part::Feature","Half_Inch_Hex_Bridgeport_Adapter002_solid")
__o__.Label="Half_Inch_Hex_Bridgeport_Adapter002 (Solid)"
__o__.Shape=__s__
del __s__, __o__
print("End command Part_MakeSolid")
print()

# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Half_Inch_Hex_Bridgeport_Adapter002_solid')

print("Begin command Std_Export")
### Begin command Std_Export
__objs__ = []
__objs__.append(FreeCAD.getDocument("Unnamed").getObject("Half_Inch_Hex_Bridgeport_Adapter002_solid"))

Part.export(__objs__,step_file)
# import ImportGui

# ImportGui.export(__objs__, u"/home/techplex/projects/pers/stl2step/out/Unnamed-Half_Inch_Hex_Bridgeport_Adapter002 (Solid).step")

del __objs__
### End command Std_Export

from Autodesk.Revit.DB import FilteredElementCollector as fec
from Autodesk.Revit.DB import BuiltInCategory as bic
from Autodesk.Revit.DB import BuiltInParameter as bip
from Autodesk.Revit.DB import Transaction

doc = __revit__.ActiveUIDocument.Document
t = Transaction(doc, 'title')

rooms = fec(doc).OfCategory(bic.OST_Rooms).WhereElementIsNotElementType().ToElements()
print len(rooms), "Rooms"

dict = {}
for room in rooms:
	room_id = room.Id
	room_area = room.Area
	dict[room_id] = room.Area
print dict 

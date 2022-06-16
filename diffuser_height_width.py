    
from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import BuiltInCategory
from Autodesk.Revit.DB import Family, FamilySymbol, ElementId, Category
#from Autodesk.Revit.DB.Category import GetCategory
#from System.Collections.Generic import List
import Autodesk.Revit.DB as DB

fec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctTerminal).ToElements()

for element in fec:
	diffuserHeight=element.LookupParameter("Diffuser Height").AsValueString()
	diffuserWidth=element.LookupParameter("Diffuser Width").AsValueString()
	h_w = "{0} x {1}".format((int(diffuserHeight)/25), int(diffuserWidth)/25)
	print(h_w)

	#Prints diffuser's height and width

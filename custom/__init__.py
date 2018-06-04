# AGR-FBX Export Script by Darkhand
# https://www.youtube.com/user/Darkhandrob
# https://twitter.com/Darkhandrob
# Last change: 04.06.2018
bl_info = {
	"name": "CSGO AGR Importer-Exporter",
	"category": "Import-Export",
	"author": "Darkhand",
	"version": (1, 0, 0),
	"blender": (2, 79, 0),
	"description": "Imports AGR and exports every object as a FBX",
	"location": "File > Import/Export"
	}

import bpy

from . import Agr_Import_Export_FBX, Agr_Export_FBX

def menu_draw_import(self, context):
	self.layout.operator("custom.import_agr_to_fbx", text="AGR Import and Export FBX")
	
def menu_draw_export(self, context):
	self.layout.operator("custom.agr_to_fbx", text="AGR Export FBX")

def register():
	bpy.utils.register_class(Agr_Import_Export_FBX.ImpExportAgr)
	bpy.types.INFO_MT_file_import.append(menu_draw_import)
	bpy.utils.register_class(Agr_Export_FBX.ExportAgr)
	bpy.types.INFO_MT_file_export.append(menu_draw_export)
	
def unregister():
	bpy.types.INFO_MT_file_import.remove(menu_draw_import)
	bpy.utils.unregister_class(Agr_Import_Export_FBX.ImpExportAgr)
	bpy.types.INFO_MT_file_export.remove(menu_draw_export)
	bpy.utils.unregister_class(Agr_Export_FBX.ExportAgr)
	
if __name__ == "__main__":
	unregister()
	register()
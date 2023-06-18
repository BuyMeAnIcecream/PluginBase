import unreal

#create new menu option
menus = unreal.ToolMenus.get()
main_menu = menus.find_menu("LevelEditor.MainMenu")
custom_menu = main_menu.add_sub_menu("Custom Menu", "Python Automation", "Menu Name", "Menu Label")
menus.refresh_all_widgets()


#define a script to call on menu option clicked
@unreal.uclass() 
class MyScriptObject(unreal.ToolMenuEntryScript):
	@unreal.ufunction(override=True)
	def execute(self, context):
		print("Script executed!")
	
#Expanding existing menu

#find tools menu first
tools_menu = menus.find_menu("LevelEditor.MainMenu.Tools")

#create script obj
script_object = MyScriptObject()
script_object.init_entry(
	owner_name=tools_menu.menu_name,
	menu=tools_menu.menu_name,
	section="Tools",
	name="My Python Injection",
	label="My Python Injection",
	tool_tip="Custom Script Entry"
)

#register entry
script_object.register_menu_entry()

#Expanding context menu
asset_context_menu = menus.find_menu("ContentBrowser.AssetContextMenu.StaticMesh")
script_object2 = MyScriptObject()
script_object2.init_entry(
	owner_name=asset_context_menu.menu_name,
	menu=asset_context_menu.menu_name,
	section="GetAssetActions",
	name="My Python Injection",
	label="My Python Injection",
	tool_tip="Custom Script Entry"
)

#register entry
script_object2.register_menu_entry()

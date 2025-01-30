if "bpy" in locals():
    import importlib
    importlib.reload(mesh)
    importlib.reload(util)
else:
    from . import mesh
    from . import util


import bpy


class OBJECT_OT_pineapple(bpy.types.Operator):
    """Construct a pineapple mesh."""
    bl_idname = "mesh.primitive_pineapple_add"
    bl_label = "Pineapple"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        util.deselect_all()
        
        mesh_data = util.construct_data("pineapple", mesh.VERTS, mesh.EDGES, mesh.FACES)
        mesh_obj = util.construct_mesh("Pineapple", mesh_data)

        util.select_mesh(mesh_obj)
        util.recalc_normals()
        
        return { 'FINISHED' }


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_pineapple.bl_idname, icon='MESH_CUBE')


def register():
    bpy.utils.register_class(OBJECT_OT_pineapple)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_pineapple)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __package__ == "__main__":
    register()

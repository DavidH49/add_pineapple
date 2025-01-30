if "bpy" in locals():
    import importlib
    importlib.reload(mesh)
    importlib.reload(util)
else:
    from . import mesh
    from . import util


import bpy


class OBJECT_OT_pineapple(bpy.types.Operator):
    """Add a pineapple"""
    bl_idname = "mesh.pineapple"
    bl_label = "Pineapple"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        util.deselect_all()
        
        mesh_data = bpy.data.meshes.new("pineapple")
        mesh_data.from_pydata(mesh.VERTS, mesh.EDGES, mesh.FACES)
        mesh_obj = bpy.data.objects.new("Pineapple", mesh_data)
        
        bpy.context.collection.objects.link(mesh_obj)
        bpy.context.view_layer.objects.active = mesh_obj
        
        mesh_obj.select_set(True)
        mesh_obj.matrix_world = bpy.context.scene.cursor.matrix

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

import bpy


def construct_data(name, verts, edges, faces):
    mesh_data = bpy.data.meshes.new(name)
    mesh_data.from_pydata(verts, edges, faces)

    return mesh_data


def construct_mesh(name, data):
    mesh_obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(mesh_obj)
    bpy.context.view_layer.objects.active = mesh_obj

    return mesh_obj


def select_mesh(obj):
    obj.select_set(True)
    obj.matrix_world = bpy.context.scene.cursor.matrix


def deselect_all():
    for o in bpy.context.selected_objects:
        o.select_set(False)


def recalc_normals():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()
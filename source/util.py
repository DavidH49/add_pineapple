import bpy


def deselect_all():
    for o in bpy.context.selected_objects:
        o.select_set(False)


def recalc_normals():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()
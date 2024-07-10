import maya.cmds as cmds


def createControl(joint):
    # Create a NURBS curve (control) at the joint's position.
    # select and query joints position first
    joint_position = cmds.xform(joint, query=True, translation=True, worldSpace=True)
    print(joint_position)

    # create nurbs circle next and set translation as the joints
    control = cmds.circle()
    cmds.xform(control, translation=joint_position, worldSpace=True)

    # Create an empty group (parent group) at the joint's position.
    group = cmds.group(empty=True)
    cmds.xform(group, translation=joint_position, worldSpace=True)
    # Parent the control under the parent group.
    cmds.parent(control, group)
    # Rename the control and parent group according to established naming conventions
    cmds.rename(control, joint + '_ctrl')
    cmds.rename(group, '_grp')

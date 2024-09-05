import maya.cmds as cmds

selected_joints = cmds.ls(selection=True, type='joint')


def createControl(joint):
    if not selected_joints:
        cmds.warning("Please select a joint.")
        return

    # split joint name into two
    prefix, suffix = joint.rsplit('_', 1)

    # create control name
    control_name = prefix + '_ctrl'

    # Query translation and rotation separately
    joint_position = cmds.xform(joint, query=True, translation=True, worldSpace=True)
    joint_rotation = cmds.xform(joint, query=True, rotation=True, worldSpace=True)

    # Ensure rotation values are valid
    if not joint_position or not joint_rotation:
        cmds.warning("Error querying position or rotation for {joint}. Skipping.")
        return

    # Create control
    control = cmds.circle(name=control_name)[0]  # Get the actual control shape
    cmds.xform(control, translation=joint_position, rotation=joint_rotation, worldSpace=True)

    # Create group and position it
    group = cmds.group(empty=True, name=control_name + "_grp")
    cmds.xform(group, translation=joint_position, rotation=joint_rotation, worldSpace=True)

    # Parent control under group
    cmds.parent(control, group)


# Loop through selected joints and create controls
for joint in selected_joints:
    createControl(joint)

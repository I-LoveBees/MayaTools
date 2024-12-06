import maya.cmds as cmds

# Select the control first, then the group containing the next control
sels = cmds.ls(sl=True)

if len(sels) < 2:
    cmds.error("Please select at least two objects: a control and the group containing the control to follow.")

for index in range(0, len(sels) - 1, 1):
    parent_ctrl = sels[index]          # The control driving the movement
    child_ctrl_grp = sels[index + 1]  # The group of the control to follow

    # Ensure the second selection is indeed a group
    if not cmds.objectType(child_ctrl_grp, isType="transform"):
        cmds.error(f"'{child_ctrl_grp}' is not a valid transform. Ensure you are selecting the correct group.")

    # Retrieve the child control within the group
    child_ctrl = cmds.listRelatives(child_ctrl_grp, children=True, type="transform")
    if not child_ctrl:
        cmds.error(f"Group '{child_ctrl_grp}' does not contain any controls. Ensure the group contains a control object.")
    child_ctrl = child_ctrl[0]

    # Creating parent constraints with and without translate/rotate
    p_constraint1 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipRotate=['x', 'y', 'z'], weight=1)[0]
    p_constraint2 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipTranslate=['x', 'y', 'z'], weight=1)[0]
    s_constraint = cmds.scaleConstraint(parent_ctrl, child_ctrl_grp, mo=True, weight=1)[0]  # Constrain scale

    # Adding custom attributes to the child control
    cmds.addAttr(child_ctrl, ln="Follow_Translate", at="double", min=0, max=1, dv=1)
    cmds.setAttr(f"{child_ctrl}.Follow_Translate", e=True, keyable=True)
    cmds.addAttr(child_ctrl, ln="Follow_Rotate", at="double", min=0, max=1, dv=1)
    cmds.setAttr(f"{child_ctrl}.Follow_Rotate", e=True, keyable=True)

    # Connecting custom attributes to parent constraints
    cmds.connectAttr(f"{child_ctrl}.Follow_Translate", f"{p_constraint1}.w0", f=True)
    cmds.connectAttr(f"{child_ctrl}.Follow_Rotate", f"{p_constraint2}.w0", f=True)

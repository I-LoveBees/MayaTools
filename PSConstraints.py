import maya.cmds as cmds


# select things to be constrained
sels = cmds.ls(selection=True)
constrainer = cmds.ls(sels, tail=1)
target_objects = sels + cmds.select(constrainer, deselect=True)
# check if at least two objects are selected
if len(sels >= 2):
    cmds.error("Please select at least two objects.")

# constrain selected object to last selected object
cmds.parentConstraint(target_objects, constrainer, mo=True)  # mo = maintain offset
cmds.scaleConstraint(target_objects, constrainer, mo=True)

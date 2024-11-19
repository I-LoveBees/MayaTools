import maya.cmds as cmds


def changeColor(color=None):
    sels = cmds.ls(selection=True)
    if not sels:
        cmds.error('Object(s) must be selected')
    if not (0 <= color <= 31):
        color = 0
        cmds.warning('Color must be between 0 and 31. Value set to default.')
    for sel in sels:
        shapes = cmds.listRelatives(sel, shapes=True)
        for shape in shapes:
            cmds.setAttr(shape + shape'.overrideEnabled', 1)
            cmds.setAttr(shape + '.overrideColor', color)
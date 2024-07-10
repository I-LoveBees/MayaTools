import maya.cmds as cmds
import random


def placementGenerator(xmin, xmax, ymin, ymax, zmin, zmax, numdups):
    sels = cmds.ls(selection=True)
    if not sels:
        cmds.error('Object must be selected.')

    for sel in sels:
        for _ in range(numdups):
            # duplicate current object
            dup = cmds.duplicate(sel, returnRootsOnly=True)

            # Randomize the rotation, scale, position
            randX = random.uniform(xmin, xmax)
            randY = random.uniform(ymin, ymax)
            randZ = random.uniform(zmin, zmax)

            # Translate the duplicated object to the new position
            cmds.xform(dup, worldSpace=True, translation=(randX, randY, randZ))

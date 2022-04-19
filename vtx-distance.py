# Author: Nikita Kozlov
# Link: github.com/nyarstot

import maya.cmds as cmds
import math

selection = cmds.ls(sl = True)
units = cmds.currentUnit( query=True, linear=True )

if len(selection) <= 1 or len(selection) > 2:
    cmds.error("You must select exactly two points.")
else:
    vtxPos = cmds.xform(selection, q = True, ws = True, t = True)
    distance = math.sqrt((vtxPos[3] - vtxPos[0])**2 + (vtxPos[4] - vtxPos[1])**2 + (vtxPos[5] - vtxPos[2])**2)
    cmds.confirmDialog(title = 'Result', message = str(distance) + ' ' + units, button = ['Confirm'], defaultButton = 'Confirm')
from org.csstudio.opibuilder.scriptUtil import PVUtil
import math

y = PVUtil.getDoubleArray(pvArray[0])
y = [math.fabs(i) for i in y]

default = 10
maximum = max(y)

if maximum < default:
	widget.setPropertyValue("axis_1_maximum",  default)
	widget.setPropertyValue("axis_1_minimum", -default)
else:
	widget.setPropertyValue("axis_1_maximum",  maximum)
	widget.setPropertyValue("axis_1_minimum", -maximum)

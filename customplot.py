import matplotlib.pyplot as plot
import numpy as nmp
import hello as hlp

arrayNumber_FirstChairVertical=[10,15]
arrayNumber_FirstChairHorizontal=[10,80]

x=nmp.linspace(arrayNumber_FirstChairHorizontal,arrayNumber_FirstChairVertical,100)
plot.plot(x)
plot.show()

print(hlp.msg)
from math import fabs
from tkinter import Variable
from warnings import catch_warnings
import matplotlib.pyplot as plot
import numpy as nmp
import hello as hlp
#from standardplot import ArrayListofNumbers


InputedData= input("InputArrayData:").split(';')
InputedDataY=input("InputArrayData1:").split(';')
#SubData=InputedData.split(';')

DetailsOfError=""

try:
    Val0=int(InputedData[0])
except (Exception):
    print("this except{Exception}")
    Val0=10



#PositionVertical_x0=int(input("Input position X0:"));
#PositionVertical_x1=int(input("Input position X1:"));


#arrayNumber_FirstChairVertical=[SubData[0],SubData[1]]
#arrayNumber_FirstChairHorizontal=[10,80]

x=nmp.linspace(InputedData,InputedDataY,100)
plot.plot(x)
plot.show()

#print(hlp.msg)
#print(hlp.GlobalGetData(2))




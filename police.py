from pybricks.hubs import InventorHub
from pybricks.parameters import Color
from pybricks.tools import wait


hub = InventorHub()


for zayd in range(360):
    hub.light.on(Color.RED)
    wait(500)
    hub.light.on(Color.BLUE)
    wait(500)

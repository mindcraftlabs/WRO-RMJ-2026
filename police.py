from pybricks.hubs import InventorHub
from pybricks.parameters import Color
from pybricks.tools import wait
from umath import sin, pi

# Initialize the hub.
hub = InventorHub()

for i in range(5):
# Make an animation with multiple colors.




# Make the color RED grow faint and bright using a sine pattern.
    hub.light.animate([Color.RED, Color.BLUE, Color.NONE], interval=400)
    wait(10000)
    hub.light.animate([Color.RED, Color.BLUE, Color.NONE], interval=400)
   

# Cycle through a rainbow of colors.
    hub.light.animate([Color(h=i * 8) for i in range(45)], interval=500)

    wait(10000)

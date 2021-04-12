import mouse
from time import sleep

while True:
    print(mouse.get_position())
    sleep(0.1)

sleep(10)
# Maximize Button
mouse.move(2794, 16)
mouse.click()
sleep(2)

# Participant Button
mouse.move(2690, 1002)
mouse.click(button='left')
sleep(5)
# Exit Button
mouse.move(3480, 1013)
mouse.click(button='left')
# Confirm Exit Button
sleep(2)
mouse.move(3426, 920)
mouse.click(button='left')
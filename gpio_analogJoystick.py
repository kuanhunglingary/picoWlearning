from machine import Pin, ADC
import utime

xAxis = ADC(Pin(28))
yAxis = ADC(Pin(27))

button = Pin(18, Pin.IN, Pin.PULL_UP)
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    print(str(xValue) +", " + str(yValue) + " -- " + str(buttonValue))
    utime.sleep(0.1)

from tools import connect, reconnect
from machine import ADC, Timer

connect()

adc = ADC(4)  # create ADC object on ADC pin,????,??
conversion_factor = 3.3/65535

def tenSecond(t):
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - ( reading_v - 0.706 ) / 0.001721
    print(celsius)

tim = Timer()
tim.init(period=10000, callback=oneSecond)

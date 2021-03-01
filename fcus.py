from machine import UART
import serial, skrf

f = frequency(303.825, 'mhz')
c = cpw(frewq, w=10e-6, s=5e-6, ep_r=10.6)
c.line(100*1e-6)
u = UART(1, 9600)
u.init(9600, bits=8, parity=None, stop=1)

s = serial.Serial('/dev/ttyUART0')
s.write(b'sig.int')
s.close()

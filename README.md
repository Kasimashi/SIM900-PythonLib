# SIM900-PythonLib
SIM900 Library : Use with RaspberryPi.
It is use for sending SMS with SIM900/SIM900A Hardware.

## Prerequite :
- Open Terminal
- Type : sudo raspi-config
- In SubMenu 'Interfacing Options'
- Go to 'Serial'
- 'would you like a login shell to be accessible over serial', put 'No'
- 'would you like the serial port hardware to be enabled?', put 'yes' (2 times)
- Reboot raspebrry

If needed Change COM in Send_sms.py :
    COMPORT_NAME = "/dev/ttyS0" (Internal Serial for RaspberryPi4)

## Wiring

![Wiring](wiring.png)

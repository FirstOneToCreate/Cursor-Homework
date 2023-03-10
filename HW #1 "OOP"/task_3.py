# Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad,
# WebCam, Ports, Speakers and create an HPLaptop class by using your interface.

from abc import ABC, abstractmethod

class LaptopInterface(ABC):

    def screen(self):
        pass

    def keyboard(self):
        pass

    def touchpad(self):
        pass

    def webcam(self):
        pass

    def ports(self):
        pass

    def speakers(self):
        pass


class HPLaptop(LaptopInterface):

    def screen(self):
        print("14' IPS FullHD 60 Hz screen")

    def keyboard(self):
        print("HP Collaboration Keyboard")

    def touchpad(self):
        print("Microsoft Precision Touchpad")

    def webcam(self):
        print("720p HD webcam")

    def ports(self):
        print("1x USB 3.0 charging port, 1x HDMI 1.4b, 1x MiniJack, Power connector, 1x Ethernet port, 1x USB 3.1, 1x Type-C 3.1")

    def speakers(self):
        print("Bang & Olufsen")


hp_laptop = HPLaptop()
hp_laptop.screen()
hp_laptop.keyboard()
hp_laptop.touchpad()
hp_laptop.webcam()
hp_laptop.ports()
hp_laptop.speakers()

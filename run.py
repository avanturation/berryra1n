import i2c_driver
import subprocess
from time import *


class BerryRa1n:
    def __init__(self) -> None:
        self.lcd = i2c_driver.lcd()

    def run(self, pongoos: bool = False):
        cmd = "sudo ./checkra1n -v -c -V"
        if pongoos:
            cmd += " -p"
            self.pongo = pongoos
        self.subp(cmd)

    def parse(self, value: str):
        _list = value.split(":")
        msg = _list[-1]
        return msg

    def subp(self, cmd: str):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for out in iter(proc.stdout.readline, b""):
            real = self.parse(out)
            if real == " Waiting for DFU devices":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("WAITING DFU", "1")
            elif real == " Exploiting":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("EXPLOITING", "1")
            elif real == " Checkmate!":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("CHECKM8!", "1")
            elif real == " Booting...":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("BOOTING", "1")
            elif real == " Uploading bootstrap...":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("BOOTSTRAP", "1")
            elif real == " All Done":
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("DONE", "1")
            elif real == " -20)" and self.pongo:
                self.lcd.lcd_clear()
                self.lcd.lcd_display_string("PONGOOS", "1")


if __name__ == "__main__":
    checkra1n = BerryRa1n()
    BerryRa1n.run()
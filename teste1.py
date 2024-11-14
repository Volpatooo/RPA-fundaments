from pywinauto.application import Application
from pywinauto import Desktop
from PIL import ImageGrab
import time
def open_calculator_take_print():
    app = Application().start('calc.exe')

    time.sleep(1)

    calc = Desktop(backend='uia').Calculator
    calc.wait('Visible', timeout=10)
    rect = calc.rectangle()
    screenshot = ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom))
    screenshot.save("screenshot_calculadora_pywinauto.png")

open_calculator_take_print()
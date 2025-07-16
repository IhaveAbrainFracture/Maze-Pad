print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Keyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.extensions.rgb import RGB


keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
keyboard.col_pins = (board.GP1, board.GP2, board.GP4)
keyboard.row_pins = (board.GP0, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


PASTE =KC.MACRO(
  (
    KC.LCTL(KC.V)),
  )

COPY =KC.MACRO(
  (
    KC.LCTL(KC.C)),
  )


Save =KC.MACRO(
  (
    KC.LCTL(KC.S)),
  )

Alt_Tab =KC.MACRO(
  (
    KC.LALT(KC.LTAB),
  )
)

rgb = RGB(pixel_pin=board.GP6, num_pixels=2)
keyboard.extensions.append(rgb)



keyboard.keymap =     [
        KC.RGB_MODE_BREATHE,    KC.RGB_VAI,    Alt_Tab,
        COPY,                   PASTE,         Save,
    ],


if __name__ == '__main__':
    keyboard.go()
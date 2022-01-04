def on_button_pressed_a():
    music.play_melody("C5 - - - - - - - ", 120)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    music.play_melody("C5 - - - - - - - ", 120)
    basic.show_leds("""
        # . . . .
                # . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    music.play_melody("C5 - - - - - - - ", 120)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
if input.pin_is_pressed(TouchPin.P1):
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        music.play_melody("C5 B C5 B A G F E ", 120)
basic.forever(on_forever)

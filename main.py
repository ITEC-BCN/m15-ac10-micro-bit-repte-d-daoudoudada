
temperatura = randint(0, 50)
if 0 < temperatura and temperatura < 10:
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        """)
elif 10 < temperatura and temperatura < 20:
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        # . . . .
        """)
elif 20 < temperatura and temperatura < 30:
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
elif 30 < temperatura and temperatura < 40:
    basic.show_leds("""
        . . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
else:
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)

def on_forever():
    if 0 < temperatura and temperatura < 22:
        basic.show_string("fred")
    else:
        basic.show_string("calor")
basic.forever(on_forever)

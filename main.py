isTemperatura = False
temperatura = 0
nivel_Luz = 0

def on_button_pressed_a():
    global isTemperatura
    isTemperatura = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global isTemperatura
    isTemperatura = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global temperatura, nivel_Luz
    if isTemperatura == True:
        music.stop_melody(MelodyStopOptions.ALL)
        temperatura = input.temperature()
        if temperatura > 22:
            basic.show_icon(IconNames.SKULL)
        else:
            basic.show_icon(IconNames.UMBRELLA)
    else:
        nivel_Luz = input.light_level()
        if nivel_Luz > 150:
            music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
                music.PlaybackMode.UNTIL_DONE)
        else:
            music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)

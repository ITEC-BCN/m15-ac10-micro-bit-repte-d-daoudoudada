let isTemperatura = false
let temperatura = 0
let nivel_Luz = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    isTemperatura = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    isTemperatura = false
})
basic.forever(function on_forever() {
    
    if (isTemperatura == true) {
        music.stopMelody(MelodyStopOptions.All)
        temperatura = input.temperature()
        if (temperatura > 22) {
            basic.showIcon(IconNames.Skull)
        } else {
            basic.showIcon(IconNames.Umbrella)
        }
        
    } else {
        nivel_Luz = input.lightLevel()
        if (nivel_Luz > 150) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.UntilDone)
        } else {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.UntilDone)
        }
        
    }
    
})

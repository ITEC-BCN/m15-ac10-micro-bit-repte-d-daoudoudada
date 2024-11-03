input.onButtonPressed(Button.A, function () {
    isTemperatura = true
})
input.onButtonPressed(Button.B, function () {
    isTemperatura = false
})
let nivel_Luz = 0
let isTemperatura = false
let temperatura = randint(0, 50)
basic.forever(function () {
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

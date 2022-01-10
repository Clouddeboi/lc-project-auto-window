let temperature = 0
pins.servoWritePin(AnalogPin.P1, 0)
basic.forever(function () {
    basic.showNumber(input.temperature())
    while (true) {
        temperature = smarthome.ReadTemperature(TMP36Type.TMP36_temperature_C, AnalogPin.P1)
        if (input.temperature() < 19) {
            pins.servoWritePin(AnalogPin.P1, 0)
            basic.pause(2000)
        } else if (input.buttonIsPressed(Button.B)) {
            pins.servoWritePin(AnalogPin.P1, 180)
            basic.pause(2000)
        } else if (input.buttonIsPressed(Button.A)) {
            pins.servoWritePin(AnalogPin.P1, 0)
        } else {
            pins.servoWritePin(AnalogPin.P1, 100)
            basic.pause(2000)
        }
    }
})

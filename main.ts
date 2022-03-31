let temperature = 0
let temp = 0
pins.servoWritePin(AnalogPin.P1, 0)
basic.forever(function () {
    basic.showNumber(temp)
    basic.pause(1000)
})
basic.forever(function () {
    temp = input.temperature()
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        pins.servoWritePin(AnalogPin.P1, 0)
        basic.pause(5000)
    }
})
basic.forever(function () {
    basic.showNumber(temp)
    while (true) {
        temperature = smarthome.ReadTemperature(TMP36Type.TMP36_temperature_C, AnalogPin.P1)
        if (temp < 19) {
            pins.servoWritePin(AnalogPin.P1, 0)
            basic.pause(2000)
        } else {
            pins.servoWritePin(AnalogPin.P1, 90)
            basic.pause(2000)
        }
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        pins.servoWritePin(AnalogPin.P1, 90)
        basic.pause(5000)
    }
})
basic.forever(function () {
    dataStreamer.writeNumberArray([temp])
    if (temp < 19) {
        dataStreamer.writeString("Window Closed")
        dataStreamer.writeLine()
    } else {
        dataStreamer.writeString("Window Open")
        dataStreamer.writeLine()
    }
})

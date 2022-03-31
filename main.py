temperature = 0
pins.servo_write_pin(AnalogPin.P1, 0)

def on_forever():
    basic.show_number(input.temperature())
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.A):
        pins.servo_write_pin(AnalogPin.P1, 0)
        basic.pause(5000)
basic.forever(on_forever2)

def on_forever3():
    global temperature
    basic.show_number(input.temperature())
    while True:
        temperature = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)
        if input.temperature() < 19:
            pins.servo_write_pin(AnalogPin.P1, 0)
            basic.pause(2000)
        else:
            pins.servo_write_pin(AnalogPin.P1, 90)
            basic.pause(2000)
basic.forever(on_forever3)

def on_forever4():
    if input.button_is_pressed(Button.B):
        pins.servo_write_pin(AnalogPin.P1, 90)
        basic.pause(5000)
basic.forever(on_forever4)

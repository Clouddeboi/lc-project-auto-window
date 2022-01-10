temperature = 0
pins.servo_write_pin(AnalogPin.P1, 0)

def on_forever():
    global temperature
    basic.show_number(input.temperature())
    while True:
        temperature = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)
        if input.temperature() < 19:
            pins.servo_write_pin(AnalogPin.P1, 0)
            basic.pause(2000)
        elif input.button_is_pressed(Button.B):
            pins.servo_write_pin(AnalogPin.P1, 180)
            basic.pause(2000)
        elif input.button_is_pressed(Button.A):
            pins.servo_write_pin(AnalogPin.P1, 0)
        else:
            pins.servo_write_pin(AnalogPin.P1, 100)
            basic.pause(2000)
basic.forever(on_forever)

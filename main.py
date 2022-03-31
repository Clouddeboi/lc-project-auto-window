temperature = 0
temp = 0
pins.servo_write_pin(AnalogPin.P1, 0)

def on_forever():
    basic.show_number(temp)
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    global temp
    temp = input.temperature()
basic.forever(on_forever2)

def on_forever3():
    if input.button_is_pressed(Button.A):
        pins.servo_write_pin(AnalogPin.P1, 0)
        basic.pause(5000)
basic.forever(on_forever3)

def on_forever4():
    global temperature
    basic.show_number(temp)
    while True:
        temperature = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)
        if temp < 19:
            pins.servo_write_pin(AnalogPin.P1, 0)
            basic.pause(2000)
        else:
            pins.servo_write_pin(AnalogPin.P1, 90)
            basic.pause(2000)
basic.forever(on_forever4)

def on_forever5():
    if input.button_is_pressed(Button.B):
        pins.servo_write_pin(AnalogPin.P1, 90)
        basic.pause(5000)
basic.forever(on_forever5)

def on_forever6():
    dataStreamer.write_number_array([temp])
    if temp < 19:
        dataStreamer.write_string("Window Closed")
    else:
        dataStreamer.write_string("Window Open")
basic.forever(on_forever6)

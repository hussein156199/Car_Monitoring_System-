from machine import Pin
import time


ENTRANCE_BTN_PIN = 34
EXIT_BTN_PIN = 35

led_pins = [2, 4, 5, 13, 14, 16, 17, 18]


entrance_btn = Pin(ENTRANCE_BTN_PIN, Pin.IN, Pin.PULL_DOWN)
exit_btn = Pin(EXIT_BTN_PIN, Pin.IN, Pin.PULL_DOWN)


leds = [Pin(pin, Pin.OUT) for pin in led_pins]


car_count = 0
prev_entrance_btn_state = 0
prev_exit_btn_state = 0

def update_leds():
    for i in range(8):
        if i < car_count:
            leds[i].value(1)
        else:
            leds[i].value(0)


while True:
    
    entrance_btn_state = entrance_btn.value()
    exit_btn_state = exit_btn.value()

    
    if entrance_btn_state == 1 and prev_entrance_btn_state == 0 and car_count < 8:
        car_count += 1
        update_leds()
        time.sleep(0.2)  

   
    if exit_btn_state == 1 and prev_exit_btn_state == 0 and car_count > 0:
        car_count -= 1
        update_leds()
        time.sleep(0.2)  

   
    prev_entrance_btn_state = entrance_btn_state
    prev_exit_btn_state = exit_btn_state

    time.sleep(0.05) 

#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.2  # seconds
#notes for through the fire and the flames intro -dragonforce
freqs = [261, 293, 311, 261, 293, 311, 349, 311, 392, 311, 349, 293, 311, 261, 293, 233]
print("Playing frequency (Hz):")

count = 0

while count < 3:    
    for i in range(len(freqs)):
        print(i)
        playtone(freqs[i], duration)
    count+=1


# Turn off the PWM
quiet()

import json
from pathlib import Path
import RPi.GPIO as GPIO
import time

# メモ: リレー2番ぶっ壊れてるかも
relayToGpio = {
    "1": 4,
    "2": 17, # 使用不可
    "3": 27,
    "4": 22,
    "5": 18,
    "6": 23,
    "7": 24,
    "8": 25
}

# Jsonファイルから音声コマンドの配列を読み込む
with open(Path("data/voiceCommand.json"), "rb") as f:
    command = json.load(f)

INITIAL_POSITION = command["initialposition"]
START = command["start"]
STOP = command["stop"]
WEIGHT_UP = command["weightup"]
WEIGHT_DOWN = command["weightdown"]
ANGLE_UP = command["angleup"]
ANGLE_DOWN = command["angledown"]

def gpioInit():
    """GPIOを初期化する関数
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for gpio_pin in relayToGpio.values():
        GPIO.setup(gpio_pin, GPIO.OUT)

def control(voice_command):
    """音声コマンドに応じてGPIOを制御する関数
    """
    if voice_command in INITIAL_POSITION:
        print("[INFO] Voice command recognized: INITIAL POSITION")
        GPIO.output(relayToGpio['1'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['1'], GPIO.LOW)
    elif voice_command in START:
        print("[INFO] Voice command recognized: START")
        GPIO.output(relayToGpio['3'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['3'], GPIO.LOW)
    elif voice_command in STOP:
        print("[INFO] Voice command recognized: STOP")
        GPIO.output(relayToGpio['4'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['4'], GPIO.LOW)
    elif voice_command in WEIGHT_UP:
        print("[INFO] Voice command recognized: WEIGHT UP")
        GPIO.output(relayToGpio['5'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['5'], GPIO.LOW)
    elif voice_command in WEIGHT_DOWN:
        print("[INFO] Voice command recognized: WEIGHT DOWN")
        GPIO.output(relayToGpio['6'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['6'], GPIO.LOW)
    elif voice_command in ANGLE_UP:
        print("[INFO] Voice command recognized: ANGLE UP")
        GPIO.output(relayToGpio['7'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['7'], GPIO.LOW)
    elif voice_command in ANGLE_DOWN:
        print("[INFO] Voice command recognized: ANGLE DOWN")
        GPIO.output(relayToGpio['8'], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayToGpio['8'], GPIO.LOW)
        
def gpioCleanUp():
    """GPIOをクリーンアップする関数
    """
    GPIO.cleanup()
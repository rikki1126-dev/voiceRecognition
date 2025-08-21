import json
from pathlib import Path

# Jsonファイルから音声コマンドの配列を読み込む
with open(Path("data/voiceCommand.json"), "rb") as f:
    command = json.load(f)
    
START = command["start"]
STOP = command["stop"]
SPEED_UP = command["speedup"]
SPEED_DOWN = command["speeddown"]
WEIGHT_UP = command["weightup"]
WEIGHT_DOWN = command["weightdown"]

def control(voice_command):
    """音声コマンドに応じてGPIOを制御する関数
    """
    if voice_command in START:
        print("[INFO] Voice command recognized: START")
    elif voice_command in STOP:
        print("[INFO] Voice command recognized: STOP")
    elif voice_command in SPEED_UP:
        print("[INFO] Voice command recognized: SPEED UP")
    elif voice_command in SPEED_DOWN:
        print("[INFO] Voice command recognized: SPEED DOWN")
    elif voice_command in WEIGHT_UP:
        print("[INFO] Voice command recognized: WEIGHT UP")
    elif voice_command in WEIGHT_DOWN:
        print("[INFO] Voice command recognized: WEIGHT DOWN")
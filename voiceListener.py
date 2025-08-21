import json
from pathlib import Path

from vosk import Model, KaldiRecognizer
import pyaudio

# Jsonファイルからウェイクワードの配列を読み込む
with open(Path("data/wakeword.json"), "rb") as f:
    wakeword = json.load(f)

WAKE = wakeword["wake"]
EXIT = wakeword["exit"]

# Voskモデルの読み込み
model = Model(str(Path("vosk-model-small-en-us-0.15").resolve()))

# マイクの初期化
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

# voskの設定
def transcription():
    """文字おこしを行う関数

    Returns:
        str: 音声認識結果
    """
    stream = mic.open(format=pyaudio.paInt16,
                       channels=1, 
                       rate=16000, 
                       input=True, 
                       frames_per_buffer=4096)
    # ストリーミングデータを読み取り続けるループ
    while True:
        stream.start_stream()
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                response = result["text"].strip()
                if response:
                    print("USER:", response)
                    return response
        except OSError:
            pass

# 状態フラグ変数
waiting_wakeword = True
waiting_command = False

def listen():
    """状態遷移関数

    Returns:
        str: 音声コマンド
    """
    global waiting_wakeword, waiting_command
    
    if waiting_command == True: print("[STATUS] Voice command listening...")
    else: print("[STATUS] Wakeword listening...")
    
    #***********************************************************************************
    # 状態 : ウェイクワード検出
    #***********************************************************************************
    while waiting_wakeword:
        response = transcription()
        if response in WAKE:
            waiting_wakeword = False
            waiting_command = True
            print("[STATUS] Voice command listening...")
    
    #***********************************************************************************
    # 状態 : 音声コマンド検出
    #***********************************************************************************
    while waiting_command:
        response = transcription()
        if response in EXIT:
            waiting_wakeword = True
            waiting_command = False
        else:
            return response
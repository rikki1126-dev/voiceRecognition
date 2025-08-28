import voiceListener
import gpioController

def main():
    """メイン関数
    """
    try:
        print("[INFO] Voice controller has been launched")
        # GPIOを初期化
        gpioController.gpioInit()
        # ユーザの音声を聞き取る
        while True:
            # ウェイクワード検出機能を使う場合
            # voice_command = voiceListener.listen()
            
            # 単純な音声認識のみ行う場合
            print("[STATUS] Voice command listening...")
            voice_command = voiceListener.transcription()

            # 音声認識結果をもとにGPIOを制御
            if voice_command:
                gpioController.control(voice_command)
            
    except KeyboardInterrupt:
        # GPIOをクリーンアップ
        gpioController.gpioCleanUp()
        print("[INFO] Voice controller has been stopped")

if __name__ == "__main__":
    main()
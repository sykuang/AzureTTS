from dotenv import load_dotenv
from os import getenv
import azure.cognitiveservices.speech as speechsdk
import argparse

load_dotenv()
SPEECH_KEY = getenv("SPEECH_KEY")
SPEECH_REGION = getenv("SPEECH_REGION")


def tts(text: str, voice_name: str, filename: str):
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY, region=SPEECH_REGION
    )
    if not filename:
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    else:
        audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = "en-US-AshleyNeural"

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    # text = input

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if (
        speech_synthesis_result.reason
        == speechsdk.ResultReason.SynthesizingAudioCompleted
    ):
        print(f"Speech synthesized for text [{text}]")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, default="tts.wav",help="Output filename")
    parser.add_argument("--text", type=str, default="Hello world",help="Text to speak")
    parser.add_argument("--voice", type=str, default="en-US-AshleyNeural",help="Voice to use")
    parser.add_argument("--play", action="store_true", default=False,help="Play the output or store in filename")
    parser.add_argument("--script", type=str, help="Script to read")
    args = parser.parse_args()
    if args.script:
        with open(args.script) as f:
            cnt=1
            for line in f.readlines():
                tts(line, args.voice, f"tts{cnt}.wav")
                cnt+=1
    else:
        filename = "" if args.play else args.filename
        tts(args.text, args.voice, filename)


if __name__ == "__main__":
    main()

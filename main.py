from dotenv import load_dotenv
from os import getenv
from glob import glob
import azure.cognitiveservices.speech as speechsdk
import argparse

load_dotenv()
SPEECH_KEY = getenv("SPEECH_KEY")
SPEECH_REGION = getenv("SPEECH_REGION")


def generate_ssml(text: str, voice_name: str, style: str = "chat", stydegree: int = 1,rate="default"):
    ssml = (
        '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">'
        f'<voice name="{voice_name}">'
        f'<prosody pitch="default" contour="default" range="default" rate="{rate}" volume="default">'
        f'<mstts:express-as style="{style}" styledegree="{stydegree}">'
        f"{ text }"
        "</mstts:express-as>"
        '</prosody>'
        "</voice>"
        "</speak>"
    )
    print(ssml)
    return ssml


def tts(
    text: str, voice_name: str, filename: str, style: str = "chat", stydegree: int = 1,rate="default"
):
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY, region=SPEECH_REGION
    )
    if not filename:
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        filename="speaker"
    else:
        audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = voice_name

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )

    ssml = generate_ssml(text, voice_name, style, stydegree,rate)
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

    if (
        speech_synthesis_result.reason
        == speechsdk.ResultReason.SynthesizingAudioCompleted
    ):
        print(f"Speech synthesized for text [{text}] to [{filename}]")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename", type=str, default="tts.wav", help="Output filename"
    )
    parser.add_argument("--text", type=str, default="Hello world", help="Text to speak")
    parser.add_argument(
        "--voice", type=str, default="en-US-JennyNeural", help="Voice to use"
    )
    parser.add_argument(
        "--style",
        type=str,
        default="chat",
        help="Voice style to use, this arugment will be the default style if script is provided. Default is chat",
    )
    parser.add_argument(
        "--styledegree",
        type=int,
        default=1,
        help="Voice style degree, this arugment will be the default style degree if script is provided. Default is 1",
    )
    parser.add_argument(
        "--play",
        action="store_true",
        default=False,
        help="Play the output or store in filename",
    )
    parser.add_argument(
        "--rate",
        type=str,
        default="default",
        help="Play the output or store in filename",
    )
    parser.add_argument("--script", type=str, help="Script to read")
    args = parser.parse_args()
    if args.script:
        with open(args.script) as f:
            cnt = 1
            for line in f.readlines():
                ls = line.split(":")
                style = args.style
                styledegree = args.styledegree
                if len(ls) == 2:
                    style = ls[0].split(",")[0]
                    styledegree = ls[0].split(",")[1]
                    text = ls[1]
                else:
                    text = line

                while len(glob(f"tts{cnt}.wav"))>0:
                    cnt+=1
                tts(text, args.voice, f"tts{cnt}.wav", style, styledegree)
                cnt += 1
    else:
        filename = "" if args.play else args.filename
        tts(args.text, args.voice, filename, args.style, args.styledegree,args.rate)


if __name__ == "__main__":
    main()

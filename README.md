# Azure TTS
## Usage
1. pip install -r requirement.txt
1. Copy .env_eamply to .env
1. Modify your Azure TTS key in .env
1. `python main.py --text "Hello world" --voice en-US-AriaNeural`
1. Output will be `tts.wav`

### Play the audio instead of saving file

1. `python main.py --text "Hello world" --voice en-US-AriaNeural --play`
### Generate batch file from script
1. Generate Multiple audio for each line in script
1. `python main.py --script script.txt`
1. Output will be `tts*.wav`
### Help

```
  -h, --help            show this help message and exit
  --filename FILENAME   Output filename
  --text TEXT           Text to speak
  --voice VOICE         Voice to use
  --style STYLE         Voice style to use, this arugment will be the default style if script is provided. Default is chat
  --styledegree STYLEDEGREE
                        Voice style degree, this arugment will be the default style degree if script is provided. Default is 1
  --play                Play the output or store in filename
```
### Add voice style to your script in each line.
To adjust the voice style, `add style,styledegree:` at the beginning of each line. If no style is specified, the default voice style will be used, which can be adjusted using the `--style` option.
```
excited,2:Creates a speech synthesizer with a null output stream.
This means the audio output data will not be written to any output channel.
You can just get the audio from the result.
```

### Voice list
Language|Text-to-speech voice|Gender
--|--|--|
English (United States)|en-US-JennyMultilingualNeural3|(Female)
||en-US-JennyNeural|(Female)
||en-US-GuyNeural|(Male)
||en-US-AriaNeural|(Female)
||en-US-DavisNeural|(Male)
||en-US-AmberNeural|(Female)
||en-US-AnaNeural|(Female, Child)
||en-US-AshleyNeural|(Female)
||en-US-BrandonNeural|(Male)
||en-US-ChristopherNeural|(Male)
||en-US-CoraNeural|(Female)
||en-US-ElizabethNeural|(Female)
||en-US-EricNeural|(Male)
||en-US-JacobNeural|(Male)
||en-US-JaneNeural|(Female)
||en-US-JasonNeural|(Male)
||en-US-MichelleNeural|(Female)
||en-US-MonicaNeural|(Female)
||en-US-NancyNeural|(Female)
||en-US-RogerNeural|(Male)
||en-US-SaraNeural|(Female)
||en-US-SteffanNeural|(Male)
||en-US-TonyNeural|(Male)
||en-US-AIGenerate1Neural1|(Male)
||en-US-AIGenerate2Neural1|(Female)
||en-US-BlueNeural1|(Neutral)
||en-US-JennyMultilingualV2Neural1,3|(Female)
||en-US-RyanMultilingualNeural1,3|(Male)

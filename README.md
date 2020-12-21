# SmartSTT-- In-Car Speech Recognition

HONDA HACKATHON - Voice Based Services On Connected Car Platform

## TEAM 7 : Members

```markdown
1.Ahesh Behera
2.Bighnesh Sahoo
3.Chidananda Sahoo
4.Swayam Padhi
```
## Instructions for Alexa skill:
* Alexa Skill codebase was developed and tested using the Alexa developer console. 
* The Alexa Skill for SmartSTT feature was deployed using AWS Free tier provided by Amazon. 
* The skill invocation name is "request the driver". This is used to invoke the Alexa skill while speaking to Alexa.
* While making a request, use "please" before the request as it is a compulsory slot for the utterance.

## Instructions for python (Virtual Assistant):
* First ensure that the "light.py" and "main.py" files are present in a same folder.
* Install and import all modules required .( Modules required : speech_recognition , pyttsx3 , pywhatkit , datetime , wikipedia , pyjokes , light , pyaudio)
* Wait untill you see " ... " and once it comes ,it means that our assistant is ready to hear our commands.
* Use the keyword Alexa before giving command like "Alexa,tell driver to turn up AC" .
* To terminate the assistant you can say "Alexa,thank you" or "stop" command.

NOTE:Say "driver" in the command in order to get the blinking light screen

Also note that, you might face problem in installing pyaudio module so you can lower the python version to less than 3.6 or follow these steps:
* find your Python version by `python --version` mine is `3.7.3` for example
* find the appropriate `.whl` file from here : https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio , for example mine is `PyAudio‑0.2.11‑cp37‑cp37m‑win32.whl`, and download it.
* go to the folder where it is downloaded and go to the folder where both the python files are present and save it in that folder
* install the .whl file with pip for example in my case:
   ```markdown
   pip install PyAudio-0.2.11-cp37-cp37m-win32.whl
   ```

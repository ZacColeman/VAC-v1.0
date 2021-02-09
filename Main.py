import VoiceRecognition as vr
import MathFunc as mf

recognized_text = vr.speechToText()
x = recognized_text.split(' ')

if 'math' and 'problem' in x:
    vr.textToSpeech('sure, what kind of problem?')
    recognized_text = vr.speechToText()

    if recognized_text == 'addition':
        mf.addition()
    elif recognized_text == 'subtraction':
        mf.subtraction()
    elif recognized_text == 'multiplication':
        mf.multiplication()
    elif recognized_text == 'division':
        mf.division()
    else:
        vr.textToSpeech('addition is all I can do')

else:
    vr.textToSpeech('I can only do math problems')

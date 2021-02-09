import VoiceRecognition as vr


def test():
    vr.textToSpeech('What numbers do you need to add?')
    numbers = vr.speechToText()
    numbers.split(' ')
    sum(numbers)


def addition():
    vr.textToSpeech('What is the first number?')
    x1 = int(vr.speechToText())
    vr.textToSpeech('The first number is ')
    vr.textToSpeech(x1)

    vr.textToSpeech('What is the second number?')
    x2 = int(vr.speechToText())
    vr.textToSpeech('The second number is ')
    vr.textToSpeech(x2)

    vr.textToSpeech('Calculating')

    answer = x1 + x2
    vr.textToSpeech('The answer is ')
    vr.textToSpeech(answer)


def subtraction():
    vr.textToSpeech('What is the first number?')
    x1 = int(vr.speechToText())
    vr.textToSpeech('The first number is ')
    vr.textToSpeech(x1)

    vr.textToSpeech('What is the second number?')
    x2 = int(vr.speechToText())
    vr.textToSpeech('The second number is ')
    vr.textToSpeech(x2)

    vr.textToSpeech('Calculating')

    answer = x1 - x2
    vr.textToSpeech('The answer is ')
    vr.textToSpeech(answer)


def multiplication():
    vr.textToSpeech('What is the first number?')
    x1 = int(vr.speechToText())
    vr.textToSpeech('The first number is ')
    vr.textToSpeech(x1)

    vr.textToSpeech('What is the second number?')
    x2 = int(vr.speechToText())
    vr.textToSpeech('The second number is ')
    vr.textToSpeech(x2)

    vr.textToSpeech('Calculating')

    answer = x1 * x2
    vr.textToSpeech('The answer is ')
    vr.textToSpeech(answer)


def division():
    vr.textToSpeech('What is the first number?')
    x1 = int(vr.speechToText())
    vr.textToSpeech('The first number is ')
    vr.textToSpeech(x1)

    vr.textToSpeech('What is the second number?')
    x2 = int(vr.speechToText())
    vr.textToSpeech('The second number is ')
    vr.textToSpeech(x2)

    vr.textToSpeech('Calculating')

    answer = x1 / x2
    vr.textToSpeech('The answer is ')
    vr.textToSpeech(answer)

test()
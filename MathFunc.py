import VoiceRecognition as vr


def test():
    vr.textToSpeech('What numbers do you need to subtract?')
    numbers = vr.speechToText()
    numbers.split(' ')
    print(numbers)
    answer = [int(i) for i in numbers]
    i = 1
    ans = answer[0]

    while i < len(answer):
        sub = answer[i]
        ans = ans / sub
        print(ans)
        i += 1

    vr.textToSpeech(ans)


def addition():
    vr.textToSpeech('What numbers do you need to add?')
    numbers = vr.speechToText()
    numbers.split(' ')
    answer = list(map(int, numbers))

    vr.textToSpeech('the sum is')
    vr.textToSpeech(sum(answer))


def subtraction():
    vr.textToSpeech('What numbers do you need to subtract?')
    numbers = vr.speechToText()
    numbers.split(' ')
    answer = list(map(int, numbers))
    i = 1
    ans = answer[0]

    while i < len(answer):
        sub = answer[i]
        ans = ans - sub
        print(ans)
        i += 1

    vr.textToSpeech(ans)

def multiplication():
    vr.textToSpeech('What numbers do you need to subtract?')
    numbers = vr.speechToText()
    numbers.split(' ')
    answer = list(map(int, numbers))
    i = 1
    ans = answer[0]

    while i < len(answer):
        sub = answer[i]
        ans = ans * sub
        print(ans)
        i += 1

    vr.textToSpeech(ans)
def division():
    vr.textToSpeech('What numbers do you need to subtract?')
    numbers = vr.speechToText()
    numbers.split(' ')
    answer = list(map(int, numbers))
    i = 1
    ans = answer[0]

    while i < len(answer):
        sub = answer[i]
        ans = ans - sub
        print(ans)
        i += 1

    vr.textToSpeech(ans)


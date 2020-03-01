import argparse
import random
import Interaction

import Facial
import GlobalVariables
import TextToSpeech
from Camera import Camera
from RecordAudio import RecordAudio
import SpeechToTextLOCAL
from playsound import playsound


def startcycle():
    interact.open(4)
    GlobalVariables.response = "Hello! I am the Hackathon Application Cloud Computing System or HACCS for short! How may I help you today?"
    TextToSpeech.run_quickstart()
    interact.open(5)
    playsound('output.mp3')
    # cycle()


def cycle():
    # Take Image
    Camera().takePic()

    # Process Face
    detect_faces1()

    input("Press Enter to Record")

    # RecordAudio
    RecordAudio().record()

    # Speech to Text
    SpeechToTextLOCAL.main()

    command = GlobalVariables.command

    processCommand(command)


def playNim():
    numMarbles = 20
    gameOver = False
    turnSucess = False
    GlobalVariables.response = "We will be playing Nim! We will take turns takeing 1, 2 or 3 marbles from a pile of 20. Winner is the person to take the last marble!"
    TextToSpeech.run_quickstart()
    playsound('output.mp3')

    while not gameOver:
        turnSucess=False
        # Take Image
        Camera().takePic()

        # Process Face
        detect_faces1()

        while not turnSucess:
            GlobalVariables.response = "Your Turn! How many marbles do you want?"
            TextToSpeech.run_quickstart()
            playsound('output.mp3')

            input("Press Enter to Record")

            # RecordAudio
            RecordAudio().record()

            # Speech to Text
            SpeechToTextLOCAL.main()

            command = GlobalVariables.command
            if "one" in command:
                numMarbles = numMarbles - 1
                turnSucess = True
            elif "two" in command or "to" in command:
                numMarbles = numMarbles - 2
                turnSucess = True
            elif "three" in command:
                numMarbles = numMarbles - 3
                turnSucess = True
            else:
                GlobalVariables.response = "You did not say a valid number, please try again!"
                TextToSpeech.run_quickstart()
                interact.open(3)
                playsound('output.mp3')

        GlobalVariables.response = f"There are {str(numMarbles)} Marbles left!"
        TextToSpeech.run_quickstart()
        playsound('output.mp3')

        if numMarbles == 0:
            GlobalVariables.response = "You Win! Congratulations!"
            TextToSpeech.run_quickstart()
            interact.open(0)
            playsound('output.mp3')
            gameOver = True
            cycle()

        elif numMarbles < 4:
            GlobalVariables.response = f"I will take {str(numMarbles)} Marbles!"
            TextToSpeech.run_quickstart()
            interact.open(0)
            playsound('output.mp3')
            numMarbles = 0

            GlobalVariables.response = f"There are {str(numMarbles)} Marbles left!"
            TextToSpeech.run_quickstart()
            interact.open(2)
            playsound('output.mp3')

            GlobalVariables.response = "I Win! Sorry!"
            TextToSpeech.run_quickstart()
            interact.open(8)
            playsound('output.mp3')
            gameOver = True
            cycle()

        elif GlobalVariables.emotionJoy < 3:
            r1 = random.randint(1, 3)
            GlobalVariables.response = f"I will take {r1} Marbles!"
            TextToSpeech.run_quickstart()
            interact.open(0)
            playsound('output.mp3')

            numMarbles = numMarbles - r1

            GlobalVariables.response = f"There are {str(numMarbles)} Marbles left!"
            TextToSpeech.run_quickstart()
            interact.open(2)
            playsound('output.mp3')

        else:
            num = 4 - (20 - numMarbles) % 4

            if num == 4:
                num = 1
            numMarbles=numMarbles-num

            GlobalVariables.response = f"I will take {num} Marbles!"
            TextToSpeech.run_quickstart()
            interact.open(0)
            playsound('output.mp3')

            GlobalVariables.response = f"There are {str(numMarbles)} Marbles left!"
            TextToSpeech.run_quickstart()
            interact.open(2)
            playsound('output.mp3')


def processEmotion():
    #
    if GlobalVariables.emotionJoy > 3:
        # print(2)
        r1 = random.randint(0, 2)

        if r1 == 0:
            GlobalVariables.response = "You look quite happy today!"
        elif r1 == 1:
            GlobalVariables.response = "I'm glad you are smiling!"
        elif r1 == 2:
            GlobalVariables.response = "You look like you are having a great day"

        TextToSpeech.run_quickstart()
        interact.open(0)

        playsound('output.mp3')
    else:
        r1 = random.randint(0, 2)

        if r1 == 0:
            interact.open(1)
            GlobalVariables.response = "You don't look particularly happy, I hope you are ok!"
        elif r1 == 1:
            interact.open(1)
            GlobalVariables.response = "You should smile more!"
        elif r1 == 2:
            interact.open(7)
            GlobalVariables.response = "You look tired. I hope things are fine!"

        TextToSpeech.run_quickstart()

        playsound('output.mp3')


def processCommand(s):
    if "how" in s and "you" in s:
        interact.open(6)
        howAreYou()
    if "play" in s and "game" in s:
        interact.open(6)
        playNim()


def howAreYou():
    r1 = random.randint(0, 2)

    if r1 == 0:
        interact.open(0)
        GlobalVariables.response = "I have been doing well, how about you?"
    elif r1 == 1:
        interact.open(1)
        GlobalVariables.response = "Been better, but its ok!"
    elif r1 == 2:
        interact.open(0)
        GlobalVariables.response = "It has been quite good"

    TextToSpeech.run_quickstart()

    playsound('output.mp3')
    processEmotion()
    cycle()


def detect_faces1():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_faces_parser = subparsers.add_parser(
        'faces', help=Facial.detect_faces.__doc__)
    detect_faces_parser.add_argument('path')

    args = parser.parse_args()
    run_local(args)


def detect_faces2(path):
    """Detects faces in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_face_detection]
    # [START vision_python_migration_image_file]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END vision_python_migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print(face.joy_likelihood)
        print("^-^")
        GlobalVariables.emotionJoy = face.joy_likelihood

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


def run_local(args):
    if args.command == 'faces':
        detect_faces2(args.path)


if __name__ == '__main__':
    interact = Interaction.Webpage()
    startcycle()

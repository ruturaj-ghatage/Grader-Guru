import sys
import FlowchartObjectDetection
import Debug
import Constants
import Enums
import os
from PIL import Image
from Classes.Block import Block
from Enums import OCR
from DataExtraction import data_Ex
import cv2

def main():

    '''Image Extraction -> text and diagram''' 
     
    answers = data_Ex('D:\\BEProject\\ObjectDetection\\Images_Craft')
    for x in answers:
        print(answers[x]['text'])
        for j in answers[x]['diagrams']:
            cv2.imwrite("D:\\BEProject\\ObjectDetection\\User_Files\\InputImages\\x.jpg",j)


    ''' Diagram Evaluation'''
    # dir_list= get_image_list()
    # selection= image_selection(dir_list)

    # img: Image
    # img = Image.open(r"{0}{1}\{2}".format(os.getcwd(), Constants.INPUT_FOLDER, dir_list[selection]))

    # # selection_ocr = detection_system()
    # # # selection_language = language_selection()
    # # print("selection_ocr")
    # # print(selection_ocr)


    # blocks = FlowchartObjectDetection.get_blocks(img, ocr_system=OCR(1))
    # Debug.print_blocks(blocks)
    # print("Press a button to exit")

    # s = input()


def print_header() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")


def get_image_list():
    dir_list = os.listdir("{0}{1}".format(os.getcwd(), Constants.INPUT_FOLDER))
    if len(dir_list) <= 0:
        print("No images to read")
        print("Press a button to exit")
        s = input()
        sys.exit(0)
    return dir_list


def image_selection(dir_list) -> int:
    seleccion_correcta: bool = False

    while not seleccion_correcta:
        print("Choose your image:")
        for i in range(0, len(dir_list)):
            print("{0} - {1}".format(i, dir_list[i]))
        print("")
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(dir_list)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
            sys.exit(0)
        else:
            print_header()
            print("Please, choose a valid option")


def detection_system() -> int:
    seleccion_correcta = False

    values = [member.value for member in Enums.OCR]
    names = [member.name for member in Enums.OCR]

    while not seleccion_correcta:
        print_header()
        print("Choose detection system:")
        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        print("")
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(values)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
            sys.exit(0)
        else:
            print_header()
            print("Please, choose a valid option")


def language_selection() -> int:
    seleccion_correcta= False

    values = [member.value for member in Enums.supported_languages]
    names = [member.name for member in Enums.supported_languages]

    while not seleccion_correcta:
        print_header()
        print("Choose language output:")
        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        print("")
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(values)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
            sys.exit(0)
        else:
            print_header()
            print("Please, choose a valid option")


if __name__ == "__main__":
    main()

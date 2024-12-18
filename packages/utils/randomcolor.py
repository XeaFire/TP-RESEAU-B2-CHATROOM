import random

class fg:
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


def generateRandomColor():
    colors = [
        fg.red, fg.green, fg.orange, fg.blue, fg.purple,
        fg.cyan, fg.lightgrey, fg.darkgrey, fg.lightred,
        fg.lightgreen, fg.yellow, fg.lightblue, fg.pink, fg.lightcyan
    ]
    return random.choice(colors)
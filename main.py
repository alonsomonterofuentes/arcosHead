"""
main.py
-------------
Main function of the program
"""

from Head import Head
import csv
# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

def main():
    represent_emotion("happy")

def represent_emotion(emotion):
    """Takes an emotion from a csv file and moves each servo to the requested
    position
    """
    emotion_file = open('emotions/' + str(emotion)+'.csv')
    reader = csv.reader(emotion_file)
    position = list(reader)
    #Removes first column of the matrix for order
    for i in range(0,6):
        del position[i][0]
    
    for i in range(0,len(position[0])):
        print 1
        Head.left_antenna.write((position[0][i]))

if __name__ == "__main__":
    main()

######################################################################
# Authors: Luke Wilson
# Usernames: wilsonl
# P01
# Purpose: Uses GUIs and key handles for user to use in a choose your own adventure
######################################################################
# Acknowledgements:
# Code for closing windows: https://stackoverflow.com/questions/16406669/can-i-close-the-current-open-window-python
# Code for winsound: https://stackoverflow.com/questions/43679631/python-how-to-change-audio-volume
# Code for turtle shapes: https://stackoverflow.com/questions/59126255/how-to-play-gifs-using-turtle-module-in-python
# Song I used: https://www.youtube.com/watch?v=rMudHClToL0&ab_channel=piplupwater
####################################################################################
import story
import time
import sys                                      # import the classes we need
import winsound
winsound.PlaySound("monke_song.wav", winsound.SND_ASYNC)            # program plays some funky tunes
stage = 1
s = story.story()


def lose():
    """Displays a screen that tells the user they lost"""
    global stage            # if user picks the wrong choice then they get te lose screen, window will close
    s.lose()
    time.sleep(5)           # after 5 seconds the window closes
    sys.exit()


def main():                # main function compiles all stage methods to create one big story
    """compiles a story using the story methods"""
    global stage           # global variable used to switch between phases
    if stage == 1:
        s.stage_1()
        stage = 2
    elif stage == 2:
        s.stage_2()
        stage = 3
    elif stage == 3:
        s.stage_3()
        stage = 4
    elif stage == 4:
        s.stage_4()
        stage = 5
    elif stage == 5:
        s.stage_5()
        stage = 6
    elif stage == 6:
        s.stage_6()
        stage = 7
    elif stage == 7:
        s.stage_7()
        stage = 8
    elif stage == 8:
        s.stage_8()
        stage = 9
    elif stage == 9:                        # win screen
        s.stage_9()
        time.sleep(5)                       # after 5 seconds the window closes
        sys.exit()
    s.wn.onkey(main, '1')                   # key handles used for user to go from one stage to the next
    s.wn.onkey(lose, '2')
    s.wn.listen()
    s.wn.mainloop()


if __name__ == "__main__":
    main()

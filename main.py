# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:53:20 2021

@author: tebib
"""
import cv2
import game
import app as api
if __name__ == '__main__':
    # create an interactive window
    game = game.Game()
    # start the API
    api.start()
    
    while True:
        # update the interactive window frame
        game.run_game()
        # update the data to send to the API
        api.data = game.to_dict()
        # display the interactive window
        
        # Press Esc to quit the video analysis loop
        if cv2.waitKey(1) == 27:
            # Release video capture
            cv2.destroyAllWindows()
            break
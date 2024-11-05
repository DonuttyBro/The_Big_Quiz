from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random
import pandas as pd


dataFrame = pd.read_csv ('The Big Quiz\Trivia.csv')   
answer_list = dataFrame['Answer'].tolist()


class Game:
    
    def __init__(self): 
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        root.withdraw()
        self.game_gui = Toplevel()
        self.game_gui.iconbitmap("The Big Quiz\Quiz_Icon.ico")
        
        # If users press cross at top, closes help and 'releases' help button
        self.game_gui.protocol('WM_DELETE_WINDOW', partial(self.close_play))
        
        # Set up GUI Frame
        self.play_frame = Frame(self.game_gui, padx=10, pady=10)
        self.play_frame.grid()

        self.play_heading_label = Label(self.play_frame, text="Select a category below or type a number of randomized questions to answer.\n", font=("Arial", "10"), wraplength=320)
        self.play_heading_label.grid(row=0)

        self.question_amount = Entry(self.play_frame, font=("Arial", "14"))
        self.question_amount.grid(row=2, padx=10, pady=10)
 
        self.button_frame = Frame(self.play_frame)
        self.button_frame.grid(row=4)

        self.tv_movie = Button(self.button_frame, text="TV & Movie", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.tv_movie.grid(row=0, column=0, padx=5, pady=5)

        self.video_games = Button(self.button_frame, text="Video Games", bg="#009900", fg=button_fg, font=button_font, width=12)
        self.video_games.grid(row=0, column=1, padx=5, pady=5)

        self.general_trivia = Button(self.button_frame, text="General", bg="#CC6600", fg=button_fg, font=button_font, width=12)
        self.general_trivia.grid(row=1, column=0, padx=5, pady=5)

        self.horror_trivia = Button(self.button_frame, text="Horror", bg="#004C99", fg=button_fg, font=button_font, width=12)
        self.horror_trivia.grid(row=1, column=1, padx=5, pady=5)

        
    def close_play(self):
        
        # reshow root (ie: choose rounds) and end current game / allow new game to start
        root.deiconify()
        self.game_gui.destroy()
        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Big Quiz")
    root.iconbitmap("The Big Quiz\Quiz_Icon.ico")
    Game()
    root.mainloop()
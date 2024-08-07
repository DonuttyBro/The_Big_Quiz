from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random
import pandas as pd


dataFrame = pd.read_csv ('Trivia.csv')   
answer_list = dataFrame['Answer'].tolist()

class main:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="The Big Quiz", font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        subtitle_txt = "A Quiz by Vegas"
        self.subtitle_label = Label(self.intro_frame, text=subtitle_txt, wraplength=300)
        self.subtitle_label.grid(row=1)

        self.helpinfo_frame = Frame(self.intro_frame, padx=10, pady=5)
        self.helpinfo_frame.grid(row=2)

        support_buttons = [
            ["#FF8234" ,"Information", "get info"],
            ["#5E718B" ,"Help", "get help"]
        ]

        
        self.support_button_ref = []

        for item in range(0, 2):
            self.make_support_button = Button(self.helpinfo_frame, fg="#FFFFFF", bg=support_buttons[item][0], text=support_buttons[item][1], width=11, font=("Arial", "12", "bold"), command=lambda i=item: self.to_do(support_buttons[i][2]))

            self.make_support_button.grid(row=0, column=item, padx=5)

            # Add buttons to control list
            self.support_button_ref.append(self.make_support_button )

        # Access stats and help button so they can be enabled / disabled
        self.to_information_btn = self.support_button_ref[0]
        self.to_help_btn = self.support_button_ref[1]

        self.play_button = Button(self.intro_frame, font=("Arial", "18", "bold"), text="Play", bg="#CC6600", fg="#FFFFFF", width=16)
        self.play_button.grid(row=3, padx=10, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Big Quiz")
    root.iconbitmap("Quiz_Icon.ico")
    main()
    root.mainloop()
    
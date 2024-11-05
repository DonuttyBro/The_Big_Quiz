from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random
import pandas as pd

questions_answered = 0
answered_questions = []


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

        # Access info and help button so they can be enabled / disabled
        self.to_info_btn = self.support_button_ref[0]
        self.to_help_btn = self.support_button_ref[1]

        self.play_button = Button(self.intro_frame, font=("Arial", "18", "bold"), text="Play", bg="#CC6600", fg="#FFFFFF", width=16, command=lambda:Rounds())
        self.play_button.grid(row=3, padx=10, pady=10)

    def to_do(self, action):
        if action == "get help":
            self.get_help()
        elif action == "get info":
            self.get_info()
        else:
            self.close_main()

    def get_info(self):
        DisplayInfo(self)

    def get_help(self):
        DisplayHelp(self)


    def close_main(self):
        # reshow root (ie: choose rounds) and end current game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


class Rounds:
    
    def __init__(self): 
        
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")
        
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        root.withdraw()
        self.rounds_gui = Toplevel()
        self.rounds_gui.iconbitmap("The Big Quiz\Quiz_Icon.ico")
        
        # If users press cross at top, closes help and 'releases' help button
        self.rounds_gui.protocol('WM_DELETE_WINDOW', partial(self.close_rounds))
        
        # Set up GUI Frame
        self.rounds_frame = Frame(self.rounds_gui, padx=10, pady=10)
        self.rounds_frame.grid()

        self.rounds_heading_label = Label(self.rounds_frame, text="Select a category below or type a number of randomized questions to answer.\n", font=("Arial", "10"), wraplength=320)
        self.rounds_heading_label.grid(row=0)

        self.error_label = Label(self.rounds_frame, text="", font=("Arial", "10"), wraplength=320)
        self.error_label.grid(row=1)

        self.number_frame = Frame(self.rounds_frame)
        self.number_frame.grid(row=2)

        self.question_amount = Entry(self.number_frame, font=("Arial", "14"))
        self.question_amount.grid(row=0, column=0, pady=10)

        self.question_amount_confirm = Button(self.number_frame, text=">", font=button_font, width=2, command=lambda: self.start_game())
        self.question_amount_confirm.grid(row=0, column=1, pady=10)
 
        self.button_frame = Frame(self.rounds_frame)
        self.button_frame.grid(row=4)

        self.tv_movie = Button(self.button_frame, text="TV & Movie", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.tv_movie.grid(row=0, column=0, padx=5, pady=5)

        self.video_games = Button(self.button_frame, text="Video Games", bg="#009900", fg=button_fg, font=button_font, width=12)
        self.video_games.grid(row=0, column=1, padx=5, pady=5)

        self.general_trivia = Button(self.button_frame, text="General", bg="#CC6600", fg=button_fg, font=button_font, width=12)
        self.general_trivia.grid(row=1, column=0, padx=5, pady=5)

        self.horror_trivia = Button(self.button_frame, text="Horror", bg="#004C99", fg=button_fg, font=button_font, width=12)
        self.horror_trivia.grid(row=1, column=1, padx=5, pady=5)

    
    def rounds_check(self, min_val, maximum):
        
        has_error = "no"
        error = "Please enter a whole number between {} and {}".format(min_val, maximum)

        response = self.question_amount.get()

        try:
            response = int(response)

            if response < min_val:
                has_error = "yes"
            elif response > maximum:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # Sets var_has_error so that entry box and labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

    def start_game(self):
        self.rounds_check(1,100)

        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.error_label.config(fg="#9C0000")
            self.question_amount.config(bg="#F8CECC")
            self.error_label.config(text=output)

        else:
            self.error_label.config(fg="#004C00")
            self.question_amount.config(bg="#FFFFFF")
            total_questions=self.question_amount.get()
            self.rounds_gui.destroy()
            Play(self)

        

    def close_rounds(self):
        
        # reshow root (ie: choose rounds) and end current game / allow new game to start
        root.deiconify()
        self.rounds_gui.destroy()



class Play:
    def __init__(self, partner):
        
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        #self.get_question()

        self.play_gui = Toplevel()
        self.play_gui.iconbitmap("The Big Quiz\Quiz_Icon.ico")
        
        # If users press cross at top, closes help and 'releases' help button
        self.play_gui.protocol('WM_DELETE_WINDOW', partial(self.close_play))
        
        # Set up GUI Frame
        self.play_frame = Frame(self.play_gui, padx=10, pady=10)
        self.play_frame.grid()

        self.genre_label = Label(self.play_frame, text="Genre", font=("Arial", "12"), wraplength=320)
        self.genre_label.grid(row=0)

        self.question_label = Label(self.play_frame, text="Question\n", font=("Arial", "14"), wraplength=320)
        self.question_label.grid(row=1)

        self.answer_button_frame = Frame(self.play_frame)
        self.answer_button_frame.grid(row=3)

        self.answer_1 = Button(self.answer_button_frame, text="Answer", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.answer_1.grid(row=0, column=0, padx=5, pady=5)

        self.answer_2 = Button(self.answer_button_frame, text="Answer", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.answer_2.grid(row=0, column=1, padx=5, pady=5)

        self.answer_3 = Button(self.answer_button_frame, text="Answer", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)

        self.answer_4 = Button(self.answer_button_frame, text="Answer", bg="#990099", fg=button_fg, font=button_font, width=12)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)


    def get_question(self):
        
        rounds_played = 0
        questions_num = int(total_questions)
        
        file = open("The Big Quiz\Trivia.csv", "r")
        all_questions = list(csv.reader(file, delimiter=","))
        file.close()

        # remove the first row (header values)
        all_questions.pop(0)

        while questions_num != rounds_played:
    
            current_question = random.choice(all_questions)
            genre = current_question[0]
            question = current_question[1]
            answer = current_question[2]

            answer_list = [current_question[2], current_question[3], current_question[4], current_question[5]]

            random.shuffle(answer_list)

            #guess = 

            #if guess == answer:
                
            #elif guess != answer:
                
            rounds_played += 1
            all_questions.remove(current_question)
            

    def close_play(self):

        # reshow root (ie: choose rounds) and end current game / allow new game to start
        root.deiconify()
        self.play_gui.destroy()
        


class DisplayHelp:
    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#FFE6CC"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_btn.config(state=DISABLED)

        #If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help", font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Welcome to The Big Quiz!\n\nThere is 100 multi-choice questions overall that cover four different topics (Video Games, TV & Movie, Horror and General Trivia).\n\nYou may choose to do one category, each of which has 25 questions or you may type a number of questions to do from 1 to 100.\n\nQuestions from all categories will be used if you choose a specific amount of questions to do.\n\nHave Fun and enjoy the quiz!"
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal

        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()

class DisplayInfo:
    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#80F0C7"
        self.info_box = Toplevel()

        # Disable Information button
        partner.to_info_btn.config(state=DISABLED)

        #If users press cross at top, closes help and 'releases' help button
        self.info_box.protocol('WM_DELETE_WINDOW', partial(self.close_info, partner))
        
        self.info_frame = Frame(self.info_box, width=300, height=200, bg=background)
        self.info_frame.grid()

        self.info_heading_label = Label(self.info_frame, bg=background, text="Information", font=("Arial", "14", "bold"))
        self.info_heading_label.grid(row=0)

        info_text = "The Big Quiz was created by Vegas Hart.\nIt was made for a Yr13 programming assessment.\nAll questions were custom made and may be out of date after 2024.\n\nWHY ARE YOU READING THIS??\n\nPLAY THE QUIZ!!\n"
        self.info_text_label = Label(self.info_frame, bg=background, text=info_text, wraplength=350, justify="left")
        self.info_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.info_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#4B6FBD", fg="#FFFFFF", command=partial(self.close_info, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_info(self, partner):
        # Put help button back to normal

        partner.to_info_btn.config(state=NORMAL)
        self.info_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Big Quiz")
    root.iconbitmap("The Big Quiz\Quiz_Icon.ico")
    main()
    root.mainloop()
    
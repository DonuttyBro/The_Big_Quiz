from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random
import pandas as pd


dataFrame = pd.read_csv ('Trivia.csv')   
answer_list = dataFrame['Answer'].tolist()
print(answer_list)



        
import csv
import random

file = open("The Big Quiz\Trivia.csv", "r")
all_questions = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_questions.pop(0)

# Get the first 50 rows (used to develop colour buttons for play GUI)
# print(all_questions)

print("Length: {}".format(len(all_questions)))

current_question = random.choice(all_questions)
genre = current_question[0]
question = current_question[1]
answer = current_question[2]

answer_list = [current_question[2], current_question[3], current_question[4], current_question[5]]

random.shuffle(answer_list)
print(genre)
print(question)
print(answer_list)
print(answer)
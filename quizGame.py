import requests
import json
import random
import html

total_rounds = 0
correct_score = 0
wrong_score = 0
game_control = True

def category_func():
    category_ = input(""" Please input the game category in decimals or 'more' to see more category:\n
    9 for general knowledge\n
    10 for entertainment: Books\n
    11 for entertainment: film\n
    12 for entertainment: music\n
    13 for entertainment: musicala and theatres\n
    more for more category
    """
                     )
    if category_ == 'more':
        category_ = input("""
    14 for entertainment: television\n
    15 for entertainment: video games\n
    16 for entertainment: board games\n
    17 for science & nature\n
    18 for science: computers\n
    more for more category
    """
              )
    if category_ == 'more':
        category_ = input("""
    19 for science: mathematics\n
    20 for mythology\n
    21 for sports\n
    22 for geography\n
    23 for history\n
    24 for politics\n
    """
                     )
    return category_

category = category_func()

data_valid = False
while data_valid != True:
    if category == 'more':
        print('######################################')
        print('Please choose the right category in decimals ("more" is not a category)')
        print('######################################\n')
        category = category_func()
    if category.isdecimal():
        if 8 < int(category) < 25:
            data_valid = True
        else:
            print('######################################')
            print('Please choose the right category. Category ranges from 9 - 24')
            print('######################################\n')
            category = category_func()
    else:
        print('######################################')
        print('Please choose the right category only.')
        print('######################################\n')
        category = category_func()

difficulty = input('\nPlease input the difficulty level. Select from this list: EASY, MEDIUM or DIFFICULTY ')

data_valid = False
while data_valid != True:
    if difficulty.isalpha():
        if difficulty.lower() == 'easy':
            print(f'You have chosen {difficulty} level\n')
            print('######################################')
            print('Fetching the question...')
            print('######################################\n')
            data_valid = True
        elif difficulty.lower() == 'medium':
            print(f'You have chosen {difficulty} level\n')
            print('######################################')
            print('Fetching the question...')
            print('######################################\n')
            data_valid = True
        elif difficulty.lower() == 'difficulty':
            print(f'You have chosen {difficulty} level\n')
            print('######################################')
            print('Fetching the question...')
            print('######################################\n')
            data_valid = True
        else:
            print('######################################')
            print('Please choose the correct difficulty level (EASY, MEDIUM or DIFFICULTY).')
            print('######################################\n')
            difficulty = input('\nPlease input the difficulty level. Select from this list: EASY, MEDIUM or DIFFICULTY ')
    else:
        print('######################################')
        print('The difficulty level should be alphabets (EASY, MEDIUM or DIFFICULTY).')
        print('######################################\n')
        difficulty = input('\nPlease input the difficulty level. Select from this list: EASY, MEDIUM or DIFFICULTY ')


url = f'https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty.lower()}&type=multiple'

while game_control:
    data = requests.get(url)
    if data.status_code != 200:
        print("Error! Data couldn't be successfully fetched")
        continue
    else:
        text = json.loads(data.text)
        question = text['results'][0]['question']
        print(html.unescape(question) + '\n')
        print('----------------------------')
        correct_answer = text['results'][0]['correct_answer']
        incorrect_answers = text['results'][0]['incorrect_answers']
        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)
        number = 97

        for option in incorrect_answers:
            print(chr(number),'-',html.unescape(option))
            number += 1
        print('----------------------------', '\n')
        answer = input('Please choose between the following options: a, b, c, and d. ')
        data_valid = False
        
        while data_valid != True:
            try:
                ord(answer)
                if 97 <= ord(answer.lower()) <= 100:
                    data_valid = True
                else:
                    print('Invalid answer!\n')
                    answer = input('Please choose between the following options: a, b, c, and d. ')
                    continue
            except:
                 print('Invalid answer!\n')
                 answer = input('Please choose between the following options: a, b, c, and d. ')
                 continue

        #answer = ord(input('Please choose between the following options: a, b, c, and d. ').lower())
        index = ord(answer.lower()) - 97
        if incorrect_answers[index] == correct_answer:
            print(f'\nThats great! {html.unescape(correct_answer)} was the right answer')
            print('----------------------------','\n')
            correct_score += 1
        else:
            print(f'\nOops! {html.unescape(incorrect_answers[index])} was wrong. The right answer is {html.unescape(correct_answer)}')
            wrong_score += 1
            print('----------------------------','\n')
        print('----------------------------')
        total_rounds += 1
        play_again = input('Play again? (yes or no) ')
        if play_again.lower() == 'yes':
            pass
        else:
            game_control = False
print('\n######################')
print('Your score is: ')
print(f'Correct answers -> {correct_score}')
print(f'Incorrect answers -> {wrong_score}')
print('########################')
    

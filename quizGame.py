import requests
import json
import random
import html

total_rounds = 0
correct_score = 0
wrong_score = 0
game_control = True
url = 'https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple'

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
        play_again = input('Play again? ')
        if play_again.lower() == 'yes':
            pass
        else:
            game_control = False
print('\n######################')
print('Your score is: ')
print(f'Correct answers -> {correct_score}')
print(f'Incorrect answers -> {wrong_score}')
print('########################')
    

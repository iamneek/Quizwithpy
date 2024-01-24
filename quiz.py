import requests
import random
import survey
import html
import sys
import os
from colorama import init, Back, Fore, Style

init(autoreset=True)

points = 0
quest = 0
answers = []
all_correct_answers = []
def fetchQuestion (cat, diff):
    categ = cat
    r = requests.get(f'https://opentdb.com/api.php?amount=10&category={categ}&difficulty={diff}&type=multiple')
    if(r.status_code == 200):
        return r
    else:
        return 500


def getQuestion(cat=18, diff='easy'):
    QuestionObj = fetchQuestion(cat, diff)
    return QuestionObj

def play(cate, diff):
    global points
    global quest
    if (diff == 1):
        diff = "easy"
    else:
        diff = "hard"
    QuestionObj = getQuestion(cate, diff)
    for i in range(0, 10):
        quest += 1
        question = QuestionObj.json()["results"][i]["question"]
        question = html.unescape(question)
        answer = QuestionObj.json()["results"][i]["correct_answer"]
        answer = html.unescape(answer)
        answers.append(answer)
        options_r = QuestionObj.json()["results"][i]["incorrect_answers"]
        options_r.append(answer)
        options_r = [html.unescape(option) for option in options_r]
        options = random.sample(options_r, len(options_r))
        print("\n")
        index = survey.routines.select(question+" ",
                                options=options,
                                focus_mark='👉 ',
                                evade_color=survey.colors.basic('white'))    
        if(options[index] == answer):
            points += 1
            all_correct_answers.append(answer)


if __name__ == "__main__":
    try:
        os.system('cls')
        print(f"{Style.BRIGHT}Welcome to the quiz, Please select a category to be quizzed:\n")
        categories = ['Computer Science 💻', 'General Knowledge 🧠', 'Books 📚', 'Film 🎬', 'Music 🎧', 'Vehicle 🏎️', 'Gadgets ⚙️  ( Only Easy Mode Avail Till Now )']
        cats = survey.routines.select(
                                options=categories,
                                focus_mark='👉 ',
                                evade_color=survey.colors.basic('green'))
        match cats:
            case 0:
                cate = 18
            case 1:
                cate = 9
            case 2:
                cate = 10
            case 3:
                cate = 11
            case 4:
                cate = 12
            case 5:
                cate = 28
            case 6:
                cate = 30
            case _:
                cate = 18
        diffi = input(f"\n{Style.BRIGHT}Choose Difficulty 1 for easy, 2 for hard: ")
        if diffi == "":
            diffi = 1
        diffi = int(diffi)
        print(f"\nWoah! You chose hard, cool... Let's See what you come up with 😎" if diffi == 2 else f"\nYou chose easy questions. Best Of Luck Mate! 👍")
        if cate == 30:
            if diffi != 1:
                print(f"\n\n⚠️  {Style.BRIGHT}{Fore.BLACK}{Back.YELLOW}Oops Only Easy Mode Available For Gadgets soldier{Style.RESET_ALL} 🥲")
                diffi = 1
        play(cate = cate, diff=diffi)

        print(f"These Are The Correct Answers:\n")
        for userans in answers:
            if userans in all_correct_answers:
                print(f"✅ {Style.BRIGHT}Correct Answer! {Fore.GREEN + userans}")
            else:
                print(f"❌ {Style.BRIGHT}The Answer Was: {Fore.RED + userans}")
        print("")
        if(points <= 4):
            print(f"\n{Style.BRIGHT}Sorry Mate! You scored {Back.LIGHTRED_EX} {points} points {Style.RESET_ALL}{Style.BRIGHT} only :(, Prepare well next time :D \n")


        elif(points > 4 and points < 8):
            print(f"\n{Style.BRIGHT}Good Job! Mate you scored {Fore.BLACK}{Back.LIGHTYELLOW_EX} {points} points {Style.RESET_ALL}{Style.BRIGHT}.\n")


        else:
            print(f"\n{Style.BRIGHT}You scored an excellent score {Back.LIGHTGREEN_EX} {points} points {Style.RESET_ALL}{Style.BRIGHT}. Congratulations Mate\n")
        

    except KeyboardInterrupt:
        print(f"\n{Style.BRIGHT}Quiz interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"{Style.BRIGHT}An Error Occurred...")
        print(e)
        sys.exit(1)
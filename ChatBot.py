from difflib import  get_close_matches
import random

def get_best_match(user_question:str,questions:dict)-> str|None:

    questions:list[str] = [q for q in questions]
    matches:list = get_close_matches(user_question,questions,n=1,cutoff=0.6)


    if matches:
            #print(f"{matches}")

        return  matches[0]
    return None


def chat_bot(knowledge:dict):
    while True:
        user_input : str = input('You: ')
        best_match : str|None = get_best_match(user_input,knowledge)

        if user_input.lower() == 'bye':
            print('Bot:', knowledge.get('Bye', 'Goodbye!'))
            break

        elif answer:= knowledge.get(best_match):
            print(f'Bot: {answer}')
        # elif user_input == 'Bye':
        #     break
        else:
            print('Bot : I do not understand....')



def main():
    brain : dict = {'Hello': random.choice(['Hey there!! 😊', 'Hello friend! 👋', 'Yo!']),
                    'Hi' :  random.choice(['Hey there!! 😊', 'Hello friend! 👋', 'Yo!']),
                    'who are you': 'I am your friendly Python chatbot 🤖!',
                    'what is your name': 'You can call me PyBot!',
                    'How are you': 'I am doing superb, What about you?',
                    'What time is it': 'don\t know even I don\t care also🙂',
                    'Bye' : random.choice(['See you soon 👋', 'Catch you later!', 'Goodbye! 👻']),
                    'what is python': 'Python is a popular high-level programming language known for its readability and simplicity.',
                    'what is AI': 'AI stands for Artificial Intelligence, which enables machines to mimic human behavior.'
                    }


    chat_bot(knowledge=brain)

if __name__ == '__main__':
    main()

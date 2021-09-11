from PyInquirer import prompt

from scripts.commands import update_animes

questions = [
    {
        'type': 'list',
        'name': 'command',
        'message': 'What do you want to do?',
        'choices': [
            {
                'value': 'update_animes',
                'name': 'Update animes',
            },
            {
                'value': 'exit',
                'name': 'Exit',
            }
        ]
    },
]


def main():
    print("Hi, welcome to Alm CLI")

    while True:
        answers = prompt(questions)
        command = answers.get("command")

        if command == "update_animes":
            update_animes.run()
        elif command == "exit":
            break
        else:
            print("Option not available")


if __name__ == "__main__":
    main()

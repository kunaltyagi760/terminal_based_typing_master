import random
import time
import json


def update_leaderboard(username, wpm):
    # Load existing leaderboard
    leaderboard = load_leaderboard()

    # Update or add user to the leaderboard
    leaderboard[username] = wpm

    # Sort the leaderboard by WPM in descending order
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=False))

    # Save the updated leaderboard to the JSON file
    with open('leaderboard.json', 'w') as f:
        json.dump(sorted_leaderboard, f)

def show_leaderboard():
    # Load and display the leaderboard
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    for i, (user, wpm) in enumerate(leaderboard.items(), start=1):
        print(f"{i}. {user}: {wpm} WPM")

def load_leaderboard():
    # Load leaderboard from JSON file or create an empty one
    try:
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = {}
    return leaderboard

def load_paragraph():
    # Load a random paragraph for the typing test
    with open('typing_paragraphs.json', 'r') as f:
        paragraphs_data = json.load(f)
    return random.choice(paragraphs_data['paragraphs'])


def main():
    print("Welcome to Terminal Typing Master!")

    # Get username
    username = input("Enter your username: ")

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Start Typing Test
            paragraph = load_paragraph()
            print("\nType the following paragraph:\n")
            print(paragraph)
            input("\nPress Enter when you are ready to start typing...")

            start_time = time.time()
            user_input = get_user_input()
            end_time = time.time()

            # Calculate words per minute (WPM)
            time_taken = end_time - start_time
            words_typed = len(user_input.split())
            wpm = int((words_typed / time_taken) * 60)

            print(f"\nTime Taken: {round(time_taken)}")
            print(f"Words Typed: {words_typed}")
            print(f"Your WPM: {wpm}")
            update_leaderboard(username, wpm)

        elif choice == '2':
            # Show Leaderboard
            show_leaderboard()

        elif choice == '3':
            # Exit
            print("Thanks for playing. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
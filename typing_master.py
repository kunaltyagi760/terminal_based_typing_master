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
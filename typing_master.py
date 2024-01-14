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
            category = input("Enter the typing category: ")  # You can add more categories
            words = load_words_from_json(category)

            start_time = time.time()
            user_input = get_user_input()
            end_time = time.time()

            # Calculate words per minute (WPM)
            time_taken = end_time - start_time
            words_typed = len(user_input.split())
            wpm = int((words_typed / time_taken) * 60)

            print(f"\nYour WPM: {wpm}")
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

main()
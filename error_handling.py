def error_message_prompt_and_exit(error_message: str) -> None:
    """
    Prints the error message and prompts the user to press Enter to exit the program.
    """
    print(error_message)
    input("Press Enter to exit...")
    exit(1)
    
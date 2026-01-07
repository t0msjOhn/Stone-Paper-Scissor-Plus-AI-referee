from game import resolve_round
from state import state
from referee import configure_model

def play_game():

    model = configure_model(resolve_round)
    chat = model.start_chat(enable_automatic_function_calling=True)

    # Initial Rule Explanation
    response = chat.send_message("Start the game and explain rules.")
    print(f"Referee: {response.text}")

    while not state.game_over:
        user_input = input("You: ")
        response = chat.send_message(user_input)
        print(f"\nReferee: {response.text}")

    print("\n--- Game Terminated ---")


if __name__ == "__main__":
    play_game()
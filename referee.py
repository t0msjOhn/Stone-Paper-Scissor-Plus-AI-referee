import os
from dotenv import load_dotenv
import google.generativeai as genai


def configure_model(resolve_round_callable):
    """Configure and return a GenerativeModel configured as the game referee.
    The caller must pass the local `resolve_round` function as a tool.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")

    genai.configure(api_key=api_key)

    tools = [resolve_round_callable]
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        tools=tools,
        system_instruction=(
            "You are a Game Referee for Rock-Paper-Scissors-Plus. "
            "Rules: Best of 3 rounds. Moves: Rock, Paper, Scissors, and one-time Bomb. "
            "Bomb beats everything; Bomb vs Bomb is a draw. Invalid moves waste a round. "
            "Explain rules in < 5 lines, then ask for a move. Use 'resolve_round' for every move. "
            "After Round 3, announce the final winner and stop."
        )
    )

    return model

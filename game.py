import random
from state import state

def resolve_round(user_move: str) -> str:
    """
    Validates the move, simulates the bot move, and updates game state.
    Args:
        user_move: The move chosen by the user (rock, paper, scissors, bomb).
    """
    if state.game_over:
        return "The game is already over."

    # 1. Bot Move Logic
    possible_moves = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        possible_moves.append("bomb")
    
    bot_move = random.choice(possible_moves)
    if bot_move == "bomb":
        state.bot_bomb_used = True

    # 2. Validation & Normalization
    valid_moves = ["rock", "paper", "scissors", "bomb"]
    user_move_clean = user_move.lower().strip()
    
    # Handle Invalid Input or Double Bombing
    invalid_reason = None
    if user_move_clean not in valid_moves:
        invalid_reason = f"'{user_move}' is an invalid move."
    elif user_move_clean == "bomb" and state.user_bomb_used:
        invalid_reason = "You already used your bomb!"

    if invalid_reason:
        state.round_number += 1
        if state.round_number > 3:
            state.game_over = True
        return f"Result: Invalid move ({invalid_reason}). Round wasted. Bot played {bot_move}."

    if user_move_clean == "bomb":
        state.user_bomb_used = True

    # 3. Win Logic
    rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    
    if user_move_clean == bot_move:
        result = "Draw"
    elif user_move_clean == "bomb":
        result = "User Wins"
    elif bot_move == "bomb":
        result = "Bot Wins"
    elif rules[user_move_clean] == bot_move:
        result = "User Wins"
    else:
        result = "Bot Wins"

    # 4. Update State
    if result == "User Wins":
        state.user_score += 1
    if result == "Bot Wins":
        state.bot_score += 1
    
    curr_round = state.round_number
    state.round_number += 1

    if state.round_number > 3:
        state.game_over = True

    return (f"Round {curr_round}: User played {user_move_clean}, Bot played {bot_move}. "
            f"Result: {result}. Current Score: User {state.user_score} - Bot {state.bot_score}")

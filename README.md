# Stone Paper Scissor Plus — AI Referee

A small interactive command-line Rock-Paper-Scissors game with an AI referee powered by Google's AI. The referee explains the rules, prompts for moves, calls the function `resolve_round` to evaluate each round, and announces the final winner after the best-of-3 session.

**Features**
- **Best of 3:** First to win more rounds after 3 rounds wins the match.
- **Bomb move:** Each player (user and bot) can use `Bomb` exactly once — it beats the other moves.
- **AI Referee:** Uses the `google ai` client to present rules and drive the interactive chat loop.

**Python dependencies**
- python-dotenv
- google-generative-ai

You can install them with:
pip install python-dotenv google-generative-ai


**Setup**
1. Create a `.env` file in the project root with your API key:


GOOGLE_API_KEY=your_api_key_here


2. Verify `main.py` is present in the project root.

**Running the game**
1. Run the script:

python main.py


2. The AI referee will explain the rules and then prompt you. Type one of:
- `rock`
- `paper`
- `scissors`
- `bomb` (only allowed once per player)

3. Invalid moves or using `bomb` more than once will waste the current round. The game automatically ends after 3 rounds and the referee announces the final winner.

**Gameplay notes**
- Moves are case-insensitive and trimmed of surrounding whitespace.
- The bot also gets one `bomb` which it may use randomly.
- A `bomb` vs `bomb` is treated as a draw.
- The script keeps a simple `GameState` in memory and is intended for a single interactive session.

**Files**
- `main.py`: Main game script and AI referee.
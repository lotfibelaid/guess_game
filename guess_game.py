import random

WORDS = [
    "driver", "lernen", "signature", "Bahnhof", "history", "Bitte",
    "response", "president", "highway", "computer", "helfen",
    "appartment", "Hallo", "forest", "chocolat", "Sonne", "lawyer",
    "Belegung", "Polizei"
]


def obscured_word(word: str, blanks: int = 3) -> str:
    """Return the word with a few random letters replaced by underscores."""
    blanks = min(blanks, len(word))
    positions = random.sample(range(len(word)), blanks)
    result = list(word)
    for pos in positions:
        result[pos] = '_'
    return ''.join(result)


def play():
    """Run the guessing game from the command line."""
    words = WORDS[:]
    random.shuffle(words)
    score = 0
    for word in words:
        masked = obscured_word(word)
        print(f"Guess the word: {masked}")
        guess = input("Your guess: ").strip()
        if guess.lower() == word.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct word was: {word}\n")
    print(f"Game over! You guessed {score}/{len(words)} words correctly.")


if __name__ == "__main__":
    play()

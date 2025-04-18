def detect_mood(message):
    mood_map = {
        "happy": ["happy", "joy", "excited", "great", "awesome"],
        "sad": ["sad", "down", "low", "depressed", "cry"],
        "angry": ["angry", "mad", "furious", "annoyed"],
        "love": ["love", "like", "heart", "crush"],
    }

    emoji_map = {
        "happy": "😄",
        "sad": "😢",
        "angry": "😡",
        "love": "❤"
    }

    message = message.lower()
    for mood, keywords in mood_map.items():
        for word in keywords:
            if word in message:
                return f"{mood.capitalize()}! {emoji_map[mood]}"
    
    return "Neutral. 😐"

# Example usage
msg = input("How are you feeling? ")
print(detect_mood(msg))
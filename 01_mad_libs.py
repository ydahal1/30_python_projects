def get_input(word_type:str):
    word_type = input(f"Type a {word_type}: ")
    return word_type

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once there was {noun1}. He loved doing {verb1} and {verb2} with {noun2}
"""

print(story)
full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    
    if not isinstance(character_name, str):
        return "The character name should be a string"

    elif character_name == "":
        return "The character should have a name"

    elif len(character_name) > 10:
        return "The character name is too long"
    
    elif " " in character_name:
        return "The character name should not contain spaces"
    
    stats = (strength, intelligence, charisma)

    if not all(isinstance(stat, int) and not(isinstance(stat, bool)) for stat in stats):
        return "All stats should be integers"

    elif any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    elif any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    def bar(value):
        return (full_dot * value) + (empty_dot * (10 - value))
    
    return (
            f"{character_name}\n"
            f"STR {bar(strength)}\n"
            f"INT {bar(intelligence)}\n"
            f"CHA {bar(charisma)}"
    )
    

        
print(create_character("ren", 4, 2, 1))
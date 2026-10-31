def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        lines = poem.split("\n")
        secret_code = ""
        
        for index, line in enumerate(lines):
            words = line.split()
            if index >= len(words):
                secret_code += "0"
            else:
                secret_code += str(len(words[index]))
                
        secret_codes.append(secret_code)
    return secret_codes




poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
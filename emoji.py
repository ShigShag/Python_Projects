msg = input("> ")


def emoji_converter(msg):
    words = msg.split(' ')
    emojis = {
        ":)": ":))",
        ":(": ":((",
        ":/": ":()"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter(msg))

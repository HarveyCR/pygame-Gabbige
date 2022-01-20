import random


def get_word(language, difficulty, p_speech):
    if language == "rus":
        f_name = 'rus'
    elif language == "eng":
        f_name = 'eng'
    else:
        print('ERROR: get_word(): Wrong "language=="', language)
        return ""

    p_sp = []
    if "n" in p_speech:
        p_sp.append("_n")
    elif "v" in p_speech:
        p_sp.append("_v")

    if len(p_sp) == 0:
        print('ERROR: get_word(): Wrong "p_speech=="', p_speech)
        return ""

    # return f_name

    if difficulty == 0:
        a = 1
        b = 4
    elif difficulty == 1:
        a = 5
        b = 8
    elif difficulty == 2:
        a = 9
        b = 99
    else:
        print('ERROR: get_word(): Wrong "difficulty=="', difficulty)
        return ""

    a += len("\n")
    b += len("\n")
    words = []
    for v in p_sp:
        f = f_name + v + ".txt"
        with open(f, encoding="utf8") as file_txt:
            w = [s.strip("\n") for s in file_txt if a <= len(s) <= b]
            words.extend(w)
            w = []
    # print(len(words))
    rez = random.choice(words)

    words = []
    return rez


if __name__ == '__main__':
    print(get_word('rus', 0, 'nv'))
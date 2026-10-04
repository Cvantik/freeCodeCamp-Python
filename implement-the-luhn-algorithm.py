def verify_card_number(card_number:str):
    total = 0
    just_numbers = card_number.replace(" ", "").replace("-", "")
    reversed_number = just_numbers[::-1]
    for i in range(len(reversed_number)):
        number = int(reversed_number[i])
        if i % 2 == 1:
            number = number * 2
            if number > 9:
                number -= 9
        total += number
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
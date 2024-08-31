def count_letter_a(str):
    count = 0
    for char in str.lower():
        if char == 'a':
            count += 1
    return count

print(count_letter_a(input("Digite uma string: ")))
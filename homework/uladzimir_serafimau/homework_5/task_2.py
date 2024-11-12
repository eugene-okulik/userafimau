results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]
for result in results:
    number_str = result[result.index(':') + 2:]
    number = int(number_str)
    total = number + 10
    print(total)
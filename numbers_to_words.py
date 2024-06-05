def numbers_to_words(n):
    if n == '0':
        return 'zero'
    elif not str(n).isnumeric():
        raise TypeError
    elif len(str(n)) > 51:
        raise ValueError

    ones = ['one','two','three','four','five','six','seven','eight','nine',
            'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
            'seventeen','eighteen','nineteen']
    tens = ['twenty','thirty','forty','fifty','sixty','seventy',
            'eighty','ninety']
    suffix = ['thousand','million','billion','trillion','quadrillion',
              'quintillion','sextillion','septillion','octillion','nonillion',
              'decillion','undecillion','duodecillion','tredecillion',
              'quatttuor-decillion','quindecillion']

    def length(n, zeros):
        if len(n) in zeros or len(n) < 4:
            return zeros
        zeros = list(map(lambda x: x+3, zeros))
        return length(n, zeros)

    n = int(str(n).replace(',',''))
    zeros = length(str(n), [4, 5, 6])
    max_num = int('1' + '0' * max(zeros))
    num = max_num // 1000 if max_num > 1000 else 1000

    if n < 20:
        return ones[n - 1]
    if n < 100:
        return tens[n // 10 - 2] + (f'-{ones[n % 10 - 1]}' if (n % 10 != 0) else '')
    if n < 1000:
        return f'{ones[n // 100 - 1]}-hundred' + (f' and {numbers_to_words(n % 100)}'
        if n % 100 != 0 else '')
    if n < max_num:
        for i in suffix:
            i = (min(zeros) // 3) - 1
        return numbers_to_words(n // num) + f' {suffix[i]}' + (', '
        if n % num != 0 else '') + (numbers_to_words(n % num)
        if n % num != 0 else '')


def main():
    input_integer = input('Enter a max_num between 1 and 10e50: ')

    try:
        converted_str = numbers_to_words(input_integer)
        print(converted_str)
    except TypeError:
        print('Please enter an integer.')
        main()
    except ValueError:
        print('Please enter an integer that is 51 characters or less.')
        main()


if __name__ == '__main__':
    main()


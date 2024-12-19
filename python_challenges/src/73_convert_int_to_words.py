def number_to_words(num):
    if num == 0:
        return "zero"

    def one_to_nineteen(n):
        return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n]

    def tens(n):
        return ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n]

    def two_digit(n):
        if n < 20:
            return one_to_nineteen(n)
        else:
            return tens(n // 10) + ('' if n % 10 == 0 else ' ' + one_to_nineteen(n % 10))

    def three_digit(n):
        if n < 100:
            return two_digit(n)
        else:
            return one_to_nineteen(n // 100) + " hundred" + ('' if n % 100 == 0 else ' ' + two_digit(n % 100))

    result = ''
    if num >= 1000:
        result += three_digit(num // 1000) + " thousand "
        num %= 1000
    result += three_digit(num).strip()
    return result.strip()

# Example usage:
print("Number to Words:", number_to_words(123))

def _check_valid(candidate_number) -> bool:
    candidate_number = str(candidate_number)
    return len(candidate_number) == 16 and candidate_number.isdigit()

def _clean_input(candidate_number) -> str:
    return ''.join(filter(str.isdigit, str(candidate_number)))

def _handle_two_digit(two_digit) -> int:
    return sum(int(digit) for digit in str(two_digit))

def valid_number(candidate_number) -> bool:
    candidate_number = _clean_input(candidate_number)
    if not _check_valid(candidate_number):
        return False

    double_list = []
    reversed_digits = reversed(candidate_number)

    for i, digit in enumerate(reversed_digits):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit = _handle_two_digit(digit)
        double_list.append(digit)
    
    return sum(double_list) % 10 == 0

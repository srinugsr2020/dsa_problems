"""Classify positive signed 32-bit integers by their digit-square orbit."""


def digit_square_sum(number):
    total = 0
    while number:
        number, digit = divmod(number, 10)
        total += digit * digit
    return total


def require_in_range(number):
    if not 1 <= number <= 2**31 - 1:
        raise ValueError("expected a positive signed 32-bit integer")


def happy_with_history(number):
    require_in_range(number)
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = digit_square_sum(number)
    return number == 1


def happy_with_decimal_digits(number):
    require_in_range(number)
    # Every nonhappy positive base-10 orbit enters the cycle containing 4.
    while number not in (1, 4):
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


def happy_with_floyd(number):
    require_in_range(number)
    slow = fast = number
    while True:
        slow = digit_square_sum(slow)
        fast = digit_square_sum(digit_square_sum(fast))
        if slow == fast:
            return slow == 1


if __name__ == "__main__":
    for solve in (happy_with_history, happy_with_decimal_digits, happy_with_floyd):
        assert solve(1) and solve(13) and solve(1000)
        assert not solve(2) and not solve(4) and not solve(16)
        assert not solve(2**31 - 1)
        for invalid in (0, -13, 2**31):
            try:
                solve(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Accepted an out-of-range integer: {invalid}")

    # Ten digits reduce to at most 10 * 81. Check that finite range for the shortcut.
    for start in range(1, 811):
        current = start
        for _ in range(811):
            if current in (1, 4):
                break
            current = digit_square_sum(current)
        else:
            raise AssertionError(f"Unexpected digit-square orbit: {start}")
        assert happy_with_decimal_digits(start) == happy_with_floyd(start)

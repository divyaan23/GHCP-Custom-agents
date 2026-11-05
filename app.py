"""Ahoy! Print the numbers from 1 through 10, one per line."""


def main() -> None:
    """Write the complete number sequence to standard output."""
    # Arrr! The exclusive stop at 11 keeps 10 aboard the printed sequence.
    for number in range(1, 11):
        print(number)


# Ahoy! Run only when launched directly, not when imported by another module.
if __name__ == "__main__":
    main()

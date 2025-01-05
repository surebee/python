def calculate_federal_tax(income):
    """
    Calculate federal tax based on 2023 tax brackets for single filers.
    """
    federal_brackets = [
        (0, 10275, 0.10),  # 10% on income up to $10,275
        (10275, 41775, 0.12),  # 12% on income $10,276–$41,775
        (41775, 89075, 0.22),  # 22% on income $41,776–$89,075
        (89075, 170050, 0.24),  # 24% on income $89,076–$170,050
        (170050, 215950, 0.32),  # 32% on income $170,051–$215,950
        (215950, 539900, 0.35),  # 35% on income $215,951–$539,900
        (539900, float('inf'), 0.37)  # 37% on income over $539,900
    ]

    tax = 0
    for lower, upper, rate in federal_brackets:
        if income > lower:
            taxable = min(income, upper) - lower
            tax += taxable * rate
        else:
            break
    return tax


def calculate_maryland_state_tax(income):
    """
    Calculate Maryland state tax based on 2023 state brackets for single filers.
    """
    maryland_brackets = [
        (0, 1000, 0.02),  # 2% on income up to $1,000
        (1000, 2000, 0.03),  # 3% on income $1,001–$2,000
        (2000, 3000, 0.04),  # 4% on income $2,001–$3,000
        (3000, 100000, 0.0475),  # 4.75% on income $3,001–$100,000
        (100000, 125000, 0.05),  # 5% on income $100,001–$125,000
        (125000, 150000, 0.0525),  # 5.25% on income $125,001–$150,000
        (150000, 250000, 0.055),  # 5.5% on income $150,001–$250,000
        (250000, float('inf'), 0.0575)  # 5.75% on income over $250,000
    ]

    tax = 0
    for lower, upper, rate in maryland_brackets:
        if income > lower:
            taxable = min(income, upper) - lower
            tax += taxable * rate
        else:
            break
    return tax


def calculate_taxes(income):
    """
    Calculate both federal and Maryland state taxes.
    """
    federal_tax = calculate_federal_tax(income)
    maryland_tax = calculate_maryland_state_tax(income)
    total_tax = federal_tax + maryland_tax
    return federal_tax, maryland_tax, total_tax


if __name__ == "__main__":
    print("Single-Person Company Tax Calculator")
    try:
        income = float(input("Enter your taxable income ($): "))
        federal_tax, maryland_tax, total_tax = calculate_taxes(income)

        print(f"\nTax Summary for Income: ${income:,.2f}")
        print(f"Federal Tax: ${federal_tax:,.2f}")
        print(f"Maryland State Tax: ${maryland_tax:,.2f}")
        print(f"Total Tax: ${total_tax:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


#!/usr/bin/python3
def CalcSimpleInterest(Start, Rate, Time):
    Total = Start * (1+(Rate*Time))
    print(f"""
    {Total} = {Start}(1 + ({Rate} * {Time}))
    This is because simple interest is the intrest charge on borrowing, without any extra factors, and the rate never changes
    So, we multiply The starting ammount, {Start}, by {(1+(Rate*Time))}, or (1 + ({Rate} * {Time})) to get {Total}
""")
CalcSimpleInterest(float(input("Starting principle rate (no $ sign): ")), float(input("Rate (without % sign): " )), float(input("Time borrowing (years): ")))

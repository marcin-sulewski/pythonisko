month_days = {
    'january': 31, 'february': '28/29', 'march': 31, 'april': 30,
    'may': 31, 'june': 30, 'july': 31, 'august': 31,
    'september': 30, 'october': 31, 'november': 30, 'december': 31
}

month = input("Input the name of Month: ").lower()

if month in month_days:
    print("No. of days:", month_days[month], "days")
else:
    print("Invalid month input.")

from datetime import date
from datetime import datetime
import sys
import re
import inflect

def main():
    birth = birth_input()
    present = date.today()
    start_date = datetime.strptime(birth, '%Y.%m.%d')
    end_date = datetime(present.year, present.month, present.day)
    ymd = end_date - start_date
    if start_date > end_date: # hehehehe 
        sys.exit("are you even born ?")
    minutes = int(ymd.total_seconds() // 60)
    print(f"{date_pronounce(minutes)} minutes")

def date_pronounce(min):
    p = inflect.engine()
    mini = p.number_to_words(min)
    return mini

    
def birth_input():
    birth = input("Date of Birth: ").strip()
    if re.match(r'\b\d{4}\.\d{2}\.\d{2}\b', birth):
        return birth

    else:
        sys.exit("Invalid date")

...


if __name__ == "__main__":
    main()
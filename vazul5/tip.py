def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    import re
    d = re.sub(r"," , "." , d, 1 )
    
    dol = float( re.sub(r"[^ \d . ]" , "" , d))

    doll = f'{dol:.1f}'
    vége = float(doll)
    return vége
    # TOD


def percent_to_float(p):
    import re
    P = re.sub(r"," , "." ,p, 1)
    
    
    sz =float( re.sub(r"[^ \d.]" , "" , p))
    szszam = float(f'{sz : .1f}')
    szaz =float( szszam / 100)
    return(szaz)
    # TODO


main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6:
        return False
    first_2 = s[0:1]
    last_4 = s[2:5]
    digit = False
    ix = 1
    if first_2.isalpha():
        if  len(last_4) == 0:
            return True 
        if last_4.isalpha():
            return True
        for i in last_4:

            if i.isdigit() and digit == False and i == "0":
                return False
            if i.isdigit():
                digit = True
                if ix == len(last_4):
                    return True

            

            elif not i.isdigit() and not i.isalpha():
                return False
            elif i.isalpha()  and digit == True:
                return False
            ix += 1
            
    else:
        return False
    

if __name__ == "__main__":
    main()
            
        







        # for i in range(len(last_4)):
        #     if last_4[i].isalpha() and last_4[i + 1].isdigit() and last_4[i + 1] != '0':
        #         return True
        #     else:
        #         return False
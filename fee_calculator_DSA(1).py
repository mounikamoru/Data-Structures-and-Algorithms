#fee calculator
def calculate_fee(course,marks):
    if course== "AI":
        fee = 50000
    elif course =="web development":
        fee = 30000
    elif course == "Data sceince":
        fee = 40000
    else:
        return None #invalid course

    #discount condition
    if marks > 90:
        fee -= 5000
    return fee

def main():
    course= input("enter course:")
    marks = int(input("enter  marks:"))
    fee = calculate_fee(course,marks)
    if fee is None:
        print("invalid course selected")
    else:
        print("final fee:",fee)

main()

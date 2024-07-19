import learning

def main():
    p1 = learning.getPerson(name="徐國堂")
    print(p1.bmi_print())
    print("=============")
    p2 = learning.Person.getPerson(name="robert")
    print(p2.bmi_print())

if __name__ == '__main__':
    main()
   
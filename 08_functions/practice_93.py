## keyword argument

def repeat_word(string,num):
    for _ in range(num):
        print(string)

repeat_word("mohamed",4)
repeat_word(num=4,string="mohamed")
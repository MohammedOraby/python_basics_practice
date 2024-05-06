students = {
    "mohamed":{"test1":99,"test2":77},
    "ahmed":{"test1":88},
    "sara":{"test1":89,"test2":97},
    "ali":{"test2":98},
}

for student , test_result in students.items() :
    test_1 = test_result.get("test1",0)
    test_2 = test_result.get("test2",0)
    avg = (test_1+test_2)/2
    print(f"{student} gets {avg}")
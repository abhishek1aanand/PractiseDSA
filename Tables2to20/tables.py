for i in range(2, 21):
    with open(f"C:/Users/Abhishek/PRACTISE/Datastructure&Algo/PractiseDSA/Tables2to20//Multiplication_table_of_{i}", "w") as f:
        for j in range(1, 11):
            result = i * j
            f.write(f"{i}*{j} = {result}")
            if j!=10:
                f.write("\n")

# Programming Foundations with Python Course [CSGE601020]
# Faculty of Computer Science, University of Indonesia
# Odd Semester 2020/2021
# Programming Assignment 01
# Alfina Azaria - 2006482773

print("Programming Assignment 01")
print("===========================")
print("This program can convert a positive integer in decimal representation into hex representation and vice versa\n")

RunAgain = True          # RunAgain = untuk diulang2 terus pertanyaannya
                        # biar pengulangan terus menerus, makanya pake while
                        # nonstop sampe ketemu false nnti di pertanyaan terakhir2
while RunAgain == True :
    print("(1) From decimal to hexadecimal")
    print("-------------------------------")
    decInt = int(input("Give a positive integer in decimal representation: "))
    # untuk menyimpan bil. decimal yang di input oleh user

    # karena mau diitung jadi bentuknya harus integer

    prefixHex = "Ox"    # prefix hexadecimal
    hexstr = ""     # bikin variable buat nnti ditumpuk2 hexadecimalnya
    temp = decInt   # disimpen di temp biar nnti bisa muter terus
    while temp > 0 :
        hexdigit = temp % 16        # nama variable nya hexdigit soalnya hex msh dlm bentuk int/digit biar bisa di modulo
        # tambahin kondisi jika hexdigitnya lebih dr 10
        # itu yg membedakan binary dgn hexadecimal
        if hexdigit == 10 :         
            hexdigit = "A"
        elif hexdigit == 11 :
            hexdigit = "B"
        elif hexdigit == 12 :          # pake elif elif karena biar jd multi-way decision
            hexdigit = "C"              # kalo if else if else itu boros
        elif hexdigit == 13 :
            hexdigit = "D"
        elif hexdigit == 14 :
            hexdigit = "E"
        elif hexdigit == 15 :
            hexdigit = "F"
    
        hexstr = str(hexdigit) + hexstr     #skrg hexdigit di convert ke str
        temp = temp // 16
        # biar temp tetep ngebagi2 dgn 16 terus2an

    print("The hexadecimal representation of", decInt, "is", prefixHex+hexstr)
    # jangan lupa hexstr nya ditambahin prefix Ox

    print("\n")     #kasih enter, sesuai permintaan soal

    # hexadecimal to decimal
    print("(2) From hexadecimal to decimal")
    print("-------------------------------")

    # variable hexstr2 = untuk mengubah hex ke decimal
    hexstr2 = str(input("Give a positive integer in hexadecimal representation: "))

    temp = hexstr2[2:]      # string slicing untuk menghapus prefix Ox
    newIntDec = 0   # sbg accumulator buat nnti decimalnya dijumlah2in
                    # newIntDec = new Integer Decimal; karena nnti hasil akhirnya dlm bentuk integer

    # des > hex = numpuk2in string, hasil dr pembagian
    # hex > des = jumlah2in hasil operasinya

    length = len(temp)      # untuk tau brp panjang temp skrg
    for power in range (length) :
        decdigit_str = temp[-1]      # untuk mengambil 1 digit terkanan
                                # decdigit_str = decimal digit string
        if decdigit_str == "A" :
            decdigit_str = "10"
        elif decdigit_str == "B" :
            decdigit_str = "11"
        elif decdigit_str == "C" :
            decdigit_str = "12"
        elif decdigit_str == "D" :
            decdigit_str = "13"
        elif decdigit_str == "E" :
            decdigit_str = "14"
        elif decdigit_str == "F" :
            decdigit_str = "15"

        decdigit_Int = int(decdigit_str)   # decimal nya tadinya kan masih dalam bentuk string dari si hex, agar bisa dihitung harus diubah dulu ke int

        # hitungan penjumlahan decimal
        newIntDec = newIntDec + decdigit_Int * (16**power)      # kalo binary 2 pangkat, kl hex 16 pangkat
        temp = temp[:-1]        # untuk ngebuang elemen terakhir

    print("The decimal representation of", hexstr2, "is", newIntDec)

    print("\n")
    question = input("Do you want to repeat? (Yes/No) : ")
    # kondisi if, else untuk ngebreak loop while nya
    if question == "Yes" :
        RunAgain = True
    else :        #kalo jwbannya selain yes, ya gausah ngeloop lagi
        RunAgain = False  
    print("\n")

print("Thanks for using this program.\n")

print("Press Enter to continue . . . ")
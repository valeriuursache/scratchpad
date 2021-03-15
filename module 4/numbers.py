if __name__ == "__main__":

        age = 32
        print(age)
        print(type(age))
        str_age = "32"
        age = int(str_age)
        print(type(age))

        age_bin_str = "100000"
        age = int(age_bin_str, 2)
        print (age)
        print (type(age))

        age_hex_str = "20"
        age = int(age_hex_str, 16)
        print(age)
        print(type(age))

        one_billion = 10000000000
        print(one_billion)


        age = 32.3
        age = float("32.3")
        one_fillion = 1_000_000_000.0
        one_trillion = 3.14e12

        too_big = 2e400
        print(too_big)

        float_val = .1 + .1 + .1
        print(float_val)


        my_complex_num = 2 + 3j
        print(my_complex_num.real)
        print(my_complex_num.imag)
        print(my_complex_num.conjugate())
        print("script complete")

        


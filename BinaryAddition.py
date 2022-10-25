class BinaryAddition:



    @staticmethod
    def main(args):
        #converting binary to decimal,
        # then add to get total and again converting answer to binary
        a = 0B101 #5
        b =0B11 #3
        c =a+b #8
        print(a)
        print(c)
        print(Integer.toBinaryString(c)) #1000

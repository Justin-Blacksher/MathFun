# Main test function for trig.py library
# Written by: Justin Blacksher

import constants as con
import trig as t


def main():
    triangle = t.Trig(2.8, 4.0, 4.9)
    triangle.setCalc()

    print("Triangle Definitions")
    print("---------------------")
    print("[+] hyp = " + str(triangle.getHypotenuse()))
    print("[+] adj = " + str(triangle.getAdjacent()))
    print("[+] opp = " + str(triangle.getOpposite()))
    print("[+] Cos = " + str(triangle.getCos()))
    print("[+] Tan = " + str(triangle.getTan()))
    print("[+] Sin = " + str(triangle.getSin()))
    print("[+] Cot = " + str(triangle.getCotangent()))
    print("[+] Sec = " + str(triangle.getSecant()))
    print("[+] Csc = " + str(triangle.getCosecant()))





if __name__ == '__main__':
    print("")
    main()




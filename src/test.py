from bkr import *

def main():
    bkr_test_utility = bkr_utility()

    testPolyset = bkr_test_utility.generateTestPolySet()
    bkr_test_utility.printPolySet(testPolyset)
    
    if (bkr_test_utility.bkrIsConsistent(testPolyset)):
        print(f"Set is consistent")
    else:
        print(f"Set isn't consistent")

if __name__ == "__main__":
    main()
import os

def montecarlo():
    for thr in [1, 2, 4, 8, 12, 16, 20, 24, 32]:
        for n in [1, 10, 100, 1000, 10000, 100000, 500000, 1000000]:
            cmd = "g++ -std=c++11 -O3 ./src/montecarlo.cpp -o ./bin/montecarlo -lm -fopenmp"
            os.system( cmd )
            cmd = f"./montecarlo {thr} {n}"
            os.system( cmd )


def main():
    montecarlo()


if __name__ == '__main__':
    main()
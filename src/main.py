# ここがメインプログラム

from wrapper import *

def main():
    
    n: int = int(input())

    if is_prime(n):
        print(f'{n} is prime.')
    else:
        print(f'{n} is not prime.')

if __name__ == '__main__':
    main()

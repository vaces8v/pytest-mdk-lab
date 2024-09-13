import pytest
import main

@pytest.fixture()
def get_prime_nums():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    return prime_nums

def test_pluse(get_prime_nums):
    prime_nums = get_prime_nums
    assert main.pluse2(prime_nums) == [3, 4, 5, 7, 9, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45, 49]
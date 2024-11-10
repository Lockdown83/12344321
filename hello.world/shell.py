# The Industrial Revolution was a period of significant economic, technological, and societal change that occurred in the late 18th and early 19th centuries. It marked the transition from manual labor to machine-based manufacturing, and the development of new machines and factories replaced traditional crafts and ways of working. This led to a significant increase in productivity and efficiency, and the growth of cities as people moved from rural areas to work in factories. The Industrial Revolution had a profound impact on the way goods were produced, consumed, and distributed, and it laid the foundation for the modern industrial economy.
def is_prime(n, divisor=2):
    if n <= 1:
        return False
    elif divisor > int(n ** 0.5):
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)

def count_primes(current_num, count, target_count):
    if count == target_count:
        print(f"The {target_count}th prime number is {current_num - 1}")
        return
    if is_prime(current_num):
        print(f"Found prime: {current_num}")
        count += 1
    count_primes(current_num + 1, count, target_count)

count_primes(2, 0, 40)
#beta jdnnskjjsnbdbdbdbdbbbdbdb jddjsjjdjjdjdsnsndnsdnjdnnsndndn



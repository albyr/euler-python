def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n == 1: return [1]
    primes = prime_sieve(int(n**0.5) + 1)
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)
 
    return prime_factors

trial_division(13195)

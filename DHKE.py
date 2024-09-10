import random

def diffie_hellman(p, g):
    
    private_key_a = random.randint(2, p - 2)
   
    private_key_b = random.randint(2, p - 2)

    
    public_key_a = pow(g, private_key_a, p)  
    public_key_b = pow(g, private_key_b, p)  

    
    K_AB = pow(public_key_b, private_key_a, p)  
    K_BA = pow(public_key_a, private_key_b, p)  

  

    # Print values for understanding
    print(f"Prime (P): {p}")
    print(f"alpha (G): {g}")
    print(f"Alice's Private Key: {private_key_a}")
    print(f"Bob's Private Key: {private_key_b}")
    print(f"Alice's Public Key: {public_key_a}")
    print(f"Bob's Public Key: {public_key_b}")
    print(f"Shared Secret Key: {K_AB}")
    print(f"Shared Secret Key: {K_BA}")

    return K_AB


large_p = 23  
alpha = 5  


shared_secret = diffie_hellman(large_p, alpha)

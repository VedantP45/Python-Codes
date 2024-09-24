import random

def elgamal_encryption(p, g, message):
   
    private_key_a = random.randint(2, p - 2)  
    private_key_b = random.randint(2, p - 2)  
    
    public_key_a = pow(g, private_key_a, p)  
    public_key_b = pow(g, private_key_b, p)  

    k = random.randint(2, p - 2)  
    c1 = pow(g, k, p)  
    shared_secret_b = pow(public_key_a, k, p)  
    c2 = (message * shared_secret_b) % p 
    
   
    shared_secret_a = pow(c1, private_key_a, p)  
    shared_secret_a_inv = pow(shared_secret_a, p-2, p)  
    decrypted_message = (c2 * shared_secret_a_inv) % p  

    
    print(f"Prime (P): {p}")
    print(f"Generator (G): {g}")
    print(f"Alice's Private Key: {private_key_a}")
    print(f"Bob's Private Key (used in encryption): {private_key_b}")
    print(f"Alice's Public Key: {public_key_a}")
    print(f"Bob's Public Key (for encryption): {public_key_b}")
    print(f"Ciphertext (C1, C2): ({c1}, {c2})")
    print(f"Decrypted Message: {decrypted_message}")

    return (c1, c2), decrypted_message



large_p = 23  
alpha = 5     
message = 10 


ciphertext, decrypted_message = elgamal_encryption(large_p, alpha, message)

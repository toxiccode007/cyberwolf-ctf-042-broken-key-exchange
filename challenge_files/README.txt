CYBERWOLF LABS — CTF 042
The Broken Key Exchange

Goal
Analyze the Diffie-Hellman transcript, recover the private exponent used by the legacy service, derive the session secret, and decrypt protected_message.bin.

Files
- exchange_capture.txt : public DH parameters, a legitimate public value, and several captured responses to attacker-controlled peer public values.
- protected_message.bin : encrypted message. Format: ASCII header "CW042" + 16-byte nonce + ciphertext.

Important implementation detail
The legacy server computes shared = peer_public^a mod p but does NOT validate the order of peer_public. The supplied probe values were chosen from tiny subgroups.

Mathematical route
1. Read p and g from the capture.
2. For each probe, determine the order r of the supplied peer public value.
3. Because y^a = response and y has tiny order r, only a mod r is exposed.
4. Enumerate the tiny subgroup (2, 3, 5, 7, 11) to recover a residue for each probe.
5. Combine the residues with CRT. The product 2×3×5×7×11 is larger than the private exponent used in this challenge, so the exponent is recovered exactly.
6. Compute the legitimate DH shared secret as server_public^a mod p.
7. Derive the stream key as SHA-256(str(shared_secret)).
8. Decrypt the ciphertext with repeating SHA-256 blocks XORed with the ciphertext bytes. The plaintext contains the flag.

Suggested Python building blocks
pow(base, exponent, modulus)
math.gcd / sympy.ntheory.modular.crt (optional)
hashlib.sha256

Do not brute-force the full private exponent. The challenge is designed to demonstrate a small-subgroup validation failure.

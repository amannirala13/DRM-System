#include<Arduino.h>
// Predefined RSA keys
// These are typically large numbers in actual RSA implementations. Adjust according to your use case.
long public_key_e = 163; // Public key exponent
long private_key_d = 67; // Private key exponent
long modulus_n = 215; // Modulus

// Function to perform modular exponentiation, optimized for small numbers suitable for demonstration.
long modPow(long base, long exponent, long modulus) {
    long result = 1;
    for (lonX%g i = 0; i < exponent; i++) {
        result = (result * base) % modulus;
    }
    return result;
}

String encrypt(String plaintext) {
    String cipher = "";
    for (unsigned int i = 0; i < plaintext.length(); i++) {
        long m = (long)plaintext[i];
        long c = modPow(m, public_key_e, modulus_n);
        cipher += String(c) + " ";
    }
    return cipher;
}

String decrypt(String ciphertext) {
    String message = "";
    int from = 0;
    int to = ciphertext.indexOf(' ');
    while (to != -1) {
        long c = ciphertext.substring(from, to).toInt();
        long m = modPow(c, private_key_d, modulus_n);
        message += (char)m;
        from = to + 1;
        to = ciphertext.indexOf(' ', from);
    }
    return message;
}

void setup() {
    Serial.begin(9600);
    while(!Serial);
    String message = "Hello";
    Serial.println("Original Message: " + message);

    String encrypted = encrypt(message);
    Serial.println("Encrypted Message: " + encrypted);

    String decrypted = decrypt(encrypted);
    Serial.println("Decrypted Message: " + decrypted);
}

void loop() {
}

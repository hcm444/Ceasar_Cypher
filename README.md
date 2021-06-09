# ceasar_cypher
Simple cryptography methods

## encode

Encodes with Ceasar cypher.
```
message: invictus
shift: 3
option: encode
invictus
lqylfwxv
message: 
```

## decode

Decodes with Ceasar cypher.
```
message: lqylfwxv
shift: 3
option: decode
lqylfwxv
invictus
message: 
```

## OTP encode

Encodes with Ceasar cypher adds randomness by generating a secret key.
```
message: invictus
shift: 2
option: OTP encode
invictus
nvvljvwt
[5, 8, 0, 3, 7, 2, 2, 1]
message: 
```

## OTP decode

Decodes with Ceasar cypher in accordance with secret key generated.
```
message: nvvljvwt
shift: 2
option: OTP decode
nvvljvwt
Secret Key: 5
Secret Key: 8
Secret Key: 0
Secret Key: 3
Secret Key: 7
Secret Key: 2
Secret Key: 2
Secret Key: 1
invictus
message: 
```

## hack

Bruteforce attack.
```
message: invictus
shift: 10
option: hack
Guess #0: invictus
Guess #1: hmuhbstr
Guess #2: gltgarsq
Guess #3: fksfzqrp
Guess #4: ejreypqo
Guess #5: diqdxopn
Guess #6: chpcwnom
Guess #7: bgobvmnl
Guess #8: afnaulmk
Guess #9: zemztklj
Guess #10: ydlysjki
Guess #11: xckxrijh
Guess #12: wbjwqhig
Guess #13: vaivpghf
Guess #14: uzhuofge
Guess #15: tygtnefd
Guess #16: sxfsmdec
Guess #17: rwerlcdb
Guess #18: qvdqkbca
Guess #19: pucpjabz
Guess #20: otboizay
Guess #21: nsanhyzx
Guess #22: mrzmgxyw
Guess #23: lqylfwxv
Guess #24: kpxkevwu
Guess #25: jowjduvt
message: 
```

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
message: lqylfwxv
shift: 3
option: hack
Guess #0: lqylfwxv
Guess #1: kpxkevwu
Guess #2: jowjduvt
Guess #3: **invictus**
Guess #4: hmuhbstr
Guess #5: gltgarsq
Guess #6: fksfzqrp
Guess #7: ejreypqo
Guess #8: diqdxopn
Guess #9: chpcwnom
Guess #10: bgobvmnl
Guess #11: afnaulmk
Guess #12: zemztklj
Guess #13: ydlysjki
Guess #14: xckxrijh
Guess #15: wbjwqhig
Guess #16: vaivpghf
Guess #17: uzhuofge
Guess #18: tygtnefd
Guess #19: sxfsmdec
Guess #20: rwerlcdb
Guess #21: qvdqkbca
Guess #22: pucpjabz
Guess #23: otboizay
Guess #24: nsanhyzx
Guess #25: mrzmgxyw
message: 
```

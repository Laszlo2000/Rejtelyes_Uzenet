# Caesar Cipher Decoder

This Python script decodes a Caesar cipher text with a custom character shift. The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Project Description

The provided script contains a function, `decode()`, which decodes a message encoded using a Caesar cipher with a shift of 2. Specifically, each uppercase and lowercase letter in the encoded message has been shifted forward by two positions in the alphabet. Spaces, newline characters, and punctuation marks are left unchanged.

### Encoding Logic
The encoding logic in this project assumes:
- Uppercase letters `A-Z` are shifted such that `A` maps to `C`, `B` maps to `D`, ..., and `Y` maps to `A`, `Z` maps to `B`.
- Lowercase letters `a-z` follow a similar pattern, with `a` mapping to `c` and `z` mapping to `b`.
  
Other characters (spaces, newlines, `!`, `:`) are preserved in their original positions.

### Example
The encoded message:
```plaintext
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb

The encoded message
Aban BweI!

Because iba zaw write holyeabout:
should ibe w Mount inlitermouse joufe!

Whywhywho:

Yolp

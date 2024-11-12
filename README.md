# decode.py

## Description
This Python script contains a function, `decode()`, that decrypts a given encoded message. The encryption appears to be a simple Caesar cipher shift, where uppercase and lowercase letters are shifted by two positions forward.

The script processes both uppercase and lowercase letters while preserving spaces, new lines, and certain punctuation (`'!'` and `':'`). It’s specifically designed to decode a message encoded with the same pattern of shifting characters.

## Usage

### `decode(message: str) -> str`
- **Parameters**: `message` (str) – A string containing the encoded message.
- **Returns**: A string containing the decoded message.

### Example
The following example demonstrates how to use the `decode` function.

```python
if __name__ == '__main__':
    message = '''
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
    '''
    print(decode(message))

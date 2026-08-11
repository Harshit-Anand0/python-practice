# Python-practice

## Email Validator (Without Regex)

Validates an email address using manual string checks, without regex or external libraries.

### Checks performed
- Allowed characters, single `@`, no spaces or consecutive dots
- Local part (before `@`) doesn't start/end with `.`
- Domain labels don't start/end with `-`, max 64 characters
- Top-level domain is alphabetic and at least 2 characters

### Run
```bash
python email-validator-without-regex.py
```

### Example
```
Enter your Email address: test@example.com
Your Email address is Valid.
```

### Note
Built as a practice project for string parsing and validation logic. Not RFC 5322-complete.



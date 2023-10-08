# 0x06. Regular expression

### Background Context

In this repo, regular expressions are build using Oniguruma, a regular expression  library that which is used by Ruby by default. 

### Tasks


**0. Simply matching School***

**Requirement:**

 - The regular expression must match School


**1. Repetition Token #0**

**Requirement:**

 - Find the regular expression that will match the following:
  - hbttn
  - hbtttn
  - hbttttn
  - hbtttttn


**2. Repetition Token #1**

**Requirement:**

  - Find the regular expression that will match the following:
   - htn
   - hbtn


**3. Repetition Token #2**

**Requirement:**

   - Find the regular expression that will match the following:
    - hbtn
    - hbttn
    - hbtttn
    - hbttttn


**4. Repetition Token #3**

**Requirement:**

  - Find the regular expression that will match the following:
    - hbn
    - hbtn
    - hbttn
    - hbtttn
    - hbttttn
 

**5. Not quite HBTN yet**

**Requirement:**
  - The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between


**6. Call me maybe**

This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

**Requirement:**

    - The regular expression must match a 10 digit phone number



**7. OMG WHY ARE YOU SHOUTING?**

**Requirement:**

    - The regular expression must be only matching: capital letters

**8. Textme**

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

**Requirements:**

    - Your script should output: [SENDER],[RECEIVER],[FLAGS]
        The sender phone number or name (including country code if present)
        The receiver phone number or name (including country code if present)
        The flags that were used


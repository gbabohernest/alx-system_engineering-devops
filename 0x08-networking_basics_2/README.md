# 0x08. Networking basics #1

### Tasks

**0. Change your home IP**

*Write a Bash script that configures an Ubuntu server with the below requirements.*

 - Requirements:

    - localhost resolves to 127.0.0.2
    - facebook.com resolves to 8.8.8.8.
    - The checker is running on Docker, so make sure to read this


**1. Show attached IPs**

*Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.*

- Example:

*sylvain@ubuntu$ ./1-show_attached_IPs | cat -e*
```10.0.2.15$```
```127.0.0.1$``
```sylvain@ubuntu$```

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our localhost IP :)


**2. Port listening on localhost**

*Write a Bash script that listens on port 98 on localhost.*

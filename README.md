# Unbound Watchdog

I created this script as a workaround for an issue, which was causing that Unbound was not resolving any requests after reboot of my Raspberry Pi. 

This script will check if the system has been restarted lately (uptime < 5 minutes) and if connection to few specified URLs is working correctly. If connection is not possible, Unbound service is restarted.

### Usage
Just place unbound_watchdog.py script in desired directory (etc. */home/pi/unbound_watchdog* in my case) and setup cronjob for startup of script. If you choose different directory, don't forget to change also paths in script.

```
* * * * * /usr/bin/python /home/pi/unbound_watchdog/unbound_check.py
```

###### Legend
**Unbound** is a validating, recursive, and caching DNS resolver product from NLnet Labs. It is distributed free of charge in open source form under the BSD license. -[Wikipedia](https://en.wikipedia.org/wiki/Unbound_(DNS_server))

# Unbound Watchdog

I created this script as a workaround for an issue, which was causing that Unbound was not resolving any requests after reboot of my Raspberry Pi. 

This script will check if the system has been restarted lately (uptime < 5 minutes) and if connection to few specified URLs is working correctly. If connection is not possible, Unbound service is restarted.
import subprocess
import os
import datetime
date = datetime.datetime.now()
uptime = os.popen('uptime').read()
timestamp = date.strftime("%d%m%Y_%H:%M:%S")
touch = 'touch /home/pi/unbound_watchdog/touch'
os.system(touch)



uptime_check = subprocess.Popen(['cat','/proc/uptime'],
                stdout = subprocess.PIPE,
                stderr = subprocess.STDOUT)
stdout,stderr = uptime_check.communicate()

uptime_check = stdout.split('.')

if int(uptime_check[0]) < 300:
                f = open("/home/pi/unbound_watchdog/unbound_check_%s.log" %timestamp, "a")
                print >> f, date
                print >> f, ""
                print >> f, uptime
                uptime_check = 1
else:
        exit()


success_counter = 0
urls = ['http://www.google.com','http://www.fast.com','http://www.apple.com']

for url in urls:
        print >> f, 'Test URL: %s' % url
        url_check = subprocess.Popen(['curl','-Is',url],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.STDOUT)
        stdout,stderr = url_check.communicate()

        url_check_out = stdout.split()
        if len(url_check_out) != 0:
                if url_check_out[1] == '200' or url_check_out[1] == '301':
                        print >> f, 'Connection success for %s' % url
                        success_counter += 1
        else:
                print >> f, 'Connection fail for %s' % url

if success_counter < 2:
        url_check = 1
else:
        exit()

if uptime_check == 1 and url_check == 1:


        restart_unbound = 'sudo service unbound restart'
        os.system(restart_unbound)
        print >> f, 'Unbound has been restarted'

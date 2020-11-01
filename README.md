# duet-off

Simple script to disable duet 3d printer by using tasmotized switch.
Power is disable when target temperature is set to -1 and real temeperature is below 45 deg.

Run from cron every 5 minutes.

All configuration is in python script.


To run on raspberry pi be sure to install local mDNS client:
```
sudo apt-get install libnss-mdns
```

It require python 3 with extenal dependency requests installed.

So on raspberry pi:
```
sudo apt install python3 python3-pip
pip3 install requests
```


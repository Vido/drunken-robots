#! /bin/bash

# Ex: Sat Jul 13 22:02:51 BRT 2013
datetime=$(date)

# replaces all ' ' for '_'
# Ex: Sat_Jul_13_22:02:51_BRT_2013
newfile1=${datetime// /_}

# replaces all ':' for '-'
# Ex: Sat_Jul_13_22-02-51_BRT_2013
newfile2=${newfile1//:/-}

ext=.crontab

crontab -l > backup/$newfile2$ext
crontab drunken-robots.crontab
echo "[ok] -> drunken-robots on crontab"

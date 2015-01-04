#! /bin/bash

### BEGIN INIT INFO
# Provides:          safe_set_cron
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Puts drunken-robots crontab up
# Description:       The script saves the current crontab and updates to the drunken-robots defined crontab.
### END INIT INFO

# More info: http://www.debian-administration.org/articles/28
# More info: http://wiki.debian.org/LSBInitScripts

case "$1" in

    start)
        echo "Starting script $0"
        # Change to scrip's directory
        cd $(dirname "${BASH_SOURCE[0]}")
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
        echo "[ ok ] drunken-robots on crontab... done."
        ;;

    stop)
        echo "Stopping script $0..."
        echo " done."
        ;;

    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;

    esac

exit 0

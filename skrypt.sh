#!/bin/bash

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"

        [[ "$devname" == "bus/"* ]] && continue
        [[ "$devname" == "input/"* ]] && continue
        [[ "$devname" == "video0"* ]] && continue

        eval "$(udevadm info -q property --export -p $syspath)"
        [[ -z "$ID_SERIAL" ]] && continue

        busnum="$(udevadm info -a -p  $(udevadm info -q path -n /dev/$devname) | awk -F "==" '/busnum/ {gsub("\"","");print $2}' | head -1)"
        devnum="$(udevadm info -a -p  $(udevadm info -q path -n /dev/$devname) | awk -F "==" '/devnum/ {gsub("\"","");print $2}' | head -1)"
        bus_dev=${busnum}:${devnum}
        lsusb="$(lsusb -s $bus_dev)"

        echo "$lsusb - /dev/$devname"
    )
done

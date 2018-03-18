#/usr/bin/env zsh


#get average cpu utilisation in percent
#args -t prints text not just number.

#get average inverted(you need 100-x) cpu utilisation
a=$(mpstat 1 1 | grep Average: | awk '{print $12}')
#replace , with .
a=${a//,/.}
b=$((100-a))
#rounding to 2 decimal places
c=$(echo $b | xargs printf "%.*f\n" 2)
#output
if [ "$1" = "-t" ];
then
    echo cpu usage: $c%
else
    echo $c
fi

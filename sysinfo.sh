#/usr/bin/env bash
echo $(lsb_release -i | cut -f2) $(lsb_release -r | cut -f2) $(lsb_release -c | cut -f2) $(uname -r) $(uname -m)
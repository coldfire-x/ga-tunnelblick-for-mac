#!/bin/bash

# compute google authenticator otp
PASSWD=$(oathtool -b -s 30s --totp $3)
PASSWD="$2$PASSWD"

# update keychain
/usr/bin/security add-generic-password -U -s Tunnelblick-Auth-$1 -a password -w $PASSWD

osascript ./connect_tunnelblink.scpt

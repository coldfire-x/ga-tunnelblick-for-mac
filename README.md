## requirements

- install tunnelblick
- install oauth with `brew install oathtool`


## how to use

add your authenticate information in `run.py`, there are three vars should be
set before use:

	* FIXED_PASSWD = ''  # fixed password if given
	* TUNNELBLINK_VPN_NAME = ''  # your vpn's name
	* GA_SECRET = ''  # google otp authenticator secret

now, the magic show begin, execute the `run.py`:

	python run.py

*FOR THE FIRST TIME RUN THIS SCRIPT* Tunnelblick will popup a window for input username and password,
input your vpn's username, for password you can input whatever you want, then
*MAKE SUER SAVE IN KEYCHAIN* checkbox checked. Close the windown, run this script again,
you sure good to go now(popup window gone).

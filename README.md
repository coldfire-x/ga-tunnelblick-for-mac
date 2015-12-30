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

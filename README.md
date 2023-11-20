cmk-mailperf
============

Install the python script `mailcounter` on monitored system under `/usr/local/bin`.
The script `mailcounter` requires some python modules. You can install these modules
on Debian box from the system repository using a command:

    apt install python3-docopt python3-daemon python3-dateutil python3-systemd

You should try to run the script for a while in non-daemon mode (interrupt it by Ctrl-C):

    mailcounter -D -v -v

Install the unit file `mailcounter.service` under `/etc/systemd/system/` directory
of target monitored system and reload `systemd`

    systemctl daemon-reload

Start the service mailcounter:

    systemctl start mailcounter

The service should repeatedly write the status file:

    # cat /run/mailcounter.txt
    bounced 0
    deferred 0
    forwarded 0
    greylisted 0
    received 3
    rejected 12
    sent 3
    spam 0
    time_since 2023-11-23T17:52:19.654580+01:00
    virus 0

Finally install an agent plugin on monitored host:

    /usr/lib/check_mk_agent/plugins/mailperf

On your CheckMK monitoring system install the mkp package and reinventorize monitored system.
Alternatively you can also set some levels for mail rates.

The `mailcounter` is inspired by the `mailgraph` utility and the `pflogsum` utility.

--
Václav Ovsík <vaclav.ovsik@gmail.com>  Sun, 26 Nov 2023 22:10:25 +0100  

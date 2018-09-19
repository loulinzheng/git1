#!/bin/sh
#Create Nagios nsca service check file for VMware ESX
cd /opt/nsca
#Verify schedule parameter
if [ "$1" = "" ] ; then
   echo Script requires a schedule name
   exit 1 ; fi
#Check to see if this schedule is already running
if [ "`/sbin/fuser -f *$1.dat 2>&1`" != "" ] ; then
#  Omit message to protect log of pre-existing shell
   exit 2 ; fi
#Run specified schedule
./nsca_vmware.pl $1
if [ $? -gt 0 ] ; then
   echo Perl script error, no packets sent
   exit 3 ; fi
#Send results to Nagios
/usr/bin/send_nsca -H srv-infotech.symyx.com -c ./send_nsca.cfg < nsca_vmware_$1.dat

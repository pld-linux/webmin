%include        /usr/lib/rpm/macros.perl
Summary:	Webmin - web-based administration
Summary(pl):	Webmin - administracja przez WWW
Name:		webmin
Version:	0.980
# Current unofficial tarball version (be carefull; numberring incompatibility):
#Version:	0.985
%define	source_version	%{version}
Release:	0.1
License:	distributable (BSD-like)
Group:		Applications/System
Source0:	http://www.webmin.com/webmin/download/%{name}-%{version}.tar.gz
# Unofficial webmin tarballs location (if anybody interested):
#Source0:	http://www.webmin.com/webmin/devel/tarballs/%{name}-%{source_version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}-miniserv.conf
Source3:	%{name}-find-lang.sh
#Patch0:		%{name}-%{version}-PLD.patch
URL:		http://www.webmin.com/webmin/
BuildRequires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/chkconfig

%description
Webmin is a web-based interface for system administration for Unix.
Using any browser that supports tables and forms, you can setup user
accounts, Apache, internet services, DNS, file sharing and so on.

%description -l pl
Webmin jest narzêdziem do administrowania Uniksem poprzez WWW.
Umo¿liwia m.in. konfigurowanie kont u¿ytkowników, Apache'a, us³ug
internetowych, DNS-u, udostêpniania zasobów za pomoc± dowolnej
przegl±darki obs³uguj±cej tabele i formularze

%package disk-tools
Summary:	Webmin - Partition and disk management tools
Summary(pl):	Webmin - Narzêdzia do zarz±dzania dyskami i partycjami
Group:		Applications/System
Requires:	hdparm
Requires:	fdisk
Requires:	webmin-system = %{version}
Prereq:		webmin

%description disk-tools
Webmin - Partition and disk management tools.

%description disk-tools -l pl
Webmin - Narzêdzia do zarz±dzania dyskami i partycjami.

# APACHE
%package apache
Summary:	Webmin - Apache webserver
Summary(pl):	Webmin - Serwer WWW Apache
Group:		Applications/System
Requires:	apache
Prereq:		webmin

%description apache
Webmin - Apache webserver.

%description apache -l pl
Webmin - Serwer WWW Apache.

# AT
%package at
Summary:	Webmin - At
Summary(pl):	Webmin - At
Group:		Applications/System
Requires:	at
Prereq:		webmin

%description at
Webmin - At.

%description at -l pl
Webmin - At.

# BIND 8/9
%package bind8
Summary:	Webmin - BIND DNS server
Summary(pl):	Webmin - Serwer DNS BIND
Group:		Applications/System
Requires:	bind
Prereq:		webmin

%description bind8
Webmin - BIND DNS server.

%description bind8 -l pl
Webmin - Serwer DNS BIND.

# BURNER
%package burner
Summary:	Webmin - CD Burner
Summary(pl):	Webmin - Wypalanie p³yt CD
Group:		Applications/System
Requires:	cdrecord
Requires:	mkisofs
Requires:	mpg123
Prereq:		webmin

%description burner
Webmin - CD Burner.

%description burner -l pl
Webmin - Wypalanie p³yt CD.

%if 0
# CFEGINE
%package cfengine
Summary:	Webmin - Configuration Engine
Summary(pl):	Webmin - cfengine
Group:		Applications/System
# ?????
Requires:	cfengine
Prereq:		webmin

%description cfengine
Webmin - Configuration Engine.

%description cfengine -l pl
Webmin - cfengine.
%endif

# CLUSTER-SOFTWARE
%package cluster-software
Summary:	Webmin - Cluster software packages
Summary(pl):	Webmin - Pakiety oprogramowania w klastrze
Group:		Applications/System
Prereq:		webmin

%description cluster-software
Webmin - Cluster software packages.

%description cluster-software -l pl
Webmin - Pakiety oprogramowania w klastrze.

# CLUSTER-USERADMIN
%package cluster-useradmin
Summary:	Webmin - Cluster users and groups
Summary(pl):	Webmin - U¿ytkownicy i grupy klastra
Group:		Applications/System
Prereq:		webmin

%description cluster-useradmin
Webmin - Cluster users and groups.

%description cluster-useradmin -l pl
Webmin - U¿ytkownicy i grupy klastra.

# CRON
%package cron
Summary:	Webmin - Cron
Summary(pl):	Webmin - Cron
Group:		Applications/System
Requires:	crondaemon
Prereq:		webmin

%description cron
Webmin - Cron.

%description cron -l pl
Webmin - Cron.

# DHCPD
%package dhcpd
Summary:	Webmin - DHCP server
Summary(pl):	Webmin - Serwer DHCP
Group:		Applications/System
Requires:	dhcp
Prereq:		webmin

%description dhcpd
Webmin - DHCP server.

%description dhcpd -l pl
Webmin - Serwer DHCP.

# FETCHMAIL
%package fetchmail
Summary:	Webmin - Fetchmail
Summary(pl):	Webmin - Fetchmail
Group:		Applications/System
Requires:	fetchmail

%description fetchmail
Webmin - Fetchmail.

%description fetchmail -l pl
Webmin - Fetchmail.

# DUMP
%package fsdump
Summary:	Webmin - Filesystem backup
Summary(pl):	Webmin - Archiwizacja systemu plików
Group:		Applications/System
Requires:	dump
Prereq:		rc-scripts
Prereq:		webmin

%description fsdump
Webmin - Filesystem backup.

%description fsdump -l pl
Webmin - Archiwizacja systemu plików.

# GRUB
%package grub
Summary:	Webmin - GRUB configuration
Summary(pl):	Webmin - Konfiguracja GRUB-a
Group:		Applications/System
Requires:	grub
Prereq:		webmin

%description grub
Webmin - GRUB configuration.

%description grub -l pl
Webmin - Konfiguracja GRUB-a.

# HEARTBEAT
%package heartbeat
Summary:	Webmin - Heartbeat Monitor
Summary(pl):	Webmin - Monitor Heartbeat
Group:		Applications/System
Requires:	heartbeat

%description heartbeat
Webmin - Heartbeat Monitor.

%description heartbeat -l pl
Webmin - Monitor Heartbeat.

# INETD
%package inetd
Summary:	Webmin - Inetd
Summary(pl):	Webmin - Inetd
Group:		Applications/System
Prereq:		webmin

%description inetd
Webmin - Inetd.

%description inetd -l pl
Webmin - Inetd.

# JABBER
%package jabber
Summary:	Jabber IM server
Summary(pl):	Serwer systemu powiadamiania Jabber
Group:		Applications/System
Requires:	jabber
Prereq:		webmin

%description jabber
Webmin - Jabber IM server.

%description jabber -l pl
Webmin - Serwer systemu powiadamiania Jabber.

# LILO
%package lilo
Summary:	Webmin - LILO configuration
Summary(pl):	Webmin - Konfiguracja LILO
Group:		Applications/System
Requires:	lilo
Prereq:		webmin

%description lilo
Webmin - LILO configuration.

%description lilo -l pl
Webmin - Konfiguracja LILO.

# LVM
%package lvm
Summary:	Webmin - Logical Volume Management
Summary(pl):	Webmin - Zarz±dzanie wolumenami logicznymi (LVM)
Group:		Applications/System
Requires:	lvm
Prereq:		webmin

%description lvm
Webmin - Logical Volume Management.

%description lvm -l pl
Webmin - Zarz±dzanie wolumenami logicznymi (LVM).

%if 0
# MAJORDOMO
%package majordomo
Summary:	Webmin - Majordomo List Manager
Summary(pl):	Webmin - Zarz±dca list dyskusyjnych Majordomo
Group:		Applications/System
Requires:	majordomo
Requires:	webmin-sendmail = %{version}
Prereq:		webmin

%description majordomo
Webmin - Majordomo List Manager.

%description majordomo -l pl
Webmin - Zarz±dca list dyskusyjnych Majordomo.
%endif

# MON
%package mon
Summary:	Webmin - MON resource monitoring system
Summary(pl):	Webmin - System monitorowania zasobów MON
Group:		Applications/System
Requires:	mon
Prereq:		rc-scripts
Prereq:		webmin

%description mon
Webmin - MON resource monitoring system.

%description mon -l pl
Webmin - System monitorowania zasobów MON.

# MYSQL
%package mysql
Summary:	Webmin - MySQL server
Summary(pl):	Webmin - Serwer MySQL
Group:		Applications/System
Requires:	mysql-client
Prereq:		webmin

%description mysql
Webmin - MySQL server.

%description mysql -l pl
Webmin - Serwer MySQL.

# NET
%package net
Summary:	Webmin - Network configuration
Summary(pl):	Webmin - Konfiguracja sieci
Group:		Applications/System
Prereq:		rc-scripts
Prereq:		webmin

%description net
Webmin - Network configuration.

%description net -l pl
Webmin - Konfiguracja sieci.

# POSTFIX
%package postfix
Summary:	Webmin - Postfix
Summary(pl):	Webmin - Postfix
Group:		Applications/System
Requires:	postfix

%description postfix
Webmin - Postfix.

%description postfix -l pl
Webmin - Postfix.

# POSTGRESQL
%package postgresql
Summary:	Webmin - PostgreSQL server
Summary(pl):	Webmin - Serwer PostgreSQL
Group:		Applications/System
Requires:	postgresql-clients
Prereq:		webmin

%description postgresql
Webmin - PostgreSQL server.

%description postgresql -l pl
Webmin - Serwer PostgreSQL.

# PPP
%package ppp
Summary:	Webmin - PAP (PPP) usernames and passwords
Summary(pl):	Webmin - Nazwy u¿ytkowników i has³a dla PAP (PPP)
Group:		Applications/System
Requires:	ppp
Prereq:		webmin

%description ppp
Webmin - PAP (PPP) usernames and passwords.

%description ppp -l pl
Webmin - Nazwy u¿ytkowników i has³a dla PAP (PPP).

%if 0
# PRINTER
%package printer
Summary:	Webmin - Printer administration
Summary(pl):	Webmin - Zarz±dzanie drukarkami
Group:		Applications/System
Requires:	lpd
Prereq:		webmin

%description printer
Webmin - Printer administration.

%description printer -l pl
Webmin - Zarz±dzanie drukarkami.
%endif

# PROFTPD
%package proftpd
Summary:	Webmin - Proftpd FTP Server
Summary(pl):	Webmin - Serwer FTP Proftpd
Group:		Applications/System
Requires:	proftpd

%description proftpd
Webmin - Proftpd FTP Server.

%description proftpd -l pl
Webmin - Serwer FTP Proftpd.

# CVS-PSERVER
%package cvs-pserver
Summary:	Webmin - CVS pserver
Summary(pl):	Webmin - Serwer CVS (pserver)
Group:		Applications/System
Requires:	cvs-pserver

%description cvs-pserver
Webmin - CVS pserver configuration.

%description cvs-pserver -l pl
Webmin - Konfiguracja serwera CVS dzia³aj±cego w trybie pserver.

# SAMBA
%package samba
Summary:	Webmin - Samba configuration
Summary(pl):	Webmin - Konfiguracja samby
Group:		Applications/System
Requires:	samba
Prereq:		webmin

%description samba
Webmin - Samba.

%description samba -l pl
Webmin - Samba.

# SENTRY
%package sentry
Summary:	Webmin - Sentries
Summary(pl):	Webmin - Wykrywanie prób nieautoryzowanego dostêpu
Group:		Applications/System
#Requires:	portsentry
#Requires:	hostsentry
Prereq:		webmin

%description sentry
Webmin - Sentries.

%description sentry -l pl
Webmin - Wykrywanie prób nieautoryzowanego dostêpu lub skanowania systemu.

# QMAIL
%package qmail
Summary:	Webmin - Qmail configuration
Summary(pl):	Webmin - Konfiguracja qmaila
Group:		Applications/System
Requires:	qmail
Prereq:		webmin

%description qmail
Webmin - Qmail configuration.

%description qmail -l pl
Webmin - Konfiguracja qmaila.

# SENDMAIL
%package sendmail
Summary:	Webmin - Sendmail configuration
Summary(pl):	Webmin - Konfiguracja sendmaila
Group:		Applications/System
Requires:	sendmail
Prereq:		webmin

%description sendmail
Webmin - Sendmail configuration.

%description sendmail -l pl
Webmin - Konfiguracja sendmaila.

# SQUID
%package squid
Summary:	Webmin - Squid proxy
Summary(pl):	Webmin - Serwer proxy Squid
Group:		Applications/System
Requires:	squid
Prereq:		webmin

%description squid
Webmin - Squid proxy.

%description squid -l pl
Webmin - Serwer proxy Squid.

# SSHD
%package sshd
Summary:	Webmin - SSH Server
Summary(pl):	Webmin - Serwer SSH
Group:		Applications/System
Requires:	openssh-server openssh-clients

%description sshd
Webmin - SSH Server.

%description sshd -l pl
Webmin - Serwer SSH.

# WUFTPD
%package wuftpd
Summary:	Webmin - Wu-Ftpd server
Summary(pl):	Webmin - Serwer Wu-Ftpd
Group:		Applications/System
Requires:	wu-ftpd
Prereq:		webmin

%description wuftpd
Webmin - Wu-Ftpd server.

%description wuftpd -l pl
Webmin - Serwer Wu-Ftpd.

# XINETD
%package xinetd
Summary:	Webmin - Xinetd
Summary(pl):	Webmin - Xinetd
Group:		Applications/System

%description xinetd
Webmin - Xinetd.

%description xinetd -l pl
Webmin - Xinetd.

# NFS EXPORTS
%package nfs
Summary:	Webmin - NFS server configuration
Summary(pl):	Webmin - Konfiguracja serwera NFS
Group:		Applications/System
Requires:	nfsdaemon
Prereq:		webmin

%description nfs
Webmin - NFS server configuration.

%description nfs -l pl
Webmin - Konfiguracja serwera NFS.

# QUOTA
%package quota
Summary:	Webmin - Quota management
Summary(pl):	Webmin - Zarz±dzanie quota
Group:		Applications/System
Requires:	quota
Prereq:		webmin

%description quota
Webmin - Quota management.

%description quota -l pl
Webmin - Zarz±dzanie quota.

# SOFTWARE
%package software
Summary:	Webmin - Software Packages
Group:		Applications/System
Requires:	rpm
Prereq:		webmin

%description software
Webmin - Software Packages.

# STATUS
%package monitor
Summary:	Webmin - Event monitor
Summary(pl):	Webmin - Monitor zdarzeñ
Group:		Applications/System
Requires:	crondaemon
Prereq:		webmin

%description monitor
Webmin - Event monitor.

%description monitor -l pl
Webmin - Monitor zdarzeñ.

# SYSLOG
%package syslog
Summary:	Webmin - System logger
Summary(pl):	Webmin - Logi systemowe
Group:		Applications/System
Requires:	syslogdaemon
Prereq:		webmin

%description syslog
Webmin - System logger.

%description syslog -l pl
Webmin - Logi systemowe.

%package admin-tools
Summary:	Webmin - Admin-tools (telnet, file manager, etc)
Summary(pl):	Webmin - Narzêdzia administracyjne (telnet, zarz±dzanie plikami, itp.)
Group:		Applications/System
Prereq:		webmin

%description admin-tools
Webmin - Admin-tools (telnet, file manager, etc).

%description admin-tools -l pl
Webmin - Narzêdzia administracyjne (telnet, zarz±dzanie plikami, itp.).

# PROC, INIT, INITTAB, MOUNT
%package system
Summary:	Webmin - System Configuration
Summary(pl):	Webmin - Konfiguracja systemu
#Summary:	Webmin - Process Manager
#Summary(pl):	Webmin - Zarz±dzenia procesami
Group:		Applications/System
Prereq:		webmin

%description system
Webmin - System Configuration.

%description system -l pl
Webmin - Konfiguracja systemu.

# NIS
%package nis
Summary:	Webmin - NIS configuration
Summary(pl):	Webmin - Konfiguracja NIS
Group:		Applications/System
Requires:	webmin-useradmin = %{version}
Requires:	webmin-inetd = %{version}
Prereq:		webmin

%description nis
Webmin - NIS configuration.

%description nis -l pl
Webmin - Konfiguracja NIS.

# PASSWD
%package passwd
Summary:	Webmin - Change Passwords
Summary(pl):	Webmin - Zmiany hase³
Group:		Applications/System
Requires:	webmin-useradmin = %{version}
Prereq:		webmin

%description passwd
Webmin - Change Passwords.

%description passwd -l pl
Webmin - Zmiany hase³.

# USERADMIN
%package useradmin
Summary:	Webmin - User account manager
Summary(pl):	Webmin - Obs³uga kont u¿ytkowników
Group:		Applications/System
Prereq:		webmin

%description useradmin
Webmin - User account manager.

%description useradmin -l pl
Webmin - Obs³uga kont u¿ytkowników.

# no usermin in PLD yet
%if 0
# USERMIN
%package usermin
Summary:	Webmin - Usermin configuration
Summary(pl):	Webmin - Konfiguracja Usermina
Group:		Applications/System
Requires:	usermin
Prereq:		webmin

%description usermin
Webmin - Usermin configuration.

%description usermin -l pl
Webmin - Konfiguracja usermina.
%endif

# THEMES
%package themes
Summary:	Webmin - Extra Themes for Webmin
Summary(pl):	Webmin - Dodatkowe motywy Webmina
Group:		Applications/System

%description themes
Webmin - Extra Themes for Webmin.

%description themes -l pl
Webmin - Dodatkowe motywy Webmina.

%prep
%setup -q -n %{name}-%{source_version}
#%patch0 -p1
%build

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/webmin,/var/{log,run}/webmin} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webmin,rc.d/init.d}

cp -rp * $RPM_BUILD_ROOT%{_datadir}/webmin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/webmin
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.conf
install %{SOURCE3} .
install $RPM_BUILD_ROOT%{_datadir}/webmin/miniserv.pem \
	$RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.pem

(find $RPM_BUILD_ROOT%{_datadir}/webmin -name '*.cgi' -print ; find $RPM_BUILD_ROOT%{_datadir}/webmin -name '*.pl' -print) | perl $RPM_BUILD_ROOT%{_datadir}/webmin/perlpath.pl %{_bindir}/perl -

export allmods=`cd $RPM_BUILD_ROOT%{_datadir}/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`

perl $RPM_BUILD_ROOT%{_datadir}/webmin/copyconfig.pl pld-linux 1.0 $RPM_BUILD_ROOT%{_datadir}/webmin $RPM_BUILD_ROOT%{_sysconfdir}/webmin "" $allmods

echo "%{_bindir}/perl"		>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/perl-path
echo "/var/log/webmin" 		>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/var-path
echo "real_os_version=1.0"	>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "lang=en" 			>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "find_pid_command=ps auwwwx | grep NAME | grep -v grep | awk '{ print $2 }'"	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "os_type=pld-linux" 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "path=/bin:%{_bindir}:/sbin:%{_sbindir}:%{_prefix}/local/bin" >>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo real_os_type=PLD Linux 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo os_version=1.0 		>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config

echo %{version}			>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/version

gzip -9nf LICENCE LICENCE.ja

for a in acl apache at bind8 burner cfengine cluster-software \
    cluster-useradmin custom dhcpd exports fdisk fetchmail file fsdump \
    grub heartbeat inittab jabber lilo lpadmin lvm majordomo man mon \
    mysql net nis pam pap passwd postfix postgresql proc proftpd pserver \
    qmailadmin quota raid samba sendmail sentry servers shell software \
    squid sshd status syslog telnet time useradmin usermin webmin \
    webminlog wuftpd xinetd ; do
	./webmin-find-lang.sh $RPM_BUILD_ROOT %{_datadir}/webmin/$a $a
done
for a in cron inetd init mount stunnel ; do
	./webmin-find-lang.sh $RPM_BUILD_ROOT %{_datadir}/webmin/$a $a --no-help
done
./webmin-find-lang.sh $RPM_BUILD_ROOT %{_datadir}/webmin MAIN

cat custom.lang file.lang telnet.lang webminlog.lang > admin-tools.lang
cat fdisk.lang raid.lang > disk-tools.lang
cat init.lang inittab.lang mount.lang proc.lang > system.lang
cat MAIN.lang acl.lang man.lang pam.lang servers.lang shell.lang \
	time.lang webmin.lang > base.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q ^host= /etc/webmin/miniserv.conf; then
	echo "host=`hostname`" >>/etc/webmin/miniserv.conf
fi

if [ -f /var/lock/subsys/webmin ]; then
	/etc/rc.d/init.d/webmin restart >&2
else
        echo "Run \"/etc/rc.d/init.d/webmin start\" to start webmin" >&2
	echo "and use your web browser to go to:" >&2
	echo "http://your_host_name:10000" >&2
fi

export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%preun
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/webmin ]; then
                /etc/rc.d/init.d/webmin stop
        fi
        /sbin/chkconfig	--del webmin
fi

%post disk-tools
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post apache
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post at
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post burner
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post bind8
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%if 0
%post cfengine
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods
%endif

%post cluster-software
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post cluster-useradmin
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post cron
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post dhcpd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post fetchmail
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post fsdump
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post grub
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post heartbeat
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post inetd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post jabber
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post lilo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post lvm
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%if 0
%post majordomo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods
%endif

%post mon
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post mysql
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post net
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post postfix
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post postgresql
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post ppp
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%if 0
%post printer
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods
%endif

%post proftpd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post cvs-pserver
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post qmail
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post samba
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post sentry
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post sendmail
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post squid
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post sshd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post wuftpd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post xinetd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post nfs
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post quota
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post software
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post monitor
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post syslog
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post admin-tools
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post system
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post nis
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post passwd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%if 0
%post usermin
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods
%endif

%post useradmin
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%files -f base.lang
%defattr(644,root,root,755)
%doc LICENCE.gz LICENCE.ja.gz
%attr(750,root,root) %dir /var/log/webmin
%attr(754,root,root) /etc/rc.d/init.d/webmin

%attr(755,root,root) %{_datadir}/webmin/*.pl
%attr(755,root,root) %{_datadir}/webmin/*.cgi
%{_datadir}/webmin/images
%{_datadir}/webmin/config-*
%{_datadir}/webmin/install-type
%{_datadir}/webmin/mime.types
%{_datadir}/webmin/*.txt
%{_datadir}/webmin/version

%attr(750,root,root) %dir %{_sysconfdir}/webmin
%config(noreplace) %{_sysconfdir}/webmin/config
%config(noreplace) %{_sysconfdir}/webmin/miniserv.conf
%attr(600,root,root) %config(noreplace) %{_sysconfdir}/webmin/miniserv.pem
# %config(noreplace) %{_sysconfdir}/webmin/miniserv.users
%{_sysconfdir}/webmin/perl-path
%{_sysconfdir}/webmin/var-path
%{_sysconfdir}/webmin/version
# %config(noreplace) %{_sysconfdir}/webmin/webmin.acl
# %config(noreplace) %{_sysconfdir}/webmin/webmin.groups

# ACL #
%dir %{_sysconfdir}/webmin/acl
%dir %{_datadir}/webmin/acl
%attr(755,root,root) %{_datadir}/webmin/acl/*.cgi
%{_datadir}/webmin/acl/config
%{_datadir}/webmin/acl/config-*
%{_datadir}/webmin/acl/config.info
%{_datadir}/webmin/acl/defaultacl
%{_datadir}/webmin/acl/images
%{_datadir}/webmin/acl/module.info
%{_datadir}/webmin/acl/openssl.cnf
%{_datadir}/webmin/acl/*-*.pl
%{_datadir}/webmin/acl/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/acl/config

# MAN
%dir %{_sysconfdir}/webmin/man
%dir %{_datadir}/webmin/man
%attr(755,root,root) %{_datadir}/webmin/man/*.cgi
%{_datadir}/webmin/man/config-*
%{_datadir}/webmin/man/config.info
%{_datadir}/webmin/man/images
%{_datadir}/webmin/man/module.info
%{_datadir}/webmin/man/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/man/config

# PAM
%dir %{_sysconfdir}/webmin/pam
%dir %{_datadir}/webmin/pam
%attr(755,root,root) %{_datadir}/webmin/pam/*.cgi
%{_datadir}/webmin/pam/config-*
%{_datadir}/webmin/pam/config.info
%{_datadir}/webmin/pam/images
%{_datadir}/webmin/pam/module.info
%{_datadir}/webmin/pam/*-*.pl
%{_datadir}/webmin/pam/*_*.pl
%{_datadir}/webmin/pam/template.pl
%config(noreplace) %{_sysconfdir}/webmin/pam/config

# SERVERS #
%dir %{_sysconfdir}/webmin/servers
%dir %{_datadir}/webmin/servers
%attr(755,root,root) %{_datadir}/webmin/servers/*.cgi
%{_datadir}/webmin/servers/config
%{_datadir}/webmin/servers/config.info
%{_datadir}/webmin/servers/defaultacl
%{_datadir}/webmin/servers/images
%{_datadir}/webmin/servers/module.info
%{_datadir}/webmin/servers/*-*.pl
%{_datadir}/webmin/servers/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/servers/config

# WEBMIN #
%dir %{_sysconfdir}/webmin/webmin
%dir %{_datadir}/webmin/webmin
%attr(755,root,root) %{_datadir}/webmin/webmin/*.cgi
%{_datadir}/webmin/webmin/config
%{_datadir}/webmin/webmin/images
%{_datadir}/webmin/webmin/*.risk
%{_datadir}/webmin/webmin/*.skill
%{_datadir}/webmin/webmin/module.info
%{_datadir}/webmin/webmin/*.pl

#### HARDWARE ####

# TIME
%dir %{_sysconfdir}/webmin/time
%dir %{_datadir}/webmin/time
%attr(755,root,root) %{_datadir}/webmin/time/*.cgi
%{_datadir}/webmin/time/config
%{_datadir}/webmin/time/config-*
%{_datadir}/webmin/time/config.info
%{_datadir}/webmin/time/defaultacl
%{_datadir}/webmin/time/images
%{_datadir}/webmin/time/module.info
%{_datadir}/webmin/time/*-*.pl
%{_datadir}/webmin/time/*_*.pl
%{_datadir}/webmin/time/time.js
%config(noreplace) %{_sysconfdir}/webmin/time/config

%files admin-tools -f admin-tools.lang
%defattr(644,root,root,755)
# TELNET
%dir %{_sysconfdir}/webmin/telnet
%dir %{_datadir}/webmin/telnet
%attr(755,root,root) %{_datadir}/webmin/telnet/*.cgi
%{_datadir}/webmin/telnet/config
%{_datadir}/webmin/telnet/config-*
%{_datadir}/webmin/telnet/config.info
%{_datadir}/webmin/telnet/images
%{_datadir}/webmin/telnet/module.info
%{_datadir}/webmin/telnet/jta20.jar
%{_datadir}/webmin/telnet/*.conf
%config(noreplace) %{_sysconfdir}/webmin/telnet/config

# CUSTOM
%dir %{_sysconfdir}/webmin/custom
%dir %{_datadir}/webmin/custom
%attr(755,root,root) %{_datadir}/webmin/custom/*.cgi
%{_datadir}/webmin/custom/config
%{_datadir}/webmin/custom/config.info
%{_datadir}/webmin/custom/defaultacl
%{_datadir}/webmin/custom/images
%{_datadir}/webmin/custom/module.info
%{_datadir}/webmin/custom/*-*.pl
%{_datadir}/webmin/custom/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/custom/config

# FILE
%dir %{_sysconfdir}/webmin/file
%dir %{_datadir}/webmin/file
%attr(755,root,root) %{_datadir}/webmin/file/*.cgi
%{_datadir}/webmin/file/config-*
%{_datadir}/webmin/file/defaultacl
%{_datadir}/webmin/file/images
%{_datadir}/webmin/file/module.info
%{_datadir}/webmin/file/*.pl
# These are source files; not necessary to run...
#%{_datadir}/webmin/file/*.java
%{_datadir}/webmin/file/*.class

# SHELL
%dir %{_sysconfdir}/webmin/shell
%dir %{_datadir}/webmin/shell
%attr(755,root,root) %{_datadir}/webmin/shell/*.cgi
%{_datadir}/webmin/shell/defaultacl
%{_datadir}/webmin/shell/images
%{_datadir}/webmin/shell/module.info
%{_datadir}/webmin/shell/*.pl

# WEBMINLOG
%dir %{_sysconfdir}/webmin/webminlog
%dir %{_datadir}/webmin/webminlog
%attr(755,root,root) %{_datadir}/webmin/webminlog/*.cgi
%{_datadir}/webmin/webminlog/images
%{_datadir}/webmin/webminlog/module.info
%{_datadir}/webmin/webminlog/*.pl

#### DISKS ####
%files disk-tools -f disk-tools.lang
%defattr(644,root,root,755)

# FDISK
%dir %{_sysconfdir}/webmin/fdisk
%dir %{_datadir}/webmin/fdisk
%attr(755,root,root) %{_datadir}/webmin/fdisk/*.cgi
%{_datadir}/webmin/fdisk/config
%{_datadir}/webmin/fdisk/defaultacl
%{_datadir}/webmin/fdisk/images
%{_datadir}/webmin/fdisk/module.info
%{_datadir}/webmin/fdisk/*.pl
%config(noreplace) %{_sysconfdir}/webmin/fdisk/config

# RAID
%dir %{_sysconfdir}/webmin/raid
%dir %{_datadir}/webmin/raid
%attr(755,root,root) %{_datadir}/webmin/raid/*.cgi
%{_datadir}/webmin/raid/config
%{_datadir}/webmin/raid/config.info
%{_datadir}/webmin/raid/images
%{_datadir}/webmin/raid/module.info
%{_datadir}/webmin/raid/*-*.pl
%{_datadir}/webmin/raid/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/raid/config

# GRUB
%files grub -f grub.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/grub
%dir %{_datadir}/webmin/grub
%attr(755,root,root) %{_datadir}/webmin/grub/*.cgi
%{_datadir}/webmin/grub/config
%{_datadir}/webmin/grub/config-*
%{_datadir}/webmin/grub/config.info
%{_datadir}/webmin/grub/images
%{_datadir}/webmin/grub/module.info
%{_datadir}/webmin/grub/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/grub/config

# JABBER
%files jabber -f jabber.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/jabber
%dir %{_datadir}/webmin/jabber
%attr(755,root,root) %{_datadir}/webmin/jabber/*.cgi
%{_datadir}/webmin/jabber/config
%{_datadir}/webmin/jabber/config-*
%{_datadir}/webmin/jabber/config.info
%{_datadir}/webmin/jabber/images
%{_datadir}/webmin/jabber/module.info
%{_datadir}/webmin/jabber/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/jabber/config

# LILO
%files lilo -f lilo.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lilo
%dir %{_datadir}/webmin/lilo
%attr(755,root,root) %{_datadir}/webmin/lilo/*.cgi
%{_datadir}/webmin/lilo/config
%{_datadir}/webmin/lilo/config-*
%{_datadir}/webmin/lilo/config.info
%{_datadir}/webmin/lilo/images
%{_datadir}/webmin/lilo/module.info
%{_datadir}/webmin/lilo/*-*.pl
%{_datadir}/webmin/lilo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/lilo/config

# LVM
%files lvm -f lvm.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lvm
%dir %{_datadir}/webmin/lvm
%attr(755,root,root) %{_datadir}/webmin/lvm/*.cgi
%{_datadir}/webmin/lvm/images
%{_datadir}/webmin/lvm/module.info
%{_datadir}/webmin/lvm/*-*.pl
%{_datadir}/webmin/lvm/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/lvm/config

%if 0
# LP
%files printer -f lpadmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lpadmin
%dir %{_datadir}/webmin/lpadmin
%attr(755,root,root) %{_datadir}/webmin/lpadmin/*.cgi
%{_datadir}/webmin/lpadmin/config-*
%{_datadir}/webmin/lpadmin/config.info
%{_datadir}/webmin/lpadmin/defaultacl
%{_datadir}/webmin/lpadmin/drivers
%{_datadir}/webmin/lpadmin/images
%{_datadir}/webmin/lpadmin/module.info
%{_datadir}/webmin/lpadmin/*-*.pl
%{_datadir}/webmin/lpadmin/*_*.pl
%{_datadir}/webmin/lpadmin/sortdrivers.pl
%{_datadir}/webmin/lpadmin/*.ps
%{_datadir}/webmin/lpadmin/stp
%{_datadir}/webmin/lpadmin/*.txt
%config(noreplace) %{_sysconfdir}/webmin/lpadmin/config
%endif

# MON
%files mon -f mon.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mon
%dir %{_datadir}/webmin/mon
%attr(755,root,root) %{_datadir}/webmin/mon/*.cgi
%{_datadir}/webmin/mon/config
%{_datadir}/webmin/mon/config.info
%{_datadir}/webmin/mon/images
%{_datadir}/webmin/mon/module.info
#%{_datadir}/webmin/mon/monshowrc
%{_datadir}/webmin/mon/*-*.pl
%{_datadir}/webmin/mon/*_*.pl
%{_datadir}/webmin/mon/moncmd.pl
%config(noreplace) %{_sysconfdir}/webmin/mon/config

# NET
%files net -f net.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/net
%dir %{_datadir}/webmin/net
%attr(755,root,root) %{_datadir}/webmin/net/*.cgi
%{_datadir}/webmin/net/config-*
%{_datadir}/webmin/net/config.info
%{_datadir}/webmin/net/defaultacl
%{_datadir}/webmin/net/images
%{_datadir}/webmin/net/module.info
%{_datadir}/webmin/net/*-*.pl
%{_datadir}/webmin/net/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/net/config

#### SYSTEM ####
%files system -f system.lang
%defattr(644,root,root,755)

# INIT
%dir %{_sysconfdir}/webmin/init
%dir %{_datadir}/webmin/init
%attr(755,root,root) %{_datadir}/webmin/init/*.cgi
%{_datadir}/webmin/init/config-*
%{_datadir}/webmin/init/config.info
%{_datadir}/webmin/init/defaultacl
#%{_datadir}/webmin/init/help
%{_datadir}/webmin/init/images
%{_datadir}/webmin/init/module.info
%{_datadir}/webmin/init/*-*.pl
%{_datadir}/webmin/init/*_*.pl
%{_datadir}/webmin/init/*boot.pl
%{_datadir}/webmin/init/*.risk
%config(noreplace) %{_sysconfdir}/webmin/init/config

# INITTAB
%dir %{_sysconfdir}/webmin/inittab
%dir %{_datadir}/webmin/inittab
%attr(755,root,root) %{_datadir}/webmin/inittab/*.cgi
%{_datadir}/webmin/inittab/config
%{_datadir}/webmin/inittab/config.info
%{_datadir}/webmin/inittab/defaultacl
%{_datadir}/webmin/inittab/images
%{_datadir}/webmin/inittab/module.info
%{_datadir}/webmin/inittab/*-*.pl
%{_datadir}/webmin/inittab/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/inittab/config

# MOUNT
%dir %{_sysconfdir}/webmin/mount
%dir %{_datadir}/webmin/mount
%attr(755,root,root) %{_datadir}/webmin/mount/*.cgi
%{_datadir}/webmin/mount/config-*
%{_datadir}/webmin/mount/config.info
#%{_datadir}/webmin/mount/help
%{_datadir}/webmin/mount/images
%{_datadir}/webmin/mount/module.info
%{_datadir}/webmin/mount/*-*.pl
%{_datadir}/webmin/mount/*_*.pl
%{_datadir}/webmin/mount/*.risk
%{_datadir}/webmin/mount/*.skill
%config(noreplace) %{_sysconfdir}/webmin/mount/config

# PROC
%dir %{_sysconfdir}/webmin/proc
%dir %{_datadir}/webmin/proc
%attr(755,root,root) %{_datadir}/webmin/proc/*.cgi
%{_datadir}/webmin/proc/config-*
%{_datadir}/webmin/proc/config.info
%{_datadir}/webmin/proc/defaultacl
%{_datadir}/webmin/proc/images
%{_datadir}/webmin/proc/module.info
%{_datadir}/webmin/proc/*-*.pl
%{_datadir}/webmin/proc/*_*.pl
%{_datadir}/webmin/proc/*.risk
%{_datadir}/webmin/proc/*.skill
%config(noreplace) %{_sysconfdir}/webmin/proc/config

# PASSWD
%files passwd -f passwd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/passwd
%dir %{_datadir}/webmin/passwd
%attr(755,root,root) %{_datadir}/webmin/passwd/*.cgi
%{_datadir}/webmin/passwd/config
%{_datadir}/webmin/passwd/config.info
%{_datadir}/webmin/passwd/defaultacl
%{_datadir}/webmin/passwd/images
%{_datadir}/webmin/passwd/module.info
%{_datadir}/webmin/passwd/*-*.pl
%{_datadir}/webmin/passwd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/passwd/config

%if 0
# USERMIN #
%files usermin -f usermin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/usermin
%dir %{_datadir}/webmin/usermin
%attr(755,root,root) %{_datadir}/webmin/usermin/*.cgi
%{_datadir}/webmin/usermin/config
%{_datadir}/webmin/usermin/config.info
%{_datadir}/webmin/usermin/images
%{_datadir}/webmin/usermin/module.info
%{_datadir}/webmin/usermin/*-*.pl
%{_datadir}/webmin/usermin/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/usermin/config
%endif

# USERADMIN
%files useradmin -f useradmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/useradmin
%dir %{_datadir}/webmin/useradmin
%attr(755,root,root) %{_datadir}/webmin/useradmin/*.cgi
%{_datadir}/webmin/useradmin/config-*
%{_datadir}/webmin/useradmin/config.info
%{_datadir}/webmin/useradmin/defaultacl
%{_datadir}/webmin/useradmin/images
%{_datadir}/webmin/useradmin/module.info
%{_datadir}/webmin/useradmin/*-*.pl
%{_datadir}/webmin/useradmin/*_*.pl
%{_datadir}/webmin/useradmin/*.risk
%{_datadir}/webmin/useradmin/*.skill
%config(noreplace) %{_sysconfdir}/webmin/useradmin/config

# NFS EXPORTS
%files nfs -f exports.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/exports
%dir %{_datadir}/webmin/exports
%attr(755,root,root) %{_datadir}/webmin/exports/*.cgi
%{_datadir}/webmin/exports/config-*
%{_datadir}/webmin/exports/config.info
%{_datadir}/webmin/exports/images
%{_datadir}/webmin/exports/module.info
%{_datadir}/webmin/exports/*-*.pl
%{_datadir}/webmin/exports/*_*.pl
%{_datadir}/webmin/exports/*.risk
%{_datadir}/webmin/exports/*.skill
%config(noreplace) %{_sysconfdir}/webmin/exports/config

# QUOTA
%files quota -f quota.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/quota
%dir %{_datadir}/webmin/quota
%attr(755,root,root) %{_datadir}/webmin/quota/*.cgi
%{_datadir}/webmin/quota/config-*
%{_datadir}/webmin/quota/config.info
%{_datadir}/webmin/quota/defaultacl
%{_datadir}/webmin/quota/images
%{_datadir}/webmin/quota/module.info
%{_datadir}/webmin/quota/*-*.pl
%{_datadir}/webmin/quota/*_*.pl
%{_datadir}/webmin/quota/ed*.pl
%config(noreplace) %{_sysconfdir}/webmin/quota/config

# SOFTWARE
%files software -f software.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/software
%dir %{_datadir}/webmin/software
%attr(755,root,root) %{_datadir}/webmin/software/*.cgi
%{_datadir}/webmin/software/config-*
%{_datadir}/webmin/software/config.info
%{_datadir}/webmin/software/images
%{_datadir}/webmin/software/module.info
%{_datadir}/webmin/software/*-*.pl
%{_datadir}/webmin/software/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/software/config

# STATUS
%files monitor -f status.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/status
%dir %{_datadir}/webmin/status
%attr(755,root,root) %{_datadir}/webmin/status/*.cgi
%{_datadir}/webmin/status/config
%{_datadir}/webmin/status/config-*
%{_datadir}/webmin/status/config.info
%{_datadir}/webmin/status/defaultacl
%{_datadir}/webmin/status/images
%{_datadir}/webmin/status/module.info
%{_datadir}/webmin/status/*-*.pl
%{_datadir}/webmin/status/*_*.pl
%{_datadir}/webmin/status/monitor.pl
%{_datadir}/webmin/status/services
%config(noreplace) %{_sysconfdir}/webmin/status/config

# SYSLOG
%files syslog -f syslog.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/syslog
%dir %{_datadir}/webmin/syslog
%attr(755,root,root) %{_datadir}/webmin/syslog/*.cgi
%{_datadir}/webmin/syslog/config-*
%{_datadir}/webmin/syslog/config.info
%{_datadir}/webmin/syslog/images
%{_datadir}/webmin/syslog/module.info
%{_datadir}/webmin/syslog/*-*.pl
%{_datadir}/webmin/syslog/*_*.pl
%{_datadir}/webmin/syslog/*.risk
%{_datadir}/webmin/syslog/*.skill
%config(noreplace) %{_sysconfdir}/webmin/syslog/config

#### OTHER #####

# NIS
%files nis -f nis.lang
%defattr(644,root,root,755)
%doc nis/nisupdate.conf
%dir %{_sysconfdir}/webmin/nis
%dir %{_datadir}/webmin/nis
%attr(755,root,root) %{_datadir}/webmin/nis/*.cgi
%{_datadir}/webmin/nis/config-*
%{_datadir}/webmin/nis/config.info
%{_datadir}/webmin/nis/images
%{_datadir}/webmin/nis/module.info
%{_datadir}/webmin/nis/*-*.pl
%{_datadir}/webmin/nis/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/nis/config


#### SERVERS #####

# APACHE #
%files apache -f apache.lang
%defattr(644,root,root,755)
%doc %{_datadir}/webmin/apache/notes
%dir %{_sysconfdir}/webmin/apache
%dir %{_datadir}/webmin/apache
%attr(755,root,root) %{_datadir}/webmin/apache/*.cgi
%{_datadir}/webmin/apache/config-*
%{_datadir}/webmin/apache/config.info
%{_datadir}/webmin/apache/defaultacl
%{_datadir}/webmin/apache/images
%{_datadir}/webmin/apache/module.info
%{_datadir}/webmin/apache/*-*.pl
%{_datadir}/webmin/apache/*_*.pl
%{_datadir}/webmin/apache/autoindex.pl
%{_datadir}/webmin/apache/browsermatch.pl
%{_datadir}/webmin/apache/c*e.pl
%{_datadir}/webmin/apache/p*.pl
%{_datadir}/webmin/apache/worker.pl
%config(noreplace) %{_sysconfdir}/webmin/apache/config

# AT
%files at -f at.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/at
%dir %{_datadir}/webmin/at
%attr(755,root,root) %{_datadir}/webmin/at/*.cgi
%{_datadir}/webmin/at/config-*
%{_datadir}/webmin/at/config.info
%{_datadir}/webmin/at/defaultacl
%{_datadir}/webmin/at/images
%{_datadir}/webmin/at/module.info
%{_datadir}/webmin/at/*-*.pl
%{_datadir}/webmin/at/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/at/config

# BIND 8/9 #
%files bind8 -f bind8.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/bind8
%dir %{_datadir}/webmin/bind8
%attr(755,root,root) %{_datadir}/webmin/bind8/*.cgi
%{_datadir}/webmin/bind8/config-*
%{_datadir}/webmin/bind8/config.info
%{_datadir}/webmin/bind8/defaultacl
%{_datadir}/webmin/bind8/images
%{_datadir}/webmin/bind8/module.info
%{_datadir}/webmin/bind8/*-*.pl
%{_datadir}/webmin/bind8/*_*.pl
%{_datadir}/webmin/bind8/db.cache
%config(noreplace) %{_sysconfdir}/webmin/bind8/config

# BURNER #
%files burner -f burner.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/burner
%dir %{_datadir}/webmin/burner
%attr(755,root,root) %{_datadir}/webmin/burner/*.cgi
%{_datadir}/webmin/burner/config
%{_datadir}/webmin/burner/images
%{_datadir}/webmin/burner/module.info
%{_datadir}/webmin/burner/*-*.pl
%{_datadir}/webmin/burner/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/burner/config

%if 0
# CFENGINE
%files cfengine -f cfengine.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cfengine
%dir %{_datadir}/webmin/cfengine
%attr(755,root,root) %{_datadir}/webmin/cfengine/*.cgi
%{_datadir}/webmin/cfengine/config
%{_datadir}/webmin/cfengine/config-*
%{_datadir}/webmin/cfengine/config.info
%{_datadir}/webmin/cfengine/images
%{_datadir}/webmin/cfengine/module.info
%{_datadir}/webmin/cfengine/*-*.pl
%{_datadir}/webmin/cfengine/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cfengine/config
%endif

# CLUSTER-SOFTWARE
%files cluster-software -f cluster-software.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-software
%dir %{_datadir}/webmin/cluster-software
%attr(755,root,root) %{_datadir}/webmin/cluster-software/*.cgi
%{_datadir}/webmin/cluster-software/config
%{_datadir}/webmin/cluster-software/config.info
%{_datadir}/webmin/cluster-software/images
%{_datadir}/webmin/cluster-software/module.info
%{_datadir}/webmin/cluster-software/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-software/config

# CLUSTER-USERADMIN
%files cluster-useradmin -f cluster-useradmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-useradmin
%dir %{_datadir}/webmin/cluster-useradmin
%attr(755,root,root) %{_datadir}/webmin/cluster-useradmin/*.cgi
%{_datadir}/webmin/cluster-useradmin/config
%{_datadir}/webmin/cluster-useradmin/config.info
%{_datadir}/webmin/cluster-useradmin/images
%{_datadir}/webmin/cluster-useradmin/module.info
%{_datadir}/webmin/cluster-useradmin/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-useradmin/config

# CRON
%files cron -f cron.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cron
%dir %{_datadir}/webmin/cron
%attr(755,root,root) %{_datadir}/webmin/cron/*.cgi
%{_datadir}/webmin/cron/config-*
%{_datadir}/webmin/cron/config.info
%{_datadir}/webmin/cron/defaultacl
#%{_datadir}/webmin/cron/help
%{_datadir}/webmin/cron/images
%{_datadir}/webmin/cron/module.info
%{_datadir}/webmin/cron/*-*.pl
%{_datadir}/webmin/cron/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cron/config

# DHCPD #
%files dhcpd -f dhcpd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/dhcpd
%dir %{_datadir}/webmin/dhcpd
%attr(755,root,root) %{_datadir}/webmin/dhcpd/*.cgi
%{_datadir}/webmin/dhcpd/config-*
%{_datadir}/webmin/dhcpd/config.info
%{_datadir}/webmin/dhcpd/defaultacl
%{_datadir}/webmin/dhcpd/images
%{_datadir}/webmin/dhcpd/module.info
%{_datadir}/webmin/dhcpd/*-*.pl
%{_datadir}/webmin/dhcpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/dhcpd/config

# FETCHMAIL #
%files fetchmail -f fetchmail.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/fetchmail
%dir %{_datadir}/webmin/fetchmail
%attr(755,root,root) %{_datadir}/webmin/fetchmail/*.cgi
%{_datadir}/webmin/fetchmail/config
%{_datadir}/webmin/fetchmail/config-*
%{_datadir}/webmin/fetchmail/config.info
%{_datadir}/webmin/fetchmail/defaultacl
%{_datadir}/webmin/fetchmail/images
%{_datadir}/webmin/fetchmail/module.info
%{_datadir}/webmin/fetchmail/*-*.pl
%{_datadir}/webmin/fetchmail/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/fetchmail/config

# DUMP #
%files fsdump -f fsdump.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/fsdump
%dir %{_datadir}/webmin/fsdump
%attr(755,root,root) %{_datadir}/webmin/fsdump/*.cgi
%{_datadir}/webmin/fsdump/images
%{_datadir}/webmin/fsdump/module.info
%{_datadir}/webmin/fsdump/*-*.pl
%{_datadir}/webmin/fsdump/*_*.pl
%{_datadir}/webmin/fsdump/backup.pl
%config(noreplace) %{_sysconfdir}/webmin/fsdump/config

# HEARTBEAT #
%files heartbeat -f heartbeat.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/heartbeat
%dir %{_datadir}/webmin/heartbeat
%attr(755,root,root) %{_datadir}/webmin/heartbeat/*.cgi
%{_datadir}/webmin/heartbeat/config
%{_datadir}/webmin/heartbeat/config-*
%{_datadir}/webmin/heartbeat/config.info
%{_datadir}/webmin/heartbeat/images
%{_datadir}/webmin/heartbeat/module.info
%{_datadir}/webmin/heartbeat/*-*.pl
%{_datadir}/webmin/heartbeat/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/heartbeat/config

# INETD
%files inetd -f inetd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/inetd
%dir %{_datadir}/webmin/inetd
%attr(755,root,root) %{_datadir}/webmin/inetd/*.cgi
%{_datadir}/webmin/inetd/config-*
%{_datadir}/webmin/inetd/config.info
#%dir %{_datadir}/webmin/inetd/help
%{_datadir}/webmin/inetd/images
%{_datadir}/webmin/inetd/module.info
%{_datadir}/webmin/inetd/*-*.pl
%{_datadir}/webmin/inetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/inetd/config

%if 0
# MAJORDOMO #
%files majordomo -f majordomo.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/majordomo
%dir %{_datadir}/webmin/majordomo
%attr(755,root,root) %{_datadir}/webmin/majordomo/*.cgi
%{_datadir}/webmin/majordomo/config
%{_datadir}/webmin/majordomo/config-*
%{_datadir}/webmin/majordomo/config.info
%{_datadir}/webmin/majordomo/defaultacl
%{_datadir}/webmin/majordomo/images
%{_datadir}/webmin/majordomo/module.info
%{_datadir}/webmin/majordomo/*-*.pl
%{_datadir}/webmin/majordomo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/majordomo/config
%endif

# MYSQL #
%files mysql -f mysql.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mysql
%dir %{_datadir}/webmin/mysql
%attr(755,root,root) %{_datadir}/webmin/mysql/*.cgi
%{_datadir}/webmin/mysql/config
%{_datadir}/webmin/mysql/config-*
%{_datadir}/webmin/mysql/config.info
%{_datadir}/webmin/mysql/defaultacl
%{_datadir}/webmin/mysql/images
%{_datadir}/webmin/mysql/module.info
%{_datadir}/webmin/mysql/*-*.pl
%{_datadir}/webmin/mysql/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/mysql/config

# POSTFIX #
%files postfix -f postfix.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postfix
%dir %{_datadir}/webmin/postfix
%attr(755,root,root) %{_datadir}/webmin/postfix/*.cgi
%{_datadir}/webmin/postfix/config
%{_datadir}/webmin/postfix/config-*
%{_datadir}/webmin/postfix/config.info
%{_datadir}/webmin/postfix/defaultacl
%{_datadir}/webmin/postfix/images
%{_datadir}/webmin/postfix/module.info
%{_datadir}/webmin/postfix/*-*.pl
%{_datadir}/webmin/postfix/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/postfix/config

# POSTGRESQL #
%files postgresql -f postgresql.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postgresql
%dir %{_datadir}/webmin/postgresql
%attr(755,root,root) %{_datadir}/webmin/postgresql/*.cgi
%{_datadir}/webmin/postgresql/config
%{_datadir}/webmin/postgresql/config-*
%{_datadir}/webmin/postgresql/config.info
%{_datadir}/webmin/postgresql/defaultacl
%{_datadir}/webmin/postgresql/images
%{_datadir}/webmin/postgresql/module.info
%{_datadir}/webmin/postgresql/*-*.pl
%{_datadir}/webmin/postgresql/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/postgresql/config

# PROFTPD #
%files proftpd -f proftpd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/proftpd
%dir %{_datadir}/webmin/proftpd
%attr(755,root,root) %{_datadir}/webmin/proftpd/*.cgi
%{_datadir}/webmin/proftpd/config
%{_datadir}/webmin/proftpd/config-*
%{_datadir}/webmin/proftpd/config.info
%{_datadir}/webmin/proftpd/images
%{_datadir}/webmin/proftpd/module.info
%{_datadir}/webmin/proftpd/*-*.pl
%{_datadir}/webmin/proftpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/proftpd/config

# CVS-PSERVER #
%files cvs-pserver -f pserver.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pserver
%dir %{_datadir}/webmin/pserver
%attr(755,root,root) %{_datadir}/webmin/pserver/*.cgi
%{_datadir}/webmin/pserver/config
%{_datadir}/webmin/pserver/config.info
%{_datadir}/webmin/pserver/images
%{_datadir}/webmin/pserver/module.info
%{_datadir}/webmin/pserver/*-*.pl
%{_datadir}/webmin/pserver/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/pserver/config

# PAP (PPPD) #
%files ppp -f pap.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pap
%dir %{_datadir}/webmin/pap
%attr(755,root,root) %{_datadir}/webmin/pap/*.cgi
%{_datadir}/webmin/pap/config-*
%{_datadir}/webmin/pap/config.info
%{_datadir}/webmin/pap/images
%{_datadir}/webmin/pap/module.info
%{_datadir}/webmin/pap/*-*.pl
%{_datadir}/webmin/pap/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/pap/config

# QMAIL #
%files qmail -f qmailadmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/qmailadmin
%dir %{_datadir}/webmin/qmailadmin
%attr(755,root,root) %{_datadir}/webmin/qmailadmin/*.cgi
%{_datadir}/webmin/qmailadmin/config
%{_datadir}/webmin/qmailadmin/config.info
%{_datadir}/webmin/qmailadmin/images
%{_datadir}/webmin/qmailadmin/module.info
%{_datadir}/webmin/qmailadmin/*-*.pl
%{_datadir}/webmin/qmailadmin/*_*.pl
%{_datadir}/webmin/qmailadmin/filter.pl
%attr(755,root,root) %{_datadir}/webmin/qmailadmin/autoreply.pl
%config(noreplace) %{_sysconfdir}/webmin/qmailadmin/config

# SAMBA #
%files samba -f samba.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/samba
%dir %{_datadir}/webmin/samba
%attr(755,root,root) %{_datadir}/webmin/samba/*.cgi
%{_datadir}/webmin/samba/config-*
%{_datadir}/webmin/samba/config.info
%{_datadir}/webmin/samba/defaultacl
%{_datadir}/webmin/samba/images
%{_datadir}/webmin/samba/module.info
%{_datadir}/webmin/samba/*-*.pl
%{_datadir}/webmin/samba/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/samba/config

# SENTRY #
%files sentry -f sentry.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sentry
%dir %{_datadir}/webmin/sentry
%attr(755,root,root) %{_datadir}/webmin/sentry/*.cgi
%{_datadir}/webmin/sentry/config
%{_datadir}/webmin/sentry/config-*
%{_datadir}/webmin/sentry/config.info
%{_datadir}/webmin/sentry/images
%{_datadir}/webmin/sentry/module.info
%{_datadir}/webmin/sentry/*-*.pl
%{_datadir}/webmin/sentry/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/sentry/config

# SQUID #
%files squid -f squid.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/squid
%dir %{_datadir}/webmin/squid
%attr(755,root,root) %{_datadir}/webmin/squid/*.cgi
%{_datadir}/webmin/squid/config-*
%{_datadir}/webmin/squid/config.info
%{_datadir}/webmin/squid/defaultacl
%{_datadir}/webmin/squid/images
%{_datadir}/webmin/squid/module.info
%{_datadir}/webmin/squid/*-*.pl
%{_datadir}/webmin/squid/*_*.pl
%{_datadir}/webmin/squid/*.risk
%{_datadir}/webmin/squid/*.skill
%config(noreplace) %{_sysconfdir}/webmin/squid/config

# SSHD #
%files sshd -f sshd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sshd
%dir %{_datadir}/webmin/sshd
%attr(755,root,root) %{_datadir}/webmin/sshd/*.cgi
%{_datadir}/webmin/sshd/config
%{_datadir}/webmin/sshd/config-*
%{_datadir}/webmin/sshd/config.info
%{_datadir}/webmin/sshd/images
%{_datadir}/webmin/sshd/module.info
%{_datadir}/webmin/sshd/*-*.pl
%{_datadir}/webmin/sshd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/sshd/config

# WU-FTPD #
%files wuftpd -f wuftpd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/wuftpd
%dir %{_datadir}/webmin/wuftpd
%attr(755,root,root) %{_datadir}/webmin/wuftpd/*.cgi
%{_datadir}/webmin/wuftpd/config-*
%{_datadir}/webmin/wuftpd/config.info
%{_datadir}/webmin/wuftpd/images
%{_datadir}/webmin/wuftpd/module.info
%{_datadir}/webmin/wuftpd/*-*.pl
%{_datadir}/webmin/wuftpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/wuftpd/config

# XINETD
%files xinetd -f xinetd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/xinetd
%dir %{_datadir}/webmin/xinetd
%attr(755,root,root) %{_datadir}/webmin/xinetd/*.cgi
%{_datadir}/webmin/xinetd/config
%{_datadir}/webmin/xinetd/config-*
%{_datadir}/webmin/xinetd/config.info
%{_datadir}/webmin/xinetd/images
%{_datadir}/webmin/xinetd/module.info
%{_datadir}/webmin/xinetd/*-*.pl
%{_datadir}/webmin/xinetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/xinetd/config

# THEMES
%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/webmin/caldera
%attr(755,root,root) %{_datadir}/webmin/caldera/*.cgi
%{_datadir}/webmin/caldera/config
%{_datadir}/webmin/caldera/theme.*
%{_datadir}/webmin/caldera/*.css
%{_datadir}/webmin/caldera/*.gif
%{_datadir}/webmin/caldera/*/*
%dir %{_datadir}/webmin/kdestyle
%{_datadir}/webmin/kdestyle/theme.*
%{_datadir}/webmin/kdestyle/*/*
%dir %{_datadir}/webmin/mscstyle3
%attr(755,root,root) %{_datadir}/webmin/mscstyle3/*.cgi
%{_datadir}/webmin/mscstyle3/config
%{_datadir}/webmin/mscstyle3/theme.*
%{_datadir}/webmin/mscstyle3/*/*

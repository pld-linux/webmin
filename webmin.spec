%include        /usr/lib/rpm/macros.perl
Summary:	Webmin - web-based administration	
Summary(pl):	Webmin - administracja przez WWW
Name:		webmin
#Version:	0.87
# Current unofficial tarball version (be carefull; numberring incompatibility):
Version:	0.87.5
%define	source_version	%(echo %{version}|sed -e 's/pre//' -e 's/\\(\\.\\)\\(.\\)$/\\2/')
Release:	1
License:	Distributable (BSD-like)
#Source0:	ftp://ftp.webmin.com/pub/webadmin/%{name}-%{version}.tar.gz
# Unofficial webmin tarballs location (if anybody interested):
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://fudu.curlybracket.com/webadmin/tarballs/%{name}-%{source_version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}-miniserv.conf
Source3:	%{name}-scripts.tar.gz
#Patch0:	%{name}-PLD.patch
Patch0:		%{name}-%{version}-PLD.patch
URL:		http://www.webmin.com/webmin/
BuildRequires:	textutils
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
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	hdparm
Requires:	fdisk
Requires:	webmin-system = %{version}

%description disk-tools

%description -l pl disk-tools

# GRUB
%package grub
Summary:	Webmin - GRUB configuration
Summary(pl):	Webmin - Konfiguracja GRUB-a
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	grub

%description grub

%description -l pl grub

# LILO
%package lilo
Summary:	Webmin - LILO configuration
Summary(pl):	Webmin - Konfiguracja LILO
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	lilo

%description lilo

%description -l pl lilo

# PRINTER
%package printer
Summary:	Webmin - Printer administration	
Summary(pl):	Webmin - Zarz±dzanie drukarkami
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	lpd

%description printer

%description -l pl printer

# NET
%package net
Summary:	Webmin - Network configuration
Summary(pl):	Webmin - Konfiguracja sieci
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Prereq:		rc-scripts

%description net

%description -l pl net

# APACHE
%package apache
Summary:	Webmin - Apache webserver
Summary(pl):	Webmin - Serwer WWW Apache
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	apache

%description apache

%description -l pl apache

# AT
%package at
Summary:	Webmin - At
Summary(pl):	Webmin - At
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	at

%description at

%description -l pl at

# BIND8
%package bind8
Summary:	Webmin - BIND DNS server
Summary(pl):	Webmin - Serwer DNS BIND
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	bind

%description bind8

%description -l pl bind8

# CRON
%package cron
Summary:	Webmin - Cron
Summary(pl):	Webmin - Cron
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	crondaemon

%description cron

%description -l pl cron

# DHCPD
%package dhcpd
Summary:	Webmin - DHCP server	
Summary(pl):	Webmin - Serwer DHCP
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	dhcpd

%description dhcpd

%description -l pl dhcpd

# INETD
%package inetd
Summary:	Webmin - Inetd
Summary(pl):	Webmin - Inetd
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description inetd

%description -l pl inetd

# MAJORDOMO
%package majordomo
Summary:	Webmin - Majordomo List Manager
Summary(pl):	Webmin - Zarz±dca list dyskusyjnych Majordomo
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	majordomo
Requires:	webmin-sendmail = %{version}

%description majordomo

%description -l pl majordomo

# MYSQL
%package mysql
Summary:	Webmin - MySQL server
Summary(pl):	Webmin - Serwer MySQL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	mysql-client

%description mysql

%description -l pl mysql

# POSTFIX
%package postfix
Summary:	Webmin - Postfix	
Summary(pl):	Webmin - Postfix
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	postfix

%description postfix

%description -l pl postfix

# POSTGRESQL
%package postgresql
Summary:	Webmin - PostgreSQL server
Summary(pl):	Webmin - Serwer PostgreSQL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	postgresql-clients

%description postgresql

%description -l pl postgresql

# PPP
%package ppp
Summary:	Webmin - PAP (PPP) usernames and passwords
Summary(pl):	Webmin - Nazwy u¿ytkowników i has³a dla PAP (PPP)
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	ppp

%description ppp

%description -l pl ppp

# SAMBA
%package samba
Summary:	Webmin - Samba
Summary(pl):	Webmin - Samba
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	samba

%description samba

%description -l pl samba

# SENDMAIL
%package sendmail
Summary:	Webmin - Sendmail	
Summary(pl):	Webmin - Sendmail
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	sendmail

%description sendmail

%description -l pl sendmail

# SQUID
%package squid
Summary:	Webmin - Squid proxy
Summary(pl):	Webmin - Serwer proxy Squid
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	squid

%description squid

%description -l pl squid

# WUFTPD
%package wuftpd
Summary:	Webmin - Wu-Ftpd server
Summary(pl):	Webmin - Serwer Wu-Ftpd
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	wu-ftpd

%description wuftpd

%description -l pl wuftpd

# XINETD
%package xinetd
Summary:	Webmin - Xinetd
Summary(pl):	Webmin - Xinetd
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description xinetd

%description -l pl xinetd

# NFS EXPORTS
%package nfs
Summary:	Webmin - NFS server configuration	
Summary(pl):	Webmin - Konfiguracja serwera NFS
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	nfsdaemon

%description nfs

%description -l pl nfs

# QUOTA
%package quota
Summary:	Webmin - Quota management
Summary(pl):	Webmin - Zarz±dzanie quota
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	quota

%description quota

%description -l pl quota

# SOFTWARE
%package software
Summary:	Webmin - Software Packages
Summary(pl):	Webmin -
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	rpm

%description software

%description -l pl software

# STATUS
%package monitor
Summary:	Webmin - Event monitor
Summary(pl):	Webmin - Monitor zdarzeñ
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	crondaemon

%description monitor

%description -l pl monitor

# SYSLOG
%package syslog
Summary:	Webmin - System logger
Summary(pl):	Webmin - Logi systemowe
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	syslogdaemon

%description syslog

%description -l pl syslog

%package admin-tools
Summary:	Webmin - Admin-tools (telnet, file manager, etc)
Summary(pl):	Webmin - Narzêdzia administracyjne (telnet, menad¿er plików, itp.)
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description admin-tools

%description -l pl admin-tools

# PROC, INIT, INITTAB, MOUNT
%package system
Summary:	Webmin - System Configuration
Summary(pl):	Webmin - Konfiguracja systemu 
#Summary:	Webmin - Process Manager
#Summary(pl):	Webmin - Zarz±dzenia procesami
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description system

%description -l pl system

# NIS
%package nis
Summary:	Webmin - NIS configuration
Summary(pl):	Webmin - Konfiguracja NIS
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	webmin-useradmin = %{version}
Requires:	webmin-inetd = %{version}

%description nis

%description -l pl nis

# PASSWD
%package passwd
Summary:	Webmin - Change Passwords
Summary(pl):	Webmin - Zmiany hase³
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	webmin-useradmin = %{version}

%description passwd

%description -l pl passwd

# USERADMIN
%package useradmin
Summary:	Webmin - User account manager
Summary(pl):	Webmin - Obs³uga kont u¿ytkowników
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description useradmin

%description -l pl useradmin

%prep
%setup -q -n %{name}-%{source_version} 
%patch0 -p1
%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/webmin,/var/{log,run}/webmin} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webmin,rc.d/init.d}

cp -rp * $RPM_BUILD_ROOT%{_datadir}/webmin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/webmin
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}
install $RPM_BUILD_ROOT%{_datadir}/webmin/miniserv.pem \
	$RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.pem

%define webmin_lang	%(%{_datadir}/weblang.sh)
%define webmin_help	%(%{_datadir}/webhelp.sh)
# %define webmin_lang	%(echo -n $1 >/dev/null)
# %define webmin_help	%(echo -n $1 >/dev/null)

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

gzip -9nf LICENCE

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

%post grub
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post lilo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post net
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post printer
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post apache
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post at
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post bind8
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post cron
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post dhcpd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post inetd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post majordomo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post mysql
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

%post samba
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post sendmail
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post squid
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

%post useradmin
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%files
%defattr(644,root,root,755)
%doc LICENCE.gz
%attr(750,root,root) %dir /var/log/webmin
%attr(754,root,root) /etc/rc.d/init.d/webmin

%attr(755,root,root) %{_datadir}/webmin/*.pl
%attr(755,root,root) %{_datadir}/webmin/*.cgi
%{_datadir}/webmin/images
%webmin_lang %{_datadir}/webmin/lang
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
%{_datadir}/webmin/acl/config-*
%{_datadir}/webmin/acl/config.info
%{_datadir}/webmin/acl/defaultacl
%{_datadir}/webmin/acl/images
%webmin_lang %{_datadir}/webmin/acl/lang
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
%webmin_help %{_datadir}/webmin/man/help
%{_datadir}/webmin/man/images
%webmin_lang %{_datadir}/webmin/man/lang
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
%webmin_lang %{_datadir}/webmin/pam/lang
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
%webmin_lang %{_datadir}/webmin/servers/lang
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
%webmin_lang %{_datadir}/webmin/webmin/lang
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
%webmin_help %{_datadir}/webmin/time/help
%{_datadir}/webmin/time/images
%webmin_lang %{_datadir}/webmin/time/lang
%{_datadir}/webmin/time/module.info
%{_datadir}/webmin/time/*-*.pl
%{_datadir}/webmin/time/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/time/config

%files admin-tools
%defattr(644,root,root,755)
# TELNET
%dir %{_sysconfdir}/webmin/telnet
%dir %{_datadir}/webmin/telnet
%attr(755,root,root) %{_datadir}/webmin/telnet/*.cgi
%{_datadir}/webmin/telnet/config
%{_datadir}/webmin/telnet/config-*
%{_datadir}/webmin/telnet/config.info
%{_datadir}/webmin/telnet/images
%webmin_lang %{_datadir}/webmin/telnet/lang
%{_datadir}/webmin/telnet/module.info
%{_datadir}/webmin/telnet/jta20.jar
%{_datadir}/webmin/telnet/*.conf
%config(noreplace) %{_sysconfdir}/webmin/telnet/config

# FILE
%dir %{_sysconfdir}/webmin/file
%dir %{_datadir}/webmin/file
%attr(755,root,root) %{_datadir}/webmin/file/*.cgi
%{_datadir}/webmin/file/images
%webmin_lang %{_datadir}/webmin/file/lang
%{_datadir}/webmin/file/module.info
%{_datadir}/webmin/file/*.pl
# These are source files; not necessary to run...
#%{_datadir}/webmin/file/*.java
%{_datadir}/webmin/file/*.class

# CUSTOM
%dir %{_sysconfdir}/webmin/custom
%dir %{_datadir}/webmin/custom
%attr(755,root,root) %{_datadir}/webmin/custom/*.cgi
%{_datadir}/webmin/custom/config
%{_datadir}/webmin/custom/config.info
%{_datadir}/webmin/custom/defaultacl
%webmin_help %{_datadir}/webmin/custom/help
%{_datadir}/webmin/custom/images
%webmin_lang %{_datadir}/webmin/custom/lang
%{_datadir}/webmin/custom/module.info
%{_datadir}/webmin/custom/*-*.pl
%{_datadir}/webmin/custom/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/custom/config

# WEBMINLOG
%dir %{_sysconfdir}/webmin/webminlog
%dir %{_datadir}/webmin/webminlog
%attr(755,root,root) %{_datadir}/webmin/webminlog/*.cgi
%{_datadir}/webmin/webminlog/images
%webmin_lang %{_datadir}/webmin/webminlog/lang
%{_datadir}/webmin/webminlog/module.info
%{_datadir}/webmin/webminlog/*.pl

#### DISKS ####
%files disk-tools
%defattr(644,root,root,755)

# FDISK
%dir %{_sysconfdir}/webmin/fdisk
%dir %{_datadir}/webmin/fdisk
%attr(755,root,root) %{_datadir}/webmin/fdisk/*.cgi
%{_datadir}/webmin/fdisk/defaultacl
%webmin_help %{_datadir}/webmin/fdisk/help
%{_datadir}/webmin/fdisk/images
%webmin_lang %{_datadir}/webmin/fdisk/lang
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
%webmin_lang %{_datadir}/webmin/raid/lang
%{_datadir}/webmin/raid/module.info
%{_datadir}/webmin/raid/*-*.pl
%{_datadir}/webmin/raid/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/raid/config 

# GRUB
%files grub
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/grub
%dir %{_datadir}/webmin/grub
%attr(755,root,root) %{_datadir}/webmin/grub/*.cgi
%{_datadir}/webmin/grub/config
%{_datadir}/webmin/grub/config.info
%{_datadir}/webmin/grub/images
%webmin_lang %{_datadir}/webmin/grub/lang
%{_datadir}/webmin/grub/module.info
%{_datadir}/webmin/grub/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/grub/config

# LILO
%files lilo
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lilo
%dir %{_datadir}/webmin/lilo
%attr(755,root,root) %{_datadir}/webmin/lilo/*.cgi
%{_datadir}/webmin/lilo/config
%{_datadir}/webmin/lilo/config-*
%{_datadir}/webmin/lilo/config.info
%{_datadir}/webmin/lilo/images
%webmin_lang %{_datadir}/webmin/lilo/lang
%{_datadir}/webmin/lilo/module.info
%{_datadir}/webmin/lilo/*-*.pl
%{_datadir}/webmin/lilo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/lilo/config

# LP
%files printer
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lpadmin
%dir %{_datadir}/webmin/lpadmin
%attr(755,root,root) %{_datadir}/webmin/lpadmin/*.cgi
%{_datadir}/webmin/lpadmin/config-*
%{_datadir}/webmin/lpadmin/config.info
%{_datadir}/webmin/lpadmin/defaultacl
%{_datadir}/webmin/lpadmin/drivers
%{_datadir}/webmin/lpadmin/images
%webmin_lang %{_datadir}/webmin/lpadmin/lang
%{_datadir}/webmin/lpadmin/module.info
%{_datadir}/webmin/lpadmin/*-*.pl
%{_datadir}/webmin/lpadmin/*_*.pl
%{_datadir}/webmin/lpadmin/sortdrivers.pl
%{_datadir}/webmin/lpadmin/*.ps
%{_datadir}/webmin/lpadmin/stp
%{_datadir}/webmin/lpadmin/*.txt
%config(noreplace) %{_sysconfdir}/webmin/lpadmin/config

# NET
%files net
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/net
%dir %{_datadir}/webmin/net
%attr(755,root,root) %{_datadir}/webmin/net/*.cgi
%{_datadir}/webmin/net/config-*
%{_datadir}/webmin/net/config.info
%{_datadir}/webmin/net/defaultacl
%{_datadir}/webmin/net/images
%webmin_lang %{_datadir}/webmin/net/lang
%{_datadir}/webmin/net/module.info
%{_datadir}/webmin/net/*-*.pl
%{_datadir}/webmin/net/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/net/config 

#### SYSTEM ####
%files system
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
%webmin_lang %{_datadir}/webmin/init/lang
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
%webmin_help %{_datadir}/webmin/inittab/help
%{_datadir}/webmin/inittab/images
%webmin_lang %{_datadir}/webmin/inittab/lang
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
%webmin_lang %{_datadir}/webmin/mount/lang
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
%webmin_help %{_datadir}/webmin/proc/help
%{_datadir}/webmin/proc/images
%webmin_lang %{_datadir}/webmin/proc/lang
%{_datadir}/webmin/proc/module.info
%{_datadir}/webmin/proc/*-*.pl
%{_datadir}/webmin/proc/*_*.pl
%{_datadir}/webmin/proc/*.risk
%{_datadir}/webmin/proc/*.skill
%config(noreplace) %{_sysconfdir}/webmin/proc/config

# PASSWD
%files passwd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/passwd
%dir %{_datadir}/webmin/passwd
%attr(755,root,root) %{_datadir}/webmin/passwd/*.cgi
%{_datadir}/webmin/passwd/config
%{_datadir}/webmin/passwd/config.info
%{_datadir}/webmin/passwd/defaultacl
%{_datadir}/webmin/passwd/images
%webmin_lang %{_datadir}/webmin/passwd/lang
%{_datadir}/webmin/passwd/module.info
%{_datadir}/webmin/passwd/*-*.pl
%{_datadir}/webmin/passwd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/passwd/config

# USERADMIN
%files useradmin
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/useradmin
%dir %{_datadir}/webmin/useradmin
%attr(755,root,root) %{_datadir}/webmin/useradmin/*.cgi
%{_datadir}/webmin/useradmin/config-*
%{_datadir}/webmin/useradmin/config.info
%{_datadir}/webmin/useradmin/defaultacl
%webmin_help %{_datadir}/webmin/useradmin/help
%{_datadir}/webmin/useradmin/images
%webmin_lang %{_datadir}/webmin/useradmin/lang
%{_datadir}/webmin/useradmin/module.info
%{_datadir}/webmin/useradmin/*-*.pl
%{_datadir}/webmin/useradmin/*_*.pl
%{_datadir}/webmin/useradmin/*.risk
%{_datadir}/webmin/useradmin/*.skill
%config(noreplace) %{_sysconfdir}/webmin/useradmin/config

# NFS EXPORTS
%files nfs
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/exports
%dir %{_datadir}/webmin/exports
%attr(755,root,root) %{_datadir}/webmin/exports/*.cgi
%{_datadir}/webmin/exports/config-*
%{_datadir}/webmin/exports/config.info
%webmin_help %{_datadir}/webmin/exports/help
%{_datadir}/webmin/exports/images
%webmin_lang %{_datadir}/webmin/exports/lang
%{_datadir}/webmin/exports/module.info
%{_datadir}/webmin/exports/*-*.pl
%{_datadir}/webmin/exports/*_*.pl
%{_datadir}/webmin/exports/*.risk
%{_datadir}/webmin/exports/*.skill
%config(noreplace) %{_sysconfdir}/webmin/exports/config

# QUOTA
%files quota
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/quota
%dir %{_datadir}/webmin/quota
%attr(755,root,root) %{_datadir}/webmin/quota/*.cgi
%{_datadir}/webmin/quota/config-*
%{_datadir}/webmin/quota/config.info
%{_datadir}/webmin/quota/defaultacl
%webmin_help %{_datadir}/webmin/quota/help
%{_datadir}/webmin/quota/images
%webmin_lang %{_datadir}/webmin/quota/lang
%{_datadir}/webmin/quota/module.info
%{_datadir}/webmin/quota/*-*.pl
%{_datadir}/webmin/quota/*_*.pl
%{_datadir}/webmin/quota/ed*.pl
%config(noreplace) %{_sysconfdir}/webmin/quota/config

# SOFTWARE
%files software
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/software
%dir %{_datadir}/webmin/software
%attr(755,root,root) %{_datadir}/webmin/software/*.cgi
%{_datadir}/webmin/software/config-*
%{_datadir}/webmin/software/config.info
%webmin_help %{_datadir}/webmin/software/help
%{_datadir}/webmin/software/images
%webmin_lang %{_datadir}/webmin/software/lang
%{_datadir}/webmin/software/module.info
%{_datadir}/webmin/software/*-*.pl
%{_datadir}/webmin/software/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/software/config

# STATUS
%files monitor
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/status
%dir %{_datadir}/webmin/status
%attr(755,root,root) %{_datadir}/webmin/status/*.cgi
%{_datadir}/webmin/status/config
%{_datadir}/webmin/status/config-*
%{_datadir}/webmin/status/config.info
%{_datadir}/webmin/status/images
%webmin_lang %{_datadir}/webmin/status/lang
%{_datadir}/webmin/status/module.info
%{_datadir}/webmin/status/*-*.pl
%{_datadir}/webmin/status/*_*.pl
%{_datadir}/webmin/status/services
%config(noreplace) %{_sysconfdir}/webmin/status/config

# SYSLOG
%files syslog
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/syslog
%dir %{_datadir}/webmin/syslog
%attr(755,root,root) %{_datadir}/webmin/syslog/*.cgi
%{_datadir}/webmin/syslog/config-*
%{_datadir}/webmin/syslog/config.info
%{_datadir}/webmin/syslog/images
%webmin_lang %{_datadir}/webmin/syslog/lang
%{_datadir}/webmin/syslog/module.info
%{_datadir}/webmin/syslog/*-*.pl
%{_datadir}/webmin/syslog/*_*.pl
%{_datadir}/webmin/syslog/*.risk
%{_datadir}/webmin/syslog/*.skill
%config(noreplace) %{_sysconfdir}/webmin/syslog/config

#### OTHER #####

# NIS
%files nis
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/nis
%dir %{_datadir}/webmin/nis
%attr(755,root,root) %{_datadir}/webmin/nis/*.cgi
%{_datadir}/webmin/nis/config-*
%{_datadir}/webmin/nis/config.info
%{_datadir}/webmin/nis/images
%webmin_lang %{_datadir}/webmin/nis/lang
%{_datadir}/webmin/nis/module.info
%{_datadir}/webmin/nis/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/nis/config


#### SERVERS #####

# APACHE #
%files apache
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/apache
%dir %{_datadir}/webmin/apache
%attr(755,root,root) %{_datadir}/webmin/apache/*.cgi
%{_datadir}/webmin/apache/config-*
%{_datadir}/webmin/apache/config.info
%{_datadir}/webmin/apache/defaultacl
%{_datadir}/webmin/apache/images
%webmin_lang %{_datadir}/webmin/apache/lang
%{_datadir}/webmin/apache/module.info
%doc %{_datadir}/webmin/apache/notes
%{_datadir}/webmin/apache/*-*.pl
%{_datadir}/webmin/apache/*_*.pl
%{_datadir}/webmin/apache/autoindex.pl
%{_datadir}/webmin/apache/browsermatch.pl
%{_datadir}/webmin/apache/core.pl
%config(noreplace) %{_sysconfdir}/webmin/apache/config

# AT
%files at
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/at
%dir %{_datadir}/webmin/at
%attr(755,root,root) %{_datadir}/webmin/at/*.cgi
%{_datadir}/webmin/at/config-*
%{_datadir}/webmin/at/config.info
%{_datadir}/webmin/at/images
%webmin_lang %{_datadir}/webmin/at/lang
%{_datadir}/webmin/at/module.info
%{_datadir}/webmin/at/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/at/config    

# BIND 8 #
%files bind8
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/bind8
%dir %{_datadir}/webmin/bind8
%attr(755,root,root) %{_datadir}/webmin/bind8/*.cgi
%{_datadir}/webmin/bind8/config-*
%{_datadir}/webmin/bind8/config.info
%{_datadir}/webmin/bind8/defaultacl
%{_datadir}/webmin/bind8/images
%webmin_lang %{_datadir}/webmin/bind8/lang
%{_datadir}/webmin/bind8/module.info
%{_datadir}/webmin/bind8/*-*.pl
%{_datadir}/webmin/bind8/*_*.pl
%{_datadir}/webmin/bind8/db.cache
%config(noreplace) %{_sysconfdir}/webmin/bind8/config

# CRON
%files cron
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cron
%dir %{_datadir}/webmin/cron
%attr(755,root,root) %{_datadir}/webmin/cron/*.cgi
%{_datadir}/webmin/cron/config-*
%{_datadir}/webmin/cron/config.info
%{_datadir}/webmin/cron/defaultacl
#%{_datadir}/webmin/cron/help
%{_datadir}/webmin/cron/images
%webmin_lang %{_datadir}/webmin/cron/lang
%{_datadir}/webmin/cron/module.info
%{_datadir}/webmin/cron/*-*.pl
%{_datadir}/webmin/cron/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cron/config    

# DHCPD #
%files dhcpd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/dhcpd
%dir %{_datadir}/webmin/dhcpd
%attr(755,root,root) %{_datadir}/webmin/dhcpd/*.cgi
%{_datadir}/webmin/dhcpd/config-*
%{_datadir}/webmin/dhcpd/config.info
%{_datadir}/webmin/dhcpd/defaultacl
%webmin_help %{_datadir}/webmin/dhcpd/help
%{_datadir}/webmin/dhcpd/images
%webmin_lang %{_datadir}/webmin/dhcpd/lang
%{_datadir}/webmin/dhcpd/module.info
%{_datadir}/webmin/dhcpd/*-*.pl
%{_datadir}/webmin/dhcpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/dhcpd/config

# INETD
%files inetd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/inetd
%dir %{_datadir}/webmin/inetd
%attr(755,root,root) %{_datadir}/webmin/inetd/*.cgi
%{_datadir}/webmin/inetd/config-*
%{_datadir}/webmin/inetd/config.info
#%dir %{_datadir}/webmin/inetd/help
%{_datadir}/webmin/inetd/images
%webmin_lang %{_datadir}/webmin/inetd/lang
%{_datadir}/webmin/inetd/module.info
%{_datadir}/webmin/inetd/*-*.pl
%{_datadir}/webmin/inetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/inetd/config

# MAJORDOMO #
%files majordomo
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/majordomo
%dir %{_datadir}/webmin/majordomo
%attr(755,root,root) %{_datadir}/webmin/majordomo/*.cgi
%{_datadir}/webmin/majordomo/config
%{_datadir}/webmin/majordomo/config-*
%{_datadir}/webmin/majordomo/config.info
%{_datadir}/webmin/majordomo/defaultacl
%{_datadir}/webmin/majordomo/images
%webmin_lang %{_datadir}/webmin/majordomo/lang
%{_datadir}/webmin/majordomo/module.info
%{_datadir}/webmin/majordomo/*-*.pl
%{_datadir}/webmin/majordomo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/majordomo/config

# MYSQL #
%files mysql
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mysql
%dir %{_datadir}/webmin/mysql
%attr(755,root,root) %{_datadir}/webmin/mysql/*.cgi
%{_datadir}/webmin/mysql/config
%{_datadir}/webmin/mysql/config-*
%{_datadir}/webmin/mysql/config.info
%{_datadir}/webmin/mysql/defaultacl
%webmin_help %{_datadir}/webmin/mysql/help
%{_datadir}/webmin/mysql/images
%webmin_lang %{_datadir}/webmin/mysql/lang
%{_datadir}/webmin/mysql/module.info
%{_datadir}/webmin/mysql/*-*.pl
%{_datadir}/webmin/mysql/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/mysql/config

# POSTFIX #
%files postfix
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postfix
%dir %{_datadir}/webmin/postfix
%attr(755,root,root) %{_datadir}/webmin/postfix/*.cgi
%{_datadir}/webmin/postfix/config
%{_datadir}/webmin/postfix/config-*
%{_datadir}/webmin/postfix/config.info
%{_datadir}/webmin/postfix/defaultacl
%webmin_help %{_datadir}/webmin/postfix/help
%{_datadir}/webmin/postfix/images
%webmin_lang %{_datadir}/webmin/postfix/lang
%{_datadir}/webmin/postfix/module.info
%{_datadir}/webmin/postfix/*-*.pl
%{_datadir}/webmin/postfix/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/postfix/config

# POSTGRESQL #
%files postgresql
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postgresql
%dir %{_datadir}/webmin/postgresql
%attr(755,root,root) %{_datadir}/webmin/postgresql/*.cgi
%{_datadir}/webmin/postgresql/config
%{_datadir}/webmin/postgresql/config-*
%{_datadir}/webmin/postgresql/config.info
%{_datadir}/webmin/postgresql/defaultacl
%webmin_help %{_datadir}/webmin/postgresql/help
%{_datadir}/webmin/postgresql/images
%webmin_lang %{_datadir}/webmin/postgresql/lang
%{_datadir}/webmin/postgresql/module.info
%{_datadir}/webmin/postgresql/*-*.pl
%{_datadir}/webmin/postgresql/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/postgresql/config

# PAP (PPPD) #
%files ppp
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pap
%dir %{_datadir}/webmin/pap
%attr(755,root,root) %{_datadir}/webmin/pap/*.cgi
%{_datadir}/webmin/pap/config-*
%{_datadir}/webmin/pap/config.info
%{_datadir}/webmin/pap/images
%webmin_lang %{_datadir}/webmin/pap/lang
%{_datadir}/webmin/pap/module.info
%{_datadir}/webmin/pap/*-*.pl
%{_datadir}/webmin/pap/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/pap/config

# SAMBA #
%files samba
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/samba
%dir %{_datadir}/webmin/samba
%attr(755,root,root) %{_datadir}/webmin/samba/*.cgi
%{_datadir}/webmin/samba/config-*
%{_datadir}/webmin/samba/config.info
%{_datadir}/webmin/samba/defaultacl
%webmin_help %{_datadir}/webmin/samba/help
%{_datadir}/webmin/samba/images
%webmin_lang %{_datadir}/webmin/samba/lang
%{_datadir}/webmin/samba/module.info
%{_datadir}/webmin/samba/*-*.pl
%{_datadir}/webmin/samba/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/samba/config

# SENDMAIL #
%files sendmail
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sendmail
%dir %{_datadir}/webmin/sendmail
%attr(755,root,root) %{_datadir}/webmin/sendmail/*.cgi
%{_datadir}/webmin/sendmail/config-*
%{_datadir}/webmin/sendmail/config.info
%{_datadir}/webmin/sendmail/defaultacl
%webmin_help %{_datadir}/webmin/sendmail/help
%{_datadir}/webmin/sendmail/images
%webmin_lang %{_datadir}/webmin/sendmail/lang
#%{_datadir}/webmin/sendmail/list_us
%{_datadir}/webmin/sendmail/module.info
%{_datadir}/webmin/sendmail/*-*.pl
%{_datadir}/webmin/sendmail/*_*.pl
%{_datadir}/webmin/sendmail/filter.pl
%attr(755,root,root) %{_datadir}/webmin/sendmail/autoreply.pl
%config(noreplace) %{_sysconfdir}/webmin/sendmail/config

# SQUID #
%files squid
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/squid
%dir %{_datadir}/webmin/squid
%attr(755,root,root) %{_datadir}/webmin/squid/*.cgi
%{_datadir}/webmin/squid/config-*
%{_datadir}/webmin/squid/config.info
%webmin_help %{_datadir}/webmin/squid/help
%{_datadir}/webmin/squid/images
%webmin_lang %{_datadir}/webmin/squid/lang
%{_datadir}/webmin/squid/module.info
%{_datadir}/webmin/squid/*-*.pl
%{_datadir}/webmin/squid/*_*.pl
%{_datadir}/webmin/squid/*.risk
%{_datadir}/webmin/squid/*.skill
%config(noreplace) %{_sysconfdir}/webmin/squid/config

# WU-FTPD #
%files wuftpd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/wuftpd
%dir %{_datadir}/webmin/wuftpd
%attr(755,root,root) %{_datadir}/webmin/wuftpd/*.cgi
%{_datadir}/webmin/wuftpd/config-*
%{_datadir}/webmin/wuftpd/config.info
%webmin_help %{_datadir}/webmin/wuftpd/help
%{_datadir}/webmin/wuftpd/images
%webmin_lang %{_datadir}/webmin/wuftpd/lang
%{_datadir}/webmin/wuftpd/module.info
%{_datadir}/webmin/wuftpd/*-*.pl
%{_datadir}/webmin/wuftpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/wuftpd/config

# XINETD
%files xinetd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/xinetd
%dir %{_datadir}/webmin/xinetd
%attr(755,root,root) %{_datadir}/webmin/xinetd/*.cgi
%{_datadir}/webmin/xinetd/config
%{_datadir}/webmin/xinetd/config-*
%{_datadir}/webmin/xinetd/config.info
%{_datadir}/webmin/xinetd/images
%webmin_lang %{_datadir}/webmin/xinetd/lang
%{_datadir}/webmin/xinetd/module.info
%{_datadir}/webmin/xinetd/*-*.pl
%{_datadir}/webmin/xinetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/xinetd/config

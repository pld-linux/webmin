%include        /usr/lib/rpm/macros.perl
Summary:	Webmin - web-based administration	
Summary(pl):	Webmin - administracja przez WWW
Name:		webmin
Version:	0.87
Release:	1
License:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.webmin.com/pub/webadmin/%{name}-%{version}.tar.gz
#Unofficial webmin tarballs location (if anybody interested):
#Source0:	ftp://fudu.curlybracket.com/pub/webadmin/tarballs/%{name}-%{version}4.tar.gz
Source1:	%{name}.init
Source2:	%{name}-miniserv.conf
Patch0:		%{name}-PLD.patch
Url:		http://www.webmin.com/webmin/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Webmin is a web-based interface for system administration for Unix.
Using any browser that supports tables and forms, you can setup user
accounts, Apache, internet services, DNS, file sharing and so on.

%package disks-tools
Summary:	Webmin - Partition and disk management tools
Summary(pl):	Webmin - Narzêdzia do zarz±dzania dyskami i partycjami
Group:		Utilities/System
Group(pl):	Narzêdzia/System

%description disks-tools

%description -l pl disks-tools


# DISKS-TOOLS
%package disks-tools-raid
Summary:	Webmin - RAID
Summary(pl):	Webmin - RAID
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	raidtools

%description disks-tools-raid

%description -l pl disks-tools-raid

# LILO
%package lilo
Summary:	Webmin - LILO configuration
Summary(pl):	Webmin - Konfiguracja LILO
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	lilo

%description lilo

%description -l pl lilo

# PRINTER
%package printer
Summary:	Webmin - Printer administration	
Summary(pl):	Webmin - Zarz±dzanie drukark±
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	lpd

%description printer

%description -l pl printer

# NET
%package net
Summary:	Webmin - Network configuration
Summary(pl):	Webmin - Konfiguracja sieci
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Prereq:		rc-scripts

%description net

%description -l pl net

# APACHE
%package apache
Summary:	Webmin - Apache webserver
Summary(pl):	Webmin - Serwer WWW Apache
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	apache

%description apache

%description -l pl apache

# BIND8
%package bind8
Summary:	Webmin - BIND 8 DNS server
Summary(pl):	Webmin - Serwer DNS BIND 8
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	bind

%description bind8

%description -l pl bind8

# DHCPD
%package dhcpd
Summary:	Webmin - DHCP server	
Summary(pl):	Webmin - Serwer DHCP
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	dhcpd

%description dhcpd

%description -l pl dhcpd

# BIND4
%package bind4
Summary:	Webmin - BIND 4 DNS server
Summary(pl):	Webmin - Serwer DNS BIND 4
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	bind4

%description bind4

%description -l pl bind4

# MAJORDOMO
%package majordomo
Summary:	Webmin - Majordomo List Manager
Summary(pl):	Webmin - Zarz±dca list dyskusyjnych Majordomo
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	majordomo

%description majordomo

%description -l pl majordomo

# MYSQL
%package mysql
Summary:	Webmin - MySQL server
Summary(pl):	Webmin - Serwer MySQL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	mysql-client

%description mysql

%description -l pl mysql

# PPP
%package ppp
Summary:	Webmin - PAP (PPP) usernames and passwords
Summary(pl):	Webmin - nazwy u¿ytkowników i has³a dla PAP (PPP)
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	ppp

%description ppp

%description -l pl ppp

# SAMBA
%package samba
Summary:	Webmin - Samba
Summary(pl):	Webmin - Samba
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	samba

%description samba

%description -l pl samba

# SENDMAIL
%package sendmail
Summary:	Webmin - Sendmail	
Summary(pl):	Webmin - Sendmail
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	sendmail

%description sendmail

%description -l pl sendmail

# SQUID
%package squid
Summary:	Webmin - Squid proxy
Summary(pl):	Webmin - Serwer proxy Squid
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	squid

%description squid

%description -l pl squid

# WUFTPD
%package wuftpd
Summary:	Webmin - Wu-Ftpd server
Summary(pl):	Webmin - Serwer Wu-Ftpd
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	wu-ftpd

%description wuftpd

%description -l pl wuftpd

%package cron
Summary:	Webmin - Cron
Summary(pl):	Webmin - Cron
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	crondaemon

%description cron

%description -l pl cron

%package nfs
Summary:	Webmin - NFS server configuration	
Summary(pl):	Webmin - Konfiguracja serwera NFS
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	nfsdaemon

%description nfs

%description -l pl nfs

%package quota
Summary:	Webmin - Quota management
Summary(pl):	Webmin - Zarz±dzanie quota
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	quota

%description quota

%description -l pl quota

%package software
Summary:	Webmin - Software Packages
Summary(pl):	Webmin -
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	rpm

%description software

%description -l pl software

%package syslog
Summary:	Webmin - System logger 	
Summary(pl):	Webmin - Logi systemowe
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	syslogd

%description syslog 

%description -l pl syslog

%package admin-tools
Summary:	Webmin - Admin-tools (telnet, file manager, etc)
Summary(pl):	Webmin - Narzêdzia admin (telnet, menad¿er plików, itp)
Group:		Utilities/System
Group(pl):	Narzêdzia/System

%description admin-tools

%description -l pl admin-tools

%package system
Summary:	Webmin - Process Manager
Summary(pl):	Webmin - Zarz±dzenia procesami
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	webmin-disk-tools = %{version}

%description system

%description -l pl system

%package useradmin
Summary:	Webmin - User account manager
Summary(pl):	Webmin - Obs³uga kont u¿ytkowników
Group:		Utilities/System
Group(pl):	Narzêdzia/System

%description useradmin

%description -l pl useradmin

%prep
%setup -q 
%patch0 -p1
%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/webmin,/var/{log,run}/webmin} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webmin,rc.d/init.d}

cp -rp * $RPM_BUILD_ROOT%{_datadir}/webmin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/webmin
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.conf

(find $RPM_BUILD_ROOT%{_datadir}/webmin -name '*.cgi' -print ; find $RPM_BUILD_ROOT%{_datadir}/webmin -name '*.pl' -print) | perl $RPM_BUILD_ROOT%{_datadir}/webmin/perlpath.pl /usr/bin/perl -

export allmods=`cd $RPM_BUILD_ROOT%{_datadir}/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`

perl $RPM_BUILD_ROOT%{_datadir}/webmin/copyconfig.pl pld-linux 1.0 $RPM_BUILD_ROOT%{_datadir}/webmin $RPM_BUILD_ROOT%{_sysconfdir}/webmin "" $allmods

echo "/usr/bin/perl"		>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/perl-path
echo "/var/log/webmin" 		>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/var-path
echo "real_os_version=1.0"	>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "lang=en" 			>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "find_pid_command=ps auwwwx | grep NAME | grep -v grep | awk '{ print $2 }'"	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "os_type=pld-linux" 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "path=/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin" 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
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

%post disks-tools
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post disks-tools-raid
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post lilo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post printer
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post net
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post apache
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post bind8
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post dhcpd
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post bind4
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post majordomo
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post mysql
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

%post cron
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

%post syslog
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post admin-tools
export allmods=`cd /usr/share/webmin; ls */module.info | sed -e 's/\/module.info//g' | xargs echo`
perl /usr/share/webmin/newmods.pl /etc/webmin $allmods

%post system
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
%{_datadir}/webmin/lang
%{_datadir}/webmin/config-*
%{_datadir}/webmin/*.txt
%{_datadir}/webmin/version

%attr(750,root,root) %dir %{_sysconfdir}/webmin
%config(noreplace) %{_sysconfdir}/webmin/config
%config(noreplace) %{_sysconfdir}/webmin/miniserv.conf
%{_sysconfdir}/webmin/perl-path
%{_sysconfdir}/webmin/var-path
%{_sysconfdir}/webmin/version

# ACL #
%dir %{_sysconfdir}/webmin/acl
%dir %{_datadir}/webmin/acl
%attr(755,root,root) %{_datadir}/webmin/acl/*.cgi
%{_datadir}/webmin/acl/images
%{_datadir}/webmin/acl/lang
%{_datadir}/webmin/acl/module.info
%{_datadir}/webmin/acl/*.pl
%{_sysconfdir}/webmin/acl/config

# HELP #
%dir %{_sysconfdir}/webmin/help
%dir %{_datadir}/webmin/help
%attr(755,root,root) %{_datadir}/webmin/help/*.cgi
%{_datadir}/webmin/help/help
%{_datadir}/webmin/help/images
%{_datadir}/webmin/help/lang
%{_datadir}/webmin/help/module.info
%{_datadir}/webmin/help/*.pl
%{_sysconfdir}/webmin/help/config

# MAN
%dir %{_sysconfdir}/webmin/man
%dir %{_datadir}/webmin/man
%attr(755,root,root) %{_datadir}/webmin/man/*.cgi
%{_datadir}/webmin/man/config*
%{_datadir}/webmin/man/help
%{_datadir}/webmin/man/images
%{_datadir}/webmin/man/lang
%{_datadir}/webmin/man/module.info
%{_datadir}/webmin/man/*.pl
%{_sysconfdir}/webmin/man/config

# SERVERS #
%dir %{_sysconfdir}/webmin/servers
%dir %{_datadir}/webmin/servers
%attr(755,root,root) %{_datadir}/webmin/servers/*.cgi
%{_datadir}/webmin/servers/config*
%{_datadir}/webmin/servers/images
%{_datadir}/webmin/servers/lang
%{_datadir}/webmin/servers/module.info
%{_datadir}/webmin/servers/*.pl
%{_sysconfdir}/webmin/servers/config

# WEBMIN #
%dir %{_sysconfdir}/webmin/webmin
%dir %{_datadir}/webmin/webmin
%attr(755,root,root) %{_datadir}/webmin/webmin/*.cgi
%{_datadir}/webmin/webmin/images
%{_datadir}/webmin/webmin/lang
%{_datadir}/webmin/webmin/module.info
%{_datadir}/webmin/webmin/*.pl
%{_sysconfdir}/webmin/webmin/config

#### HARDWARE ####

# TIME
%dir %{_sysconfdir}/webmin/time
%dir %{_datadir}/webmin/time
%attr(755,root,root) %{_datadir}/webmin/time/*.cgi
%{_datadir}/webmin/time/config*
%{_datadir}/webmin/time/help
%{_datadir}/webmin/time/images
%{_datadir}/webmin/time/lang
%{_datadir}/webmin/time/module.info
%{_datadir}/webmin/time/*.pl


%files admin-tools
# TELNET
%dir %{_sysconfdir}/webmin/telnet
%dir %{_datadir}/webmin/telnet
%attr(755,root,root) %{_datadir}/webmin/telnet/*.cgi
%{_datadir}/webmin/telnet/config*
%{_datadir}/webmin/telnet/images
%{_datadir}/webmin/telnet/lang
%{_datadir}/webmin/telnet/module.info
%{_datadir}/webmin/telnet/*.zip

# FILE
%dir %{_sysconfdir}/webmin/file
%dir %{_datadir}/webmin/file
%attr(755,root,root) %{_datadir}/webmin/file/*.cgi
%{_datadir}/webmin/file/images
%{_datadir}/webmin/file/lang
%{_datadir}/webmin/file/module.info
%{_datadir}/webmin/file/*.pl
%{_datadir}/webmin/file/*.java
%{_datadir}/webmin/file/*.class

# CUSTOM
%dir %{_sysconfdir}/webmin/custom
%dir %{_datadir}/webmin/custom
%attr(755,root,root) %{_datadir}/webmin/custom/*.cgi
%{_datadir}/webmin/custom/help
%{_datadir}/webmin/custom/images
%{_datadir}/webmin/custom/lang
%{_datadir}/webmin/custom/module.info
%{_datadir}/webmin/custom/*.pl

#### DISKS ####
%files disks-tools

# FDISK
%dir %{_sysconfdir}/webmin/fdisk
%dir %{_datadir}/webmin/fdisk
%attr(755,root,root) %{_datadir}/webmin/fdisk/*.cgi
%{_datadir}/webmin/fdisk/config*
%{_datadir}/webmin/fdisk/help
%{_datadir}/webmin/fdisk/images
%{_datadir}/webmin/fdisk/lang
%{_datadir}/webmin/fdisk/module.info
%{_datadir}/webmin/fdisk/*.pl

# FORMAT
%dir %{_sysconfdir}/webmin/format
%dir %{_datadir}/webmin/format
%attr(755,root,root) %{_datadir}/webmin/format/*.cgi
%{_datadir}/webmin/format/config*
%{_datadir}/webmin/format/help
%{_datadir}/webmin/format/images
%{_datadir}/webmin/format/module.info
%{_datadir}/webmin/format/*.pl

# MOUNT
%dir %{_sysconfdir}/webmin/mount
%dir %{_datadir}/webmin/mount
%attr(755,root,root) %{_datadir}/webmin/mount/*.cgi
%{_datadir}/webmin/mount/config*
%{_datadir}/webmin/mount/help
%{_datadir}/webmin/mount/images
%{_datadir}/webmin/mount/lang
%{_datadir}/webmin/mount/module.info
%{_datadir}/webmin/mount/*.pl

# RAID
%files disks-tools-raid
%dir %{_sysconfdir}/webmin/raid
%dir %{_datadir}/webmin/raid
%attr(755,root,root) %{_datadir}/webmin/raid/*.cgi
%{_datadir}/webmin/raid/config*
%{_datadir}/webmin/raid/images
%{_datadir}/webmin/raid/lang
%{_datadir}/webmin/raid/module.info
%{_datadir}/webmin/raid/*.pl

# LILO
%files lilo
%dir %{_sysconfdir}/webmin/lilo
%dir %{_datadir}/webmin/lilo
%attr(755,root,root) %{_datadir}/webmin/lilo/*.cgi
%{_datadir}/webmin/lilo/config*
%{_datadir}/webmin/lilo/images
%{_datadir}/webmin/lilo/lang
%{_datadir}/webmin/lilo/module.info
%{_datadir}/webmin/lilo/*.pl

# LP
%files printer
%dir %{_sysconfdir}/webmin/lpadmin
%dir %{_datadir}/webmin/lpadmin
%attr(755,root,root) %{_datadir}/webmin/lpadmin/*.cgi
%{_datadir}/webmin/lpadmin/config*
%{_datadir}/webmin/lpadmin/images
%{_datadir}/webmin/lpadmin/lang
%{_datadir}/webmin/lpadmin/module.info
%{_datadir}/webmin/lpadmin/*.pl

# NET
%files net
%dir %{_sysconfdir}/webmin/net
%dir %{_datadir}/webmin/net
%attr(755,root,root) %{_datadir}/webmin/net/*.cgi
%{_datadir}/webmin/net/config*
%{_datadir}/webmin/net/images
%{_datadir}/webmin/net/lang
%{_datadir}/webmin/net/module.info
%{_datadir}/webmin/net/*.pl

#### SYSTEM ####
%files system

# INIT
%dir %{_sysconfdir}/webmin/init
%dir %{_datadir}/webmin/init
%attr(755,root,root) %{_datadir}/webmin/init/*.cgi
%{_datadir}/webmin/init/config*
%{_datadir}/webmin/init/help
%{_datadir}/webmin/init/images
%{_datadir}/webmin/init/lang
%{_datadir}/webmin/init/module.info
%{_datadir}/webmin/init/*.pl

# INITTAB
%dir %{_sysconfdir}/webmin/inittab
%dir %{_datadir}/webmin/inittab
%attr(755,root,root) %{_datadir}/webmin/inittab/*.cgi
%{_datadir}/webmin/inittab/config*
%{_datadir}/webmin/inittab/help
%{_datadir}/webmin/inittab/images
%{_datadir}/webmin/inittab/lang
%{_datadir}/webmin/inittab/module.info
%{_datadir}/webmin/inittab/*.pl

# PROC
%dir %{_sysconfdir}/webmin/proc
%dir %{_datadir}/webmin/proc
%attr(755,root,root) %{_datadir}/webmin/proc/*.cgi
%{_datadir}/webmin/proc/config*
%{_datadir}/webmin/proc/help
%{_datadir}/webmin/proc/images
%{_datadir}/webmin/proc/lang
%{_datadir}/webmin/proc/module.info
%{_datadir}/webmin/proc/*.pl

# USERADMIN
%files useradmin
%dir %{_sysconfdir}/webmin/useradmin
%dir %{_datadir}/webmin/useradmin
%attr(755,root,root) %{_datadir}/webmin/useradmin/*.cgi
%{_datadir}/webmin/useradmin/config*
%{_datadir}/webmin/useradmin/help
%{_datadir}/webmin/useradmin/images
%{_datadir}/webmin/useradmin/lang
%{_datadir}/webmin/useradmin/module.info
%{_datadir}/webmin/useradmin/*.pl

# CRON
%files cron
%dir %{_sysconfdir}/webmin/cron
%dir %{_datadir}/webmin/cron
%attr(755,root,root) %{_datadir}/webmin/cron/*.cgi
%{_datadir}/webmin/cron/config*
%{_datadir}/webmin/cron/help
%{_datadir}/webmin/cron/images
%{_datadir}/webmin/cron/lang
%{_datadir}/webmin/cron/module.info
%{_datadir}/webmin/cron/*.pl

# NFS EXPORTS
%files nfs
%dir %{_sysconfdir}/webmin/exports
%dir %{_datadir}/webmin/exports
%attr(755,root,root) %{_datadir}/webmin/exports/*.cgi
%{_datadir}/webmin/exports/config*
%{_datadir}/webmin/exports/help
%{_datadir}/webmin/exports/images
%{_datadir}/webmin/exports/lang
%{_datadir}/webmin/exports/module.info
%{_datadir}/webmin/exports/*.pl

# QUOTA
%files quota
%dir %{_sysconfdir}/webmin/quota
%dir %{_datadir}/webmin/quota
%attr(755,root,root) %{_datadir}/webmin/quota/*.cgi
%{_datadir}/webmin/quota/config*
%{_datadir}/webmin/quota/help
%{_datadir}/webmin/quota/images
%{_datadir}/webmin/quota/lang
%{_datadir}/webmin/quota/module.info
%{_datadir}/webmin/quota/*.pl

# SOFTWARE
%files software
%dir %{_sysconfdir}/webmin/software
%dir %{_datadir}/webmin/software
%attr(755,root,root) %{_datadir}/webmin/software/*.cgi
%{_datadir}/webmin/software/config*
%{_datadir}/webmin/software/help
%{_datadir}/webmin/software/images
%{_datadir}/webmin/software/lang
%{_datadir}/webmin/software/module.info
%{_datadir}/webmin/software/*.pl

# SYSLOG
%files syslog
%dir %{_sysconfdir}/webmin/syslog
%dir %{_datadir}/webmin/syslog
%attr(755,root,root) %{_datadir}/webmin/syslog/*.cgi
%{_datadir}/webmin/syslog/config*
%{_datadir}/webmin/syslog/images
%{_datadir}/webmin/syslog/lang
%{_datadir}/webmin/syslog/module.info
%{_datadir}/webmin/syslog/*.pl

#### SERVERS #####

# APACHE #
%files apache
%dir %{_sysconfdir}/webmin/apache
%dir %{_datadir}/webmin/apache
%attr(755,root,root) %{_datadir}/webmin/apache/*.cgi
%{_datadir}/webmin/apache/config*
%{_datadir}/webmin/apache/defaultacl
%{_datadir}/webmin/apache/images
%{_datadir}/webmin/apache/lang
%{_datadir}/webmin/apache/module.info
%{_datadir}/webmin/apache/notes
%{_datadir}/webmin/apache/*.pl
%{_sysconfdir}/webmin/apache/config

# BIND 8 #
%files bind8
%dir %{_sysconfdir}/webmin/bind8
%dir %{_datadir}/webmin/bind8
%attr(755,root,root) %{_datadir}/webmin/bind8/*.cgi
%{_datadir}/webmin/bind8/config*
%{_datadir}/webmin/bind8/defaultacl
%{_datadir}/webmin/bind8/images
%{_datadir}/webmin/bind8/lang
%{_datadir}/webmin/bind8/module.info
%{_datadir}/webmin/bind8/*.pl
%{_datadir}/webmin/bind8/db.cache
%{_sysconfdir}/webmin/bind8/config

# DHCPD #
%files dhcpd
%dir %{_sysconfdir}/webmin/dhcpd
%dir %{_datadir}/webmin/dhcpd
%attr(755,root,root) %{_datadir}/webmin/dhcpd/*.cgi
%{_datadir}/webmin/dhcpd/config*
%{_datadir}/webmin/dhcpd/images
%{_datadir}/webmin/dhcpd/lang
%{_datadir}/webmin/dhcpd/module.info
%{_datadir}/webmin/dhcpd/*.pl
%{_sysconfdir}/webmin/dhcpd/config

# BIND 4 #
%files bind4
%dir %{_sysconfdir}/webmin/dnsadmin
%dir %{_datadir}/webmin/dnsadmin
%attr(755,root,root) %{_datadir}/webmin/dnsadmin/*.cgi
%{_datadir}/webmin/dnsadmin/config*
%{_datadir}/webmin/dnsadmin/db.cache
%{_datadir}/webmin/dnsadmin/defaultacl
%{_datadir}/webmin/dnsadmin/help
%{_datadir}/webmin/dnsadmin/images
%{_datadir}/webmin/dnsadmin/module.info
%{_datadir}/webmin/dnsadmin/*.pl
%{_sysconfdir}/webmin/dnsadmin/config

# MAJORDOMO #
%files majordomo
%dir %{_sysconfdir}/webmin/majordomo
%dir %{_datadir}/webmin/majordomo
%attr(755,root,root) %{_datadir}/webmin/majordomo/*.cgi
%{_datadir}/webmin/majordomo/config*
%{_datadir}/webmin/majordomo/defaultacl
%{_datadir}/webmin/majordomo/images
%{_datadir}/webmin/majordomo/module.info
%{_datadir}/webmin/majordomo/*.pl
%{_sysconfdir}/webmin/majordomo/config

# MYSQL #
%files mysql
%dir %{_sysconfdir}/webmin/mysql
%dir %{_datadir}/webmin/mysql
%attr(755,root,root) %{_datadir}/webmin/mysql/*.cgi
%{_datadir}/webmin/mysql/config*
%{_datadir}/webmin/mysql/defaultacl
%{_datadir}/webmin/mysql/help
%{_datadir}/webmin/mysql/images
%{_datadir}/webmin/mysql/lang
%{_datadir}/webmin/mysql/module.info
%{_datadir}/webmin/mysql/*.pl
%{_sysconfdir}/webmin/mysql/config

# PAP (PPPD) #
%files ppp
%dir %{_sysconfdir}/webmin/pap
%dir %{_datadir}/webmin/pap
%attr(755,root,root) %{_datadir}/webmin/pap/*.cgi
%{_datadir}/webmin/pap/config*
%{_datadir}/webmin/pap/images
%{_datadir}/webmin/pap/module.info
%{_datadir}/webmin/pap/*.pl
%{_sysconfdir}/webmin/pap/config

# SAMBA #
%files samba
%dir %{_sysconfdir}/webmin/samba
%dir %{_datadir}/webmin/samba
%attr(755,root,root) %{_datadir}/webmin/samba/*.cgi
%{_datadir}/webmin/samba/config*
%{_datadir}/webmin/samba/help
%{_datadir}/webmin/samba/images
%{_datadir}/webmin/samba/module.info
%{_datadir}/webmin/samba/*.pl
%{_sysconfdir}/webmin/samba/config

# SENDMAIL #
%files sendmail
%dir %{_sysconfdir}/webmin/sendmail
%dir %{_datadir}/webmin/sendmail
%attr(755,root,root) %{_datadir}/webmin/sendmail/*.cgi
%{_datadir}/webmin/sendmail/config*
%{_datadir}/webmin/sendmail/defaultacl
%{_datadir}/webmin/sendmail/help
%{_datadir}/webmin/sendmail/images
%{_datadir}/webmin/sendmail/lang
%{_datadir}/webmin/sendmail/list_us
%{_datadir}/webmin/sendmail/module.info
%{_datadir}/webmin/sendmail/*.pl
%{_sysconfdir}/webmin/sendmail/config

# SQUID #
%files squid
%dir %{_sysconfdir}/webmin/squid
%dir %{_datadir}/webmin/squid
%attr(755,root,root) %{_datadir}/webmin/squid/*.cgi
%{_datadir}/webmin/squid/config*
%{_datadir}/webmin/squid/help
%{_datadir}/webmin/squid/images
%{_datadir}/webmin/squid/lang
%{_datadir}/webmin/squid/module.info
%{_datadir}/webmin/squid/*.pl
%{_sysconfdir}/webmin/squid/config

# WU-FTPD #
%files wuftpd
%dir %{_sysconfdir}/webmin/wuftpd
%dir %{_datadir}/webmin/wuftpd
%attr(755,root,root) %{_datadir}/webmin/wuftpd/*.cgi
%{_datadir}/webmin/wuftpd/config*
%{_datadir}/webmin/wuftpd/help
%{_datadir}/webmin/wuftpd/images
%{_datadir}/webmin/wuftpd/lang
%{_datadir}/webmin/wuftpd/module.info
%{_datadir}/webmin/wuftpd/*.pl
%{_sysconfdir}/webmin/wuftpd/config

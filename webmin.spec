%include	/usr/lib/rpm/macros.perl
%define		source_version	%{version}
%define		os_version	%(rpm -qf /etc/pld-release --qf '%%{version}' 2>/dev/null || echo ERROR)
Summary:	Webmin - web-based administration
Summary(pl):	Webmin - administracja przez WWW
Name:		webmin
Version:	1.260
Release:	1.7
License:	BSD-like
Group:		Applications/System
Source0:	http://dl.sourceforge.net/webadmin/%{name}-%{version}.tar.gz
# Source0-md5:	c45fe387902405cb36a1a5c6a240ad0d
# Unofficial webmin tarballs location (if anybody interested):
#Source0:	http://fudu.webmin.com/webmin/tarballs/%{name}-%{source_version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}-miniserv.conf
Source3:	%{name}-find-lang.sh
Patch0:		%{name}-PLD-module.info.patch
Patch1:		%{name}-ad-pld-config.patch
Patch2:		%{name}-software-poldek.patch
Patch3:		%{name}-quote.patch
URL:		http://www.webmin.com/
BuildRequires:	perl-CGI
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-DBI
BuildRequires:	perl-Mon
BuildRequires:	perl-Net-SSLeay
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	/etc/pld-release
BuildRequires:	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires:	perl-modules
Requires:	policy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-system = %{version}-%{release}
Requires:	fdisk
Requires:	hdparm

%description disk-tools
Webmin - Partition and disk management tools.

%description disk-tools -l pl
Webmin - narzêdzia do zarz±dzania dyskami i partycjami.

# APACHE
%package apache
Summary:	Webmin - Apache webserver
Summary(pl):	Webmin - Serwer WWW Apache
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	webserver = apache

%description apache
Webmin - Configure almost all Apache directives and features.

%description apache -l pl
Webmin - konfigurowanie prawie wszystkich ustawieñ Apache.

# AT
%package at
Summary:	Webmin - At
Summary(pl):	Webmin - At
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	at

%description at
Webmin - At.

%description at -l pl
Webmin - At.

# ppp-client
%package ppp-client
Summary:	Webmin - Configure modem connection
Summary(pl):	Webmin - konfiguracja po³±czenia przez modem
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	ppp

%description ppp-client
Webmin - Configure the WV-Dial package to connect to the Internet with
a modem PPP connection.

%description ppp-client -l pl
Webmin - konfiguracja pakietu WV-Dial do ³±czenia z Internetem po PPP
przez modem.

# pptp-client
%package  pptp-client
Summary:	Webmin - pptp-client
Summary(pl):	Webmin - klient PPTP
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description pptp-client
Webmin - Configure and establish connections to a VPN server using the
PPTP protocol.

%description pptp-client -l pl
Webmin - konfiguracja i zestawianie po³±czenia do serwera VPN poprzez
protokó³ PPTP.

# pptp-server
%package pptp-server
Summary:	Webmin - pptp-server
Summary(pl):	Webmin - serwer PPTP
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	pptpd

%description pptp-server
Webmin - Set up your system as a PPTP server so that Linux or Windows
VPN clients can connect.

%description pptp-server -l pl
Webmin - ustawienie systemu jako serwera PPTP, z którym mog± siê
³±czyæ linuksowi i windowsowi klienci VPN.

# ipsec
%package ipsec
Summary:	Webmin - IPsec VPN Configuration
Summary(pl):	Webmin - konfigurator IPsec VPN
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	ipsec-tools

%description ipsec
Webmin - Set up a client or server for an IPsec VPN using FreeSWAN.

%description ipsec -l pl
Webmin - ustawianie klienta lub serwera IPsec VPN u¿ywaj±c FreeSWAN.

# firewall
%package firewall
Summary:	Webmin - Linux firewall
Summary(pl):	Webmin - zapora ogniowa dla Linuksa
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	iptables

%description firewall
Webmin - Configure a Linux firewall using iptables. Allows the editing
of all tables, chains, rules and options.

%description firewall -l pl
Webmin - konfiguracja zapory dla Linuksa z iptables. Pozwala na
modyfikowanie tablic, ³añcuchów i regu³ filtrowania.

# idmapd
%package idmapd
Summary:	Webmin - Managing the NFS ID mapping daemon
Summary(pl):	Webmin - administracja demonem NFS ID
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description idmapd
Webmin - Managing the NFS ID mapping daemon.

%description idmapd -l pl
Webmin - administracja demonem NFS ID.

# BIND 8/9
%package bind8
Summary:	Webmin - BIND DNS server
Summary(pl):	Webmin - serwer DNS BIND
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	bind

%description bind8
Webmin - Create and edit domains, DNS records, BIND options and views.

%description bind8 -l pl
Webmin - tworzenie i modyfikowanie domen, rekordów DNS, opcji BIND-a i
widoków.

# DNSADMIN
%package dnsadmin
Summary:	Webmin - BIND 4 DNS admin
Summary(pl):	Webmin - administracja serverem DNS BIND
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
#Requires:	bind

%description dnsadmin
Webmin - Create and edit domains and DNS records.

%description dnsadmin -l pl
Webmin - Tworzenie i modyfikowanie domen i rekordów DNS.

# BURNER
%package burner
Summary:	Webmin - CD Burner
Summary(pl):	Webmin - Wypalanie p³yt CD
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	cdrecord
Requires:	fdisk
Requires:	mkisofs
Requires:	mpg123
Requires:	proc

%description burner
Webmin - Burn data CDs from ISO images or selected directories.

%description burner -l pl
Webmin - wypalanie p³yt CD z danymi z obrazów ISO lub wybranych
katalogów.

# SMART-STATUS
%package smart-status
Summary:	Webmin - Status of IDE hard drives
Summary(pl):	Webmin - stan twardych dysków
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	smartmontools

%description smart-status
Webmin - Check the status of IDE drives to detect problems and
potential failures..

%description smart-status -l pl
Webmin - sprawdzenie stanu dysków IDE w celu wykrycia problemów i
potencjalnych uszkodzeñ.

# CFENGINE
%package cfengine
Summary:	Webmin - Configuration Engine
Summary(pl):	Webmin - cfengine
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	cfengine

%description cfengine
Webmin - Configure the CFengine program, for checking and maintaining
various system-administration settings.

%description cfengine -l pl
Webmin - konfiguracja programu CFengine do sprawdzania i utrzymywania
ró¿nych ustawieñ administracyjnych.

# CLUSTER-SOFTWARE
%package cluster-software
Summary:	Webmin - Cluster software packages
Summary(pl):	Webmin - Pakiety oprogramowania
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description cluster-software
Webmin - Install RPMs, debian and solaris packages across multiple
servers from one source.

%description cluster-software -l pl
Webmin - instalacja RPM-ów, deb-ów oraz pakietów dla Solarisa na wielu
serwerach z jednego ¼ród³a.

# CLUSTER-SHELL
%package cluster-shell
Summary:	Webmin - Cluster shell
Summary(pl):	Webmin - pow³oka dla klastra
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description cluster-shell
Webmin - Run commands on multiple servers at once.

%description cluster-shell -l pl
Webmin - uruchamianie poleceñ jednocze¶nie na wielu serwerach.

# CLUSTER-USERADMIN
%package cluster-useradmin
Summary:	Webmin - Cluster users and groups
Summary(pl):	Webmin - u¿ytkownicy i grupy klastra
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description cluster-useradmin
Webmin - Create, update and delete users and groups across multiple
servers. Unlike NIS, each server has its own passwd and group files
which are remotely updated by this module.

%description cluster-useradmin -l pl
Webmin - tworzenie, aktualizacja i usuwanie u¿ytkowników i grup na
wielu serwerach. W odró¿nieniu od NIS, ka¿dy serwer ma w³asne has³o i
pliki grup które s± zdalnie aktualizowane przez ten modu³.

# CLUSTER-USERMIN
%package cluster-usermin
Summary:	Webmin - Cluster usermin
Summary(pl):	Webmin - klastrowy usermin
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description cluster-usermin
Webmin - Install and manage modules and themes across multiple Usermin
servers.

%description cluster-usermin -l pl
Webmin - instalowanie i administrowanie modu³ami i motywami na wielu
serwerach Usermin.

# CLUSTER-COPY
%package cluster-copy
Summary:	Webmin - Cluster copy file
Summary(pl):	Webmin - klastrowe kopiowanie plików
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	cron

%description cluster-copy
Webmin - Schedule the transfer of files from this server to multiple
servers in a Webmin cluster.

%description cluster-copy -l pl
Webmin - szeregowanie przesy³ania plików z tego serwera na wiele
serwerów w klastrze Webmina.

# CLUSTER-CRON
%package cluster-cron
Summary:	Webmin - Cluster cron
Summary(pl):	Webmin - klastrowy cron
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	cron

%description cluster-cron
Webmin - Create scheduled Cron jobs that run on multiple servers
simultaneously.

%description cluster-cron -l pl
Webmin - tworzeie zadañ crona uruchamianych jednocze¶nie na wielu
serwerach.

# CLUSTER-PASSWORD
%package cluster-passwd
Summary:	Webmin - Cluster passwd
Summary(pl):	Webmin - klastrowe passwd
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-cluster-useradmin = %{version}-%{release}
Requires:	passwd
Requires:	useradmin

%description cluster-passwd
Webmin - Change passwords on multiple systems in a Webmin cluster at
once.

%description cluster-passwd -l pl
Webmin - jednoczesna zmiana hase³ na serwerach w klastrze Webmina.

# LDAP-USERADMIN
%package ldap-useradmin
Summary:	Webmin - Manage users and groups stored in an LDAP database
Summary(pl):	Webmin - administracja u¿ytkownikami i grupami w bazie LDAP
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description ldap-useradmin
Webmin - Manage users and groups stored in an LDAP database, used for
Unix, Samba and Cyrus IMAP authentication.

%description ldap-useradmin -l pl
Webmin - administracja u¿ytkownikami i grupami w bazie LDAP, u¿ywanej
dla Uniksa, Samby i uwierzytelnienia Cyrus IMAP.

# CLUSTER-WEBMIN
%package cluster-webmin
Summary:	Webmin - Cluster Webmin servers
Summary(pl):	Webmin - klaster serwerów Webmina
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-servers = %{version}-%{release}

%description cluster-webmin
Webmin - Install and manage modules, themes, users, groups and access
control settings across multiple Webmin servers.

%description cluster-webmin -l pl
Webmin - instalacja i zarz±dzanie modu³ami, motywami, u¿ytkownikami,
grupami i dostêpem do ustawieñ na wielu serwerach Webmina.

# CRON
%package cron
Summary:	Webmin - Cron
Summary(pl):	Webmin - Cron
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description cron
Webmin - Create, edit and delete Cron jobs.

%description cron -l pl
Webmin - tworzenie, modyfikowanie i usuwanie zadañ crona.

%package vgetty
Summary:	Webmin - Vgetty
Summary(pl):	Webmin - Vgetty
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description vgetty
Webmin - Set up your system as an answering machine using vgetty.

%description vgetty -l pl
Webmin - ustawianie systemu do odpowiadania na po³±czenia przy u¿yciu
vgetty.

# DHCPD
%package dhcpd
Summary:	Webmin - DHCP server
Summary(pl):	Webmin - serwer DHCP
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	dhcp

%description dhcpd
Webmin - Manage shared networks, subnets, hosts and groups for ISC
DHCPD.

%description dhcpd -l pl
Webmin - zarz±dzanie sieciami, podsieciami, hostami i grupami dla ISC
DHCPD.

# adsl-client
%package adsl-client
Summary:	Webmin - adsl-client
Summary(pl):	Webmin - klient ADSL
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description adsl-client
Webmin - Set up a PPP client with the RP-PPPoE package.

%description adsl-client -l pl
Webmin - ustawienia klienta PPP z pakietem RP-PPPoE.

# FETCHMAIL
%package fetchmail
Summary:	Webmin - Fetchmail
Summary(pl):	Webmin - Fetchmail
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	fetchmail

%description fetchmail
Webmin - Configure the popular fetchmail program for automatically
retrieving mail from other servers.

%description fetchmail -l pl
Webmin - konfiguracja popularnego programu do automatycznego ¶ci±gania
poczty z innych serwerów.

# DOVECOT
%package dovecot
Summary:	Webmin - dovecot
Summary(pl):	Webmin - dovecot
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	dovecot

%description dovecot
Webmin - onfigure the Dovecot IMAP and POP3 mail retrieval server.

%description dovecot -l pl
Webmin - konfiguracja serwera IMAP i POP3 dovecot.

# MAILBOXES
%package mailboxes
Summary:	Webmin - mailboxes
Summary(pl):	Webmin - mailboxes
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mailboxes
Webmin - Read email in users' mailboxes.

%description mailboxes -l pl
Webmin - czytanie poczty ze skrzynek u¿ytkowników.

# WEBALIZER
%package webalizer
Summary:	Webmin - Webalizer Configuration
Summary(pl):	Webmin - konfiguracja Webalizera
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	webalizer

%description webalizer
Webmin - Generate reports from webserver, proxy server and FTP log
files.

%description webalizer -l pl
Webmin - generowanie raportów z serwera WWW, serwera proxy i plików
logów FTP.

# UPDOWN
%package updown
Summary:	Webmin - Upload and Download
Summary(pl):	Webmin - Upload i Download
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description updown
Webmin - Upload multiple files to the server, and download multiple
URLs either immediately or in the background at a scheduled time.

%description updown -l pl
Webmin - przesy³anie wielu plików na serwer i ¶ci±ganie z wielu
adresów natychmiast lub w tle we wcze¶niej zaprogramowanym czasie.

# DUMP
%package fsdump
Summary:	Webmin - Filesystem backup
Summary(pl):	Webmin - archiwizacja systemu plików
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	dump
Requires:	rc-scripts

%description fsdump
Webmin - Filesystem backup.

%description fsdump -l pl
Webmin - archiwizacja systemu plików.

# backup-config
%package backup-config
Summary:	Webmin - Filesystem backup
Summary(pl):	Webmin - archiwizacja systemu plików
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description backup-config
Webmin - Perform manual or scheduled backups and restores of
configuration files managed by Webmin modules.

%description backup-config -l pl
Webmin - wykonywanie rêcznej lub zaplanowanej archiwizacji oraz
odzyskania danych poprzez modu³ Webmina.

# GRUB
%package grub
Summary:	Webmin - GRUB configuration
Summary(pl):	Webmin - konfiguracja GRUB-a
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	grub

%description grub
Webmin - Configure the Linux GRUB boot loader to allow the selection
of various operating systems and kernels at boot time.

%description grub -l pl
Webmin - konfiguracja linuksowego boot loadera GRUB, aby umo¿liwia³
wybór ró¿nych systemów operacyjnych i j±der w czasie startu.

# HEARTBEAT
%package heartbeat
Summary:	Webmin - Heartbeat Monitor
Summary(pl):	Webmin - monitor Heartbeat
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	heartbeat

%description heartbeat
Webmin - Configure the Heartbeat package for automatic server failover
in a cluster.

%description heartbeat -l pl
Webmin - konfiguracja pakietu Heartbeat do automatycznego przejmowania
roli innego serwera w klastrze.

# INETD
%package inetd
Summary:	Webmin - Inetd
Summary(pl):	Webmin - Inetd
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	inetd

%description inetd
Webmin - Edit services in /etc/inetd.conf, /etc/services and /etc/rpc.

%description inetd -l pl
Webmin - modyfikowanie us³ug w /etc/inetd.conf, /etc/services i
/etc/rpc.

# JABBER
%package jabber
Summary:	Jabber IM server
Summary(pl):	Konfiguracja serwera Jabber
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	jabberd

%description jabber
Webmin - Configure the multi-protocol Jabber messaging server.

%description jabber -l pl
Webmin - konfiguracja serwera systemu powiadamiania Jabber.

# KRB5
%package krb5
Summary:	Kerberos 5 client settings
Summary(pl):	Konfiguracja klienta Kerberos 5
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	krb5

%description krb5
Webmin - Kerberos 5 client settings.

%description krb5 -l pl
Webmin - konfiguracja klienta Kerberos 5.

# LILO
%package lilo
Summary:	Webmin - LILO configuration
Summary(pl):	Webmin - konfiguracja LILO
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	lilo

%description lilo
Webmin - Configure the LILO bootloader.

%description lilo -l pl
Webmin - konfiguracja bootloadera LILO.

# LVM
%package lvm
Summary:	Webmin - Logical Volume Management
Summary(pl):	Webmin - zarz±dzanie wolumenami logicznymi (LVM)
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	lvm2

%description lvm
Webmin - Configure volume groups, physical volumes and logical volumes
for Linux LVM.

%description lvm -l pl
Webmin - zarz±dzanie grupami wolumenów, wolumenami fizycznymi i
wolumenami logicznymi linuksowego systemu LVM.

# MAJORDOMO
%package majordomo
Summary:	Webmin - Majordomo List Manager
Summary(pl):	Webmin - zarz±dca list dyskusyjnych Majordomo
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-sendmail = %{version}-%{release}
#Requires:	majordomo

%description majordomo
Webmin - Create and configure mailing lists for Majordomo.

%description majordomo -l pl
Webmin - tworzenie i konfiguracja list pocztowych Majordomo.

# MON
%package mon
Summary:	Webmin - MON resource monitoring system
Summary(pl):	Webmin - system monitorowania zasobów MON
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	mon
Requires:	rc-scripts

%description mon
Webmin - Setup MON, a powerful service monitor and alerting system.

%description mon -l pl
Webmin - ustawianie MON - potê¿nego systemu monitorowania i
alarmowania.

# MYSQL
%package mysql
Summary:	Webmin - MySQL server
Summary(pl):	Webmin - serwer MySQL
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	mysql

%description mysql
Webmin - Setup databases, tables and permissions in your MySQL
database server.

%description mysql -l pl
Webmin - ustawianie baz danych, tabel i uprawnieñ w serwerze baz
danych MySQL.

# NET
%package net
Summary:	Webmin - Network configuration
Summary(pl):	Webmin - konfiguracja sieci
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description net
Webmin - Configure boot time and active interfaces, DNS, routing and
/etc/hosts.

%description net -l pl
Webmin - konfiguracja interfejsów startowych i aktywnych, DNS-u,
routingu i pliku /etc/hosts.

# bandwidth
%package bandwidth
Summary:	Webmin - Network monitor
Summary(pl):	Webmin - monitor sieci
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description bandwidth
Webmin - View reports on bandwidth usage by host, port, protocol and
time on a Linux system.

%description bandwidth -l pl
Webmin - przegl±danie raportów wykorzystania pasma w zale¿no¶ci od
hosta, portu, protoko³u i czasu.

# SHOREWALL
%package shorewall
Summary:	Webmin - Shorewall configuration
Summary(pl):	Webmin - konfiguracja shorewall
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	shorewall

%description shorewall
Webmin - Lets you edit the most useful tables of the simple Shoreline
Firewall.

%description shorewall -l pl
Webmin - modyfikowanie najbardziej u¿ytecznych tabel prostego
firewalla Shoreline.

# POSTFIX
%package postfix
Summary:	Webmin - Postfix
Summary(pl):	Webmin - Postfix
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	postfix

%description postfix
Webmin - Configure the Postfix mail server.

%description postfix -l pl
Webmin - konfiguracja serwera poczty Postfix.

# POSTGRESQL
%package postgresql
Summary:	Webmin - PostgreSQL server
Summary(pl):	Webmin - serwer PostgreSQL
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-clients

%description postgresql
Webmin - Manage databases, tables and users in your PostgreSQL
database server.

%description postgresql -l pl
Webmin - administracja bazami danych, tabelami i u¿ytkownikami w
serwerze baz danych PostgreSQL.

# PPP
%package ppp
Summary:	Webmin - PAP (PPP) usernames and passwords
Summary(pl):	Webmin - Nazwy u¿ytkowników i has³a dla PAP (PPP)
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	ppp

%description ppp
Webmin - PAP (PPP) usernames and passwords.

%description ppp -l pl
Webmin - nazwy u¿ytkowników i has³a dla PAP (PPP).

# PROCMAIL
%package procmail
Summary:	Webmin - Procmail mail filter
Summary(pl):	Webmin - filtr poczty Procmail
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	procmail

%description procmail
Webmin - Global configuration for Procmail mail filter.

%description procmail -l pl
Webmin - ogólnosystemowa konfiguracja filtra poczty Procmail.

# SPAM
%package spam
Summary:	Webmin - SpamAssassin Mail Filter Configuration
Summary(pl):	Webmin - konfiguracja filtra poczty SpamAssassin
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	spamassassin

%description spam
Webmin - SpamAssassin Mail Filter Configuration.

%description spam -l pl
Webmin - konfiguracja filtra poczty SpamAssassin.

# PRINTER
%package printer
Summary:	Webmin - Printer administration
Summary(pl):	Webmin - zarz±dzanie drukarkami
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description printer
Webmin - Create and edit local and remote printers. Supports Windows
print servers and Ghostscript print drivers.

%description printer -l pl
Webmin - zarz±dzanie lokalnymi i zdalnymi drukarkami. Obs³uguje
serwery wydruków Windows i sterowniki Ghostscript.

# PROFTPD
%package proftpd
Summary:	Webmin - Proftpd FTP Server
Summary(pl):	Webmin - serwer FTP Proftpd
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	proftpd

%description proftpd
Webmin - Configure the powerful ProFTPD FTP server. Supports all
options in most of the standard modules.

%description proftpd -l pl
Webmin - konfiguracja serwera ProFTPD. Obs³uguje wszystkie opcje w
wiêkszo¶ci standardowych modu³ów.

# CVS-PSERVER
%package cvs-pserver
Summary:	Webmin - CVS pserver
Summary(pl):	Webmin - serwer CVS pserver
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	cvs-pserver

%description cvs-pserver
Webmin - Setup a remotely-accessible CVS server, manage users and
browse the repository.

%description cvs-pserver -l pl
Webmin - konfiguracja zdalnego dostêpu do serwera CVS, zarz±dzanie
u¿ytkownikami i przegl±danie repozytoriów.

# SAMBA
%package samba
Summary:	Webmin - Samba configuration
Summary(pl):	Webmin - konfiguracja samby
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	samba

%description samba
Webmin - Create and edit samba file and print shares.

%description samba -l pl
Webmin - tworzenie i modyfikowanie wspó³dzielenia plików i drukarek.

# openslp
%package openslp
Summary:	Webmin - OpenSLP Service Location Protocol
Summary(pl):	Webmin - protoko³u OpenSLP Service Location Protocol
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	openslp

%description openslp
Webmin - Configure OpenSLP Service Location Protocol.

%description openslp -l pl
Webmin - konfiguracja protoko³u OpenSLP Service Location Protocol.

# SENTRY
%package sentry
Summary:	Webmin - Sentries
Summary(pl):	Webmin - wykrywanie prób nieautoryzowanego dostêpu
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	hostsentry
Requires:	logcheck
Requires:	portsentry

%description sentry
Webmin - Configure the portsentry, hostsentry and logcheck system
security monitoring programs.

%description sentry -l pl
Webmin - konfigurowanie programów monitoruj±cych bezpieczeñstwo
systemu portsentry, hostsentry i logcheck.

# QMAIL
%package qmail
Summary:	Webmin - Qmail configuration
Summary(pl):	Webmin - konfiguracja qmaila
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	qmail

%description qmail
Webmin - Configure the QMail mail server, a simpler alternative to
Sendmail.

%description qmail -l pl
Webmin - konfiguracja qmaila - prostszej alternatywy dla Sendmaila.

# SENDMAIL
%package sendmail
Summary:	Webmin - Sendmail configuration
Summary(pl):	Webmin - konfiguracja sendmaila
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	sendmail

%description sendmail
Webmin - Manage sendmail aliases, masquerading, address rewriting and
other features.

%description sendmail -l pl
Webmin - zarz±dzanie aliasami sendmaila, maskowaniem i przepisywaniem
adresów oraz innymi opcjami.

# SQUID
%package squid
Summary:	Webmin - Squid proxy
Summary(pl):	Webmin - serwer proxy Squid
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	squid

%description squid
Webmin - Configure Squid options, ACLs, caching parameters and proxy
users.

%description squid -l pl
Webmin - konfiguracja opcji, ACL-i, parametrów buforowania i
u¿ytkowników dla serwera proxy Squid.

# frox
%package frox
Summary:	Webmin - Frox FTP proxy server
Summary(pl):	Webmin - serwer FTP proxy Frox
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	frox

%description frox
Webmin - Configure Frox, a transparent proxy for FTP clients.

%description frox -l pl
Webmin - konfiguracja Froksa - przezroczystego proxy dla klientów FTP.

# sarg
%package sarg
Summary:	Webmin - Sarg Squid log report generation tool
Summary(pl):	Webmin - narzêdzie do generowania raportów z logów Squida Sarg
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	sarg

%description sarg
Webmin - Configure and schedule SARG, a tool for generating reports
from Squid access logs.

%description sarg -l pl
Webmin - konfiguracja SARG-a - narzêdzia do generowania raportów z
logów Squida.

# SSHD
%package sshd
Summary:	Webmin - SSH Server
Summary(pl):	Webmin - serwer SSH
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	openssh-clients
Requires:	openssh-server

%description sshd
Webmin - Setup the SSH server for remote secure logins.

%description sshd -l pl
Webmin - ustawianie serwera SSH dla bezpiecznego zdalnego logowania.

# WUFTPD
%package wuftpd
Summary:	Webmin - Wu-Ftpd server
Summary(pl):	Webmin - serwer Wu-Ftpd
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	wu-ftpd

%description wuftpd
Webmin - Configure the access control, anonymous FTP and other options
of WU-FTPd.

%description wuftpd -l pl
Webmin - konfiguracja dostêpu, anonimowego FTP i innych opcji serwera
Wu-FTPd.

# XINETD
%package xinetd
Summary:	Webmin - Xinetd
Summary(pl):	Webmin - Xinetd
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	xinetd

%description xinetd
Webmin - Edit servers handled by Xinetd, a replacement for inetd.

%description xinetd -l pl
Webmin - modyfikowanie serwerów obs³ugiwanych przez Xinetd -
zamiennika inetd.

# NFS EXPORTS
%package nfs
Summary:	Webmin - NFS server configuration
Summary(pl):	Webmin - konfiguracja serwera NFS
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	nfs-utils

%description nfs
Webmin - NFS server configuration.

%description nfs -l pl
Webmin - konfiguracja serwera NFS.

# QUOTA
%package quota
Summary:	Webmin - Quota management
Summary(pl):	Webmin - zarz±dzanie systemem quota
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	quota

%description quota
Webmin - Setup and edit user or group disk quotas for local
filesystems.

%description quota -l pl
Webmin - ustawianie i modyfikowanie limitów dyskowych (quot)
u¿ytkowników i grup dla lokalnych systemów plików.

# SOFTWARE
%package software
Summary:	Webmin - Software packages
Summary(pl):	Webmin - pakiety oprogramowania
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	rpm

%description software
Webmin - Manage software packages on your system, and install new
packages.

%description software -l pl
Webmin - zarz±dzanie pakietami oprogramowania w systemie i instalacja
nowych pakietów.

# CPAN
%package cpan
Summary:	Webmin - Cpan
Summary(pl):	Webmin - Cpan
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	rpm

%description cpan
Webmin - Install new Perl modules on your system, and view those
already installed.

%description cpan -l pl
Webmin - instalacja nowych, oraz przegl±danie ju¿ zainstalowanych
modu³ów Perla.

# STUNNEL
%package stunnel
Summary:	Webmin - SSL tunnels configuration
Summary(pl):	Webmin - konfiguracja tuneli SSL
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	stunnel

%description stunnel
Webmin - SSL tunnels configuration.

%description stunnel -l pl
Webmin - konfiguracja tuneli SSL.

# TUNNEL
%package tunnel
Summary:	Webmin - HTTP tunnels configuration
Summary(pl):	Webmin - konfiguracja tuneli HTTP
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description tunnel
Webmin - HTTP tunnels configuration.

%description tunnel -l pl
Webmin - konfiguracja tuneli HTTP.

# STATUS
%package monitor
Summary:	Webmin - Event monitor
Summary(pl):	Webmin - monitor zdarzeñ
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description monitor
Webmin - View the status of services on your system and on remote
systems.

%description monitor -l pl
Webmin - sprawdzenie stanu lokalnych us³ug systemu i zdalnych
serwerów.

# SYSLOG
%package syslog
Summary:	Webmin - System logger
Summary(pl):	Webmin - logi systemowe
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	syslog

%description syslog
Webmin - Configure the syslog server on your system and view its log
files.

%description syslog -l pl
Webmin - konfiguracja serwera syslog w systemie i przegl±danie plików
logów.

# LOGROTATE
%package logrotate
Summary:	Webmin - Log File Editor
Summary(pl):	Webmin - edytor logów systemowych
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	logrotate

%description logrotate
Webmin - Set up the automatic rotation of Apache, Squid, Syslog and
other log files.

%description logrotate -l pl
Webmin - automatyczna rotacja plików logów Apache'a, Squida, Sysloga i
innych.

%package admin-tools
Summary:	Webmin - Admin-tools (telnet, file manager, etc)
Summary(pl):	Webmin - narzêdzia administracyjne (telnet, zarz±dzanie plikami, itp.)
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description admin-tools
Webmin - Admin-tools (telnet, file manager, etc).

%description admin-tools -l pl
Webmin - Narzêdzia administracyjne (telnet, zarz±dzanie plikami,
itp.).

# PROC, INIT, INITTAB, MOUNT
%package system
Summary:	Webmin - System Configuration
Summary(pl):	Webmin - konfiguracja systemu
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description system
Webmin - System Configuration.

%description system -l pl
Webmin - konfiguracja systemu.

# NIS
%package nis
Summary:	Webmin - NIS configuration
Summary(pl):	Webmin - konfiguracja NIS
Group:		Applications/System
Requires(post):	%{name} = %{version}
Requires:	%{name}-inetd = %{version}-%{release}
Requires:	%{name}-useradmin = %{version}-%{release}

%description nis
Webmin - Setup a system as an NIS client, master or slave server. Note
that NIS+ is not supported.

%description nis -l pl
Webmin - konfiguracja systemu jako klienta, g³ównego lub zapasowego
serwera NIS. Uwaga: NIS+ nie jest obs³ugiwany.

# PASSWD
%package passwd
Summary:	Webmin - Change Passwords
Summary(pl):	Webmin - zmiana hase³
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-useradmin = %{version}-%{release}

%description passwd
Webmin - Change Passwords.

%description passwd -l pl
Webmin - zmiana hase³.

# htaccess-htpasswd
%package htaccess-htpasswd
Summary:	Webmin - Protected Web Directories
Summary(pl):	Webmin - ochrona katalogów WWW
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-useradmin = %{version}-%{release}

%description htaccess-htpasswd
Webmin - Create .htaccess and htpasswd files to protect web-acessible
directories.

%description htaccess-htpasswd -l pl
Webmin - tworzenie plików .htaccess i htpasswd do ochrony katalogów
dostêpnych przez WWW.

# USERADMIN
%package useradmin
Summary:	Webmin - User account manager
Summary(pl):	Webmin - zarz±dzanie kontami u¿ytkowników
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description useradmin
Webmin - User account manager.

%description useradmin -l pl
Webmin - zarz±dzanie kontami u¿ytkowników.

# change-user
%package change-user
Summary:	Webmin - Change Language and Theme
Summary(pl):	Webmin - zmiana jêzyka i wygl±du
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	acl

%description change-user
Webmin - Change Language and Theme.

%description change-user -l pl
Webmin - zmiana jêzyka i wygl±du.

# no usermin in PLD yet # USERMIN
%package usermin
Summary:	Webmin - Usermin configuration
Summary(pl):	Webmin - konfiguracja Usermina
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description usermin
Webmin - Usermin configuration.

%description usermin -l pl
Webmin - konfiguracja usermina.

# THEMES
%package themes
Summary:	Webmin - Extra Themes for Webmin
Summary(pl):	Webmin - dodatkowe motywy Webmina
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description themes
Webmin - Extra Themes for Webmin.

%description themes -l pl
Webmin - dodatkowe motywy Webmina.

# SOURCES
%package src
Summary:	Webmin - Java sources
Summary(pl):	Webmin - ¼ród³a w Javie
Group:		Applications/System
Requires(post):	%{name} = %{version}-%{release}
Requires:	%{name}-admin-tools = %{version}-%{release}

%description src
Webmin - Java sources of the `file' module.

%description src -l pl
Webmin - ¼ród³a modu³u "file" napisanego czê¶ciowo w Javie.

%prep
%setup -q -n %{name}-%{source_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# only for solaris, so rm
rm -rf zones	# Create and manage Solaris 10 zones.
rm -rf rbac 	# Manage RBAC user attributes, profiles and authorizations.
rm -rf smf  	# Edit services under control of Service Manangement Facility SMF(1).
rm -rf acl/Authen-SolarisRBAC-0.1
rm -rf acl/Authen-SolarisRBAC-0.1.tar.gz
rm -rf dfsadmin # Edit file shares as defined in the %{_sysconfdir}/dfs/dfstab file.
rm -rf ipfilter	# Configure a firewall using the IPFilter package, by creating and editing rules.
rm -rf format 	# Create and edit paritions on local disks on Solaris.
# only for BSD, so rm
rm -rf ipfw    	# Configure a BSD firewall using IPFW, by creating and editing rules.
rm -rf bsdexports # Edit file shares from the FreeBSD %{_sysconfdir}/exports file.
# only for other unix/linux distributions
rm -rf sgiexports # Edit file shares as defined in the Irix %{_sysconfdir}/exports file.
rm -rf hpuxexports # Edit file shares as defined in the HPUX %{_sysconfdir}/exports file.

rm -f */*aix */*cobalt* */*caldera* */*coherent* */*corel* */*debian* */*freebs* */*generic* */*gentoo* */*hpux */*iri* */*lfs*  \
    */*msc* */*netbsd */*osf1 */*redhat* */*slackware* */*sol* */*suse* */*trustix* */*turbo* */*united* \
    */*unixware */*windows */*maco* */*mandrake* */*openbs* */*openserv* */*open-lin* */config-\*-linux

rm -f *caldera-init *aix *cobalt* *coherent* *corel* *debian* *freebsd *generic* *gentoo* *hpux *iri* *lfs*  \
    *-msc-* *netbsd  *osf1 *redhat* *slackware* *solari* *sol* *suse* *trustix* *turbo* *united* \
    *unixware *windows *maco* *mandrake* *openbs* *openserv* *open-lin*

(find -name '*.cgi' -print ; find -name '*.pl' -print) | %{__perl} perlpath.pl %{__perl} -

# remove backups from patching as we use globs to package files to buildroot
find '(' -name '*~' -o -name '*.orig' ')' | xargs -r rm -v

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/webmin,/var/{log,run}/webmin} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webmin,webmincnf} \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d}

rm -f *.lang
cp -a * $RPM_BUILD_ROOT%{_datadir}/webmin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/webmin
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.conf
mv $RPM_BUILD_ROOT%{_datadir}/webmin/webmin-pam $RPM_BUILD_ROOT/etc/pam.d/webmin
mv $RPM_BUILD_ROOT%{_datadir}/webmin/pserver/cvsweb.conf $RPM_BUILD_ROOT%{_sysconfdir}/webmincnf/cvsweb.conf
mv $RPM_BUILD_ROOT%{_datadir}/webmin/miniserv.pem $RPM_BUILD_ROOT%{_sysconfdir}/webmin/miniserv.pem

export allmods=`cd $RPM_BUILD_ROOT%{_datadir}/webmin; ls */module.info | sed -e 's,/module.info,,g' | xargs echo`
%{__perl} $RPM_BUILD_ROOT%{_datadir}/webmin/copyconfig.pl pld-linux %{os_version} $RPM_BUILD_ROOT%{_datadir}/webmin $RPM_BUILD_ROOT%{_sysconfdir}/webmin "" $allmods

echo "%{__perl}"		> $RPM_BUILD_ROOT%{_sysconfdir}/webmin/perl-path
echo "/var/log/webmin" 		> $RPM_BUILD_ROOT%{_sysconfdir}/webmin/var-path
echo "real_os_version=%{os_version}"	> $RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "lang=en" 			>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "find_pid_command=/sbin/pidof NAME"	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "os_type=pld-linux" 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "path=/bin:%{_bindir}:/sbin:%{_sbindir}:%{_prefix}/local/bin" >>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "real_os_type=PLD Linux" 	>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config
echo "os_version=%{os_version}" 		>>$RPM_BUILD_ROOT%{_sysconfdir}/webmin/config

echo %{version} > $RPM_BUILD_ROOT%{_sysconfdir}/webmin/version

for a in acl apache at cron bind8 burner cfengine cluster-software \
	cluster-useradmin cluster-webmin custom dhcpd exports fdisk \
	pptp-server pptp-client ipsec openslp mount logrotate ldap-useradmin \
	fetchmail mailboxes webalizer file fsdump grub heartbeat inittab jabber krb5 lilo lpadmin \
	lvm majordomo man mon mysql net shorewall nis pam pap passwd postfix \
	postgresql proc procmail proftpd tunnel pserver stunnel init adsl-client \
	qmailadmin quota raid samba sendmail sentry servers shell software \
	cluster-copy cluster-cron cluster-usermin cluster-passwd cluster-shell \
	squid sshd status syslog telnet time useradmin usermin webmin dnsadmin \
	webminlog wuftpd xinetd inetd idmapd frox bandwidth firewall ; do
	sh %{SOURCE3} $RPM_BUILD_ROOT %{_datadir}/webmin/$a $a
done
for a in vgetty sarg updown htaccess-htpasswd spam smart-status ppp-client \
	backup-config change-user dovecot cpan; do
	sh %{SOURCE3} $RPM_BUILD_ROOT %{_datadir}/webmin/$a $a --no-help
done
sh %{SOURCE3} $RPM_BUILD_ROOT %{_datadir}/webmin MAIN

cat custom.lang file.lang telnet.lang webminlog.lang > admin-tools.lang
cat fdisk.lang raid.lang > disk-tools.lang
cat init.lang inittab.lang mount.lang proc.lang > system.lang
cat MAIN.lang acl.lang man.lang pam.lang servers.lang shell.lang \
	time.lang webmin.lang > base.lang

%clean
rm -rf $RPM_BUILD_ROOT

%define	webmin_modules_update \
allmods=`cd %{_datadir}/webmin; ls */module.info | sed -e 's,/module.info,,g' | xargs echo`; export allmods \
%{__perl} %{_datadir}/webmin/newmods.pl %{_sysconfdir}/webmin $allmods

%post
if ! grep -q ^host= %{_sysconfdir}/webmin/miniserv.conf; then
	echo "host=`hostname`" >> %{_sysconfdir}/webmin/miniserv.conf
fi
/sbin/chkconfig --add webmin
%service webmin restart
if [ "$1" = 1 ] ;then
	%banner %{name} -e <<EOF
Use your web browser to go to: http://your_host_name:10000
EOF
fi

%webmin_modules_update

%preun
if [ "$1" = "0" ]; then
	%service webmin stop
	/sbin/chkconfig	--del webmin
fi

%post disk-tools
%webmin_modules_update

%post apache
%webmin_modules_update

%post at
%webmin_modules_update

%post ppp-client
%webmin_modules_update

%post pptp-client
%webmin_modules_update

%post pptp-server
%webmin_modules_update

%post ipsec
%webmin_modules_update

%post firewall
%webmin_modules_update

%post idmapd
%webmin_modules_update

%post burner
%webmin_modules_update

%post smart-status
%webmin_modules_update

%post bind8
%webmin_modules_update

%post dnsadmin
%webmin_modules_update

%post cfengine
%webmin_modules_update

%post cluster-software
%webmin_modules_update

%post cluster-shell
%webmin_modules_update

%post cluster-useradmin
%webmin_modules_update

%post cluster-usermin
%webmin_modules_update

%post cluster-copy
%webmin_modules_update

%post cluster-cron
%webmin_modules_update

%post cluster-passwd
%webmin_modules_update

%post ldap-useradmin
%webmin_modules_update

%post cluster-webmin
%webmin_modules_update

%post cron
%webmin_modules_update

%post vgetty
%webmin_modules_update

%post dhcpd
%webmin_modules_update

%post adsl-client
%webmin_modules_update

%post fetchmail
%webmin_modules_update

%post dovecot
%webmin_modules_update

%post mailboxes
%webmin_modules_update

%post webalizer
%webmin_modules_update

%post updown
%webmin_modules_update

%post fsdump
%webmin_modules_update

%post backup-config
%webmin_modules_update

%post grub
%webmin_modules_update

%post heartbeat
%webmin_modules_update

%post inetd
%webmin_modules_update

%post jabber
%webmin_modules_update

%post krb5
%webmin_modules_update

%post lilo
%webmin_modules_update

%post lvm
%webmin_modules_update

%post majordomo
%webmin_modules_update

%post mon
%webmin_modules_update

%post mysql
%webmin_modules_update

%post net
%webmin_modules_update

%post bandwidth
%webmin_modules_update

%post shorewall
%webmin_modules_update

%post postfix
%webmin_modules_update

%post postgresql
%webmin_modules_update

%post ppp
%webmin_modules_update

%post procmail
%webmin_modules_update

%post spam
%webmin_modules_update

%post printer
%webmin_modules_update

%post proftpd
%webmin_modules_update

%post cvs-pserver
%webmin_modules_update

%post qmail
%webmin_modules_update

%post samba
%webmin_modules_update

%post openslp
%webmin_modules_update

%post sentry
%webmin_modules_update

%post sendmail
%webmin_modules_update

%post stunnel
%webmin_modules_update

%post tunnel
%webmin_modules_update

%post squid
%webmin_modules_update

%post frox
%webmin_modules_update

%post sarg
%webmin_modules_update

%post sshd
%webmin_modules_update

%post wuftpd
%webmin_modules_update

%post xinetd
%webmin_modules_update

%post nfs
%webmin_modules_update

%post quota
%webmin_modules_update

%post software
%webmin_modules_update

%post cpan
%webmin_modules_update

%post monitor
%webmin_modules_update

%post syslog
%webmin_modules_update

%post logrotate
%webmin_modules_update

%post admin-tools
%webmin_modules_update

%post system
%webmin_modules_update

%post nis
%webmin_modules_update

%post passwd
%webmin_modules_update

%post htaccess-htpasswd
%webmin_modules_update

%post usermin
%webmin_modules_update

%post useradmin
%webmin_modules_update

%post change-user
%webmin_modules_update

%files -f base.lang
%defattr(644,root,root,755)
%doc %{_datadir}/webmin/LICENCE
%doc %lang(ja) %{_datadir}/webmin/LICENCE.ja
%attr(750,root,root) %dir /var/log/webmin
%attr(754,root,root) /etc/rc.d/init.d/webmin
%attr(640,root,root) /etc/pam.d/webmin
%attr(755,root,root) %{_datadir}/webmin/*.pl
%attr(755,root,root) %{_datadir}/webmin/*.cgi
%doc %{_datadir}/webmin/README
%{_datadir}/webmin/images
%{_datadir}/webmin/config-pld-linux
%{_datadir}/webmin/Webmin
%{_datadir}/webmin/install-type
%{_datadir}/webmin/mime.types
%{_datadir}/webmin/*.txt
%{_datadir}/webmin/version
%{_datadir}/webmin/webmin-*
%{_datadir}/webmin/setup.sh
%{_datadir}/webmin/defaulttheme
%{_datadir}/webmin/defaultacl
%{_datadir}/webmin/favicon.ico

%attr(750,root,root) %dir %{_sysconfdir}/webmin
%dir %{_sysconfdir}/webmincnf
%config(noreplace) %{_sysconfdir}/webmin/config
%config(noreplace) %{_sysconfdir}/webmin/miniserv.conf
%attr(600,root,root) %config(noreplace) %{_sysconfdir}/webmin/miniserv.pem
%{_sysconfdir}/webmin/perl-path
%{_sysconfdir}/webmin/var-path
%{_sysconfdir}/webmin/version

# ACL #
%dir %{_sysconfdir}/webmin/acl
%dir %{_datadir}/webmin/acl
%attr(755,root,root) %{_datadir}/webmin/acl/*.cgi
%doc %{_datadir}/webmin/acl/CHANGELOG
%{_datadir}/webmin/acl/images
%{_datadir}/webmin/acl/module.info
%{_datadir}/webmin/acl/config
%{_datadir}/webmin/acl/config.info
%{_datadir}/webmin/acl/defaultacl
%{_datadir}/webmin/acl/openssl.cnf
%{_datadir}/webmin/acl/*-*.pl
%{_datadir}/webmin/acl/*_*.pl
%{_datadir}/webmin/acl/postinstall.pl
%{_datadir}/webmin/acl/xenroll.dll
%config(noreplace) %{_sysconfdir}/webmin/acl/config

# MAN
%dir %{_sysconfdir}/webmin/man
%dir %{_datadir}/webmin/man
%attr(755,root,root) %{_datadir}/webmin/man/*.cgi
%doc %{_datadir}/webmin/man/CHANGELOG
%{_datadir}/webmin/man/images
%{_datadir}/webmin/man/module.info
%{_datadir}/webmin/man/config.info
%{_datadir}/webmin/man/config-pld-linux
%{_datadir}/webmin/man/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/man/config

# PAM
%dir %{_sysconfdir}/webmin/pam
%dir %{_datadir}/webmin/pam
%attr(755,root,root) %{_datadir}/webmin/pam/*.cgi
%{_datadir}/webmin/pam/images
%{_datadir}/webmin/pam/module.info
%{_datadir}/webmin/pam/config.info
%{_datadir}/webmin/pam/*-*.pl
%{_datadir}/webmin/pam/*_*.pl
%{_datadir}/webmin/pam/template.pl
%config(noreplace) %{_sysconfdir}/webmin/pam/config

# SERVERS #
%dir %{_sysconfdir}/webmin/servers
%dir %{_datadir}/webmin/servers
%attr(755,root,root) %{_datadir}/webmin/servers/*.cgi
%doc %{_datadir}/webmin/servers/CHANGELOG
%{_datadir}/webmin/servers/images
%{_datadir}/webmin/servers/module.info
%{_datadir}/webmin/servers/config
%{_datadir}/webmin/servers/config.info
%{_datadir}/webmin/servers/defaultacl
%{_datadir}/webmin/servers/auto.pl
%{_datadir}/webmin/servers/uninstall.pl
%{_datadir}/webmin/servers/*-*.pl
%{_datadir}/webmin/servers/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/servers/config

# WEBMIN #
%dir %{_sysconfdir}/webmin/webmin
%dir %{_datadir}/webmin/webmin
%attr(755,root,root) %{_datadir}/webmin/webmin/*.cgi
%doc %{_datadir}/webmin/webmin/CHANGELOG
%{_sysconfdir}/webmin/webmin/config
%{_datadir}/webmin/webmin/images
%{_datadir}/webmin/webmin/module.info
%{_datadir}/webmin/webmin/config
%{_datadir}/webmin/webmin/config.info
%{_datadir}/webmin/webmin/*.skill
%{_datadir}/webmin/webmin/*.pl
%{_datadir}/webmin/webmin/adminupgrade
%{_datadir}/webmin/webmin/subdir
%{_datadir}/webmin/webmin/*.asc

#### HARDWARE ####

# TIME
%dir %{_sysconfdir}/webmin/time
%dir %{_datadir}/webmin/time
%attr(755,root,root) %{_datadir}/webmin/time/*.cgi
%doc %{_datadir}/webmin/time/CHANGELOG
%{_datadir}/webmin/time/images
%{_datadir}/webmin/time/module.info
%{_datadir}/webmin/time/config.info
%{_datadir}/webmin/time/defaultacl
%{_datadir}/webmin/time/*_*.pl
%{_datadir}/webmin/time/*-*.pl
%{_datadir}/webmin/time/uninstall.pl
%{_datadir}/webmin/time/sync.pl
%{_datadir}/webmin/time/rbac-mapping
%{_datadir}/webmin/time/time.js
%config(noreplace) %{_sysconfdir}/webmin/time/config

%files admin-tools -f admin-tools.lang
%defattr(644,root,root,755)
# TELNET
%dir %{_sysconfdir}/webmin/telnet
%dir %{_datadir}/webmin/telnet
%attr(755,root,root) %{_datadir}/webmin/telnet/*.cgi
#%doc %{_datadir}/webmin/telnet/CHANGELOG
%{_datadir}/webmin/telnet/images
%{_datadir}/webmin/telnet/module.info
%{_datadir}/webmin/telnet/config
%{_datadir}/webmin/telnet/config.info
%{_datadir}/webmin/telnet/*.jar
%{_datadir}/webmin/telnet/*.conf
%config(noreplace) %{_sysconfdir}/webmin/telnet/config

# CUSTOM
%dir %{_sysconfdir}/webmin/custom
%dir %{_datadir}/webmin/custom
%attr(755,root,root) %{_datadir}/webmin/custom/*.cgi
%{_datadir}/webmin/custom/images
%{_datadir}/webmin/custom/module.info
%{_datadir}/webmin/custom/config
%{_datadir}/webmin/custom/config.info
%{_datadir}/webmin/custom/defaultacl
%{_datadir}/webmin/custom/*-*.pl
%{_datadir}/webmin/custom/*_*.pl
%doc %{_datadir}/webmin/custom/CHANGELOG
%config(noreplace) %{_sysconfdir}/webmin/custom/config

# FILE
%dir %{_sysconfdir}/webmin/file
%dir %{_datadir}/webmin/file
%attr(755,root,root) %{_datadir}/webmin/file/*.cgi
%doc %{_datadir}/webmin/file/CHANGELOG
%{_sysconfdir}/webmin/file/config
%{_datadir}/webmin/file/images
%{_datadir}/webmin/file/module.info
%{_datadir}/webmin/file/unicode
%{_datadir}/webmin/file/config
%{_datadir}/webmin/file/config.info
%{_datadir}/webmin/file/defaultacl
%{_datadir}/webmin/file/*.pl
%{_datadir}/webmin/file/file.jar
%{_datadir}/webmin/file/*.class
%{_datadir}/webmin/file/Makefile

# SHELL
%dir %{_sysconfdir}/webmin/shell
%dir %{_datadir}/webmin/shell
%attr(755,root,root) %{_datadir}/webmin/shell/*.cgi
#%doc %{_datadir}/webmin/shell/CHANGELOG
%{_sysconfdir}/webmin/shell/config
%{_datadir}/webmin/shell/images
%{_datadir}/webmin/shell/module.info
%{_datadir}/webmin/shell/defaultacl
%{_datadir}/webmin/shell/config
%{_datadir}/webmin/shell/config.info
%{_datadir}/webmin/shell/*.pl

# WEBMINLOG
%dir %{_sysconfdir}/webmin/webminlog
%dir %{_datadir}/webmin/webminlog
%attr(755,root,root) %{_datadir}/webmin/webminlog/*.cgi
%doc %{_datadir}/webmin/webminlog/CHANGELOG
%{_sysconfdir}/webmin/webminlog/config
%{_datadir}/webmin/webminlog/images
%{_datadir}/webmin/webminlog/module.info
%{_datadir}/webmin/webminlog/config
%{_datadir}/webmin/webminlog/config.info
%{_datadir}/webmin/webminlog/*.pl
%{_datadir}/webmin/webminlog/defaultacl

#### DISKS ####
%files disk-tools -f disk-tools.lang
%defattr(644,root,root,755)

# FDISK
%dir %{_sysconfdir}/webmin/fdisk
%dir %{_datadir}/webmin/fdisk
%attr(755,root,root) %{_datadir}/webmin/fdisk/*.cgi
%doc %{_datadir}/webmin/fdisk/CHANGELOG
%{_datadir}/webmin/fdisk/images
%{_datadir}/webmin/fdisk/module.info
%{_datadir}/webmin/fdisk/*.pl
%{_datadir}/webmin/fdisk/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/fdisk/config

# RAID
%dir %{_sysconfdir}/webmin/raid
%dir %{_datadir}/webmin/raid
%attr(755,root,root) %{_datadir}/webmin/raid/*.cgi
%doc %{_datadir}/webmin/raid/CHANGELOG
%{_datadir}/webmin/raid/images
%{_datadir}/webmin/raid/module.info
%{_datadir}/webmin/raid/config
%{_datadir}/webmin/raid/config.info
%{_datadir}/webmin/raid/*-*.pl
%{_datadir}/webmin/raid/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/raid/config

# GRUB
%files grub -f grub.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/grub
%dir %{_datadir}/webmin/grub
%attr(755,root,root) %{_datadir}/webmin/grub/*.cgi
%{_datadir}/webmin/grub/images
%{_datadir}/webmin/grub/module.info
%{_datadir}/webmin/grub/config
%{_datadir}/webmin/grub/config.info
%{_datadir}/webmin/grub/*_*.pl
%{_datadir}/webmin/grub/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/grub/config

# JABBER
%files jabber -f jabber.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/jabber
%dir %{_datadir}/webmin/jabber
%attr(755,root,root) %{_datadir}/webmin/jabber/*.cgi
#%doc %{_datadir}/webmin/jabber/CHANGELOG
%{_datadir}/webmin/jabber/images
%{_datadir}/webmin/jabber/module.info
%{_datadir}/webmin/jabber/config
%{_datadir}/webmin/jabber/config.info
%{_datadir}/webmin/jabber/*.pl
%config(noreplace) %{_sysconfdir}/webmin/jabber/config

# KRB5
%files krb5 -f krb5.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/krb5
%dir %{_datadir}/webmin/krb5
%attr(755,root,root) %{_datadir}/webmin/krb5/*.cgi
%doc %{_datadir}/webmin/krb5/CHANGELOG
%{_datadir}/webmin/krb5/images
%{_datadir}/webmin/krb5/module.info
%{_datadir}/webmin/krb5/config
%{_datadir}/webmin/krb5/config.info
%{_datadir}/webmin/krb5/*.pl
%config(noreplace) %{_sysconfdir}/webmin/krb5/config

# LILO
%files lilo -f lilo.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lilo
%dir %{_datadir}/webmin/lilo
%attr(755,root,root) %{_datadir}/webmin/lilo/*.cgi
#%doc %{_datadir}/webmin/lilo/CHANGELOG
%{_datadir}/webmin/lilo/images
%{_datadir}/webmin/lilo/module.info
%{_datadir}/webmin/lilo/config
%{_datadir}/webmin/lilo/config.info
%{_datadir}/webmin/lilo/*-*.pl
%{_datadir}/webmin/lilo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/lilo/config

# LVM
%files lvm -f lvm.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lvm
%dir %{_datadir}/webmin/lvm
%attr(755,root,root) %{_datadir}/webmin/lvm/*.cgi
%doc %{_datadir}/webmin/lvm/CHANGELOG
%{_datadir}/webmin/lvm/images
%{_datadir}/webmin/lvm/module.info
%{_datadir}/webmin/lvm/*-*.pl
%{_datadir}/webmin/lvm/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/lvm/config

#%if 0
# LP
%files printer -f lpadmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/lpadmin
%dir %{_datadir}/webmin/lpadmin
%attr(755,root,root) %{_datadir}/webmin/lpadmin/*.cgi
%doc %{_datadir}/webmin/lpadmin/CHANGELOG
%{_datadir}/webmin/lpadmin/images
%{_datadir}/webmin/lpadmin/module.info
%{_datadir}/webmin/lpadmin/config.info
%{_datadir}/webmin/lpadmin/config-pld-linux
%{_datadir}/webmin/lpadmin/defaultacl
%{_datadir}/webmin/lpadmin/drivers
%{_datadir}/webmin/lpadmin/*-*.pl
%{_datadir}/webmin/lpadmin/*_*.pl
%{_datadir}/webmin/lpadmin/rbac-mapping
%{_datadir}/webmin/lpadmin/colour.fig
%{_datadir}/webmin/lpadmin/bw.fig
%{_datadir}/webmin/lpadmin/base_coas_driver
%{_datadir}/webmin/lpadmin/catalog.devices
%{_datadir}/webmin/lpadmin/sortdrivers.pl
%{_datadir}/webmin/lpadmin/*.ps
%{_datadir}/webmin/lpadmin/stp
%{_datadir}/webmin/lpadmin/*.txt
%config(noreplace) %{_sysconfdir}/webmin/lpadmin/config
#%endif

# MON
%files mon -f mon.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mon
%dir %{_datadir}/webmin/mon
%attr(755,root,root) %{_datadir}/webmin/mon/*.cgi
%doc %{_datadir}/webmin/mon/CHANGELOG
%{_datadir}/webmin/mon/images
%{_datadir}/webmin/mon/module.info
%{_datadir}/webmin/mon/config
%{_datadir}/webmin/mon/config.info
%{_datadir}/webmin/mon/monshowrc
%{_datadir}/webmin/mon/*-*.pl
%{_datadir}/webmin/mon/*_*.pl
%{_datadir}/webmin/mon/moncmd.pl
%{_datadir}/webmin/mon/moncmd.diff
%{_datadir}/webmin/mon/README
%config(noreplace) %{_sysconfdir}/webmin/mon/config

# NET
%files net -f net.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/net
%dir %{_datadir}/webmin/net
%attr(755,root,root) %{_datadir}/webmin/net/*.cgi
%doc %{_datadir}/webmin/net/CHANGELOG
%{_datadir}/webmin/net/images
%{_datadir}/webmin/net/module.info
%{_datadir}/webmin/net/config
%{_datadir}/webmin/net/config.info
%{_datadir}/webmin/net/config-cygwin
%{_datadir}/webmin/net/config-pld-linux
%{_datadir}/webmin/net/rc.inet1
%{_datadir}/webmin/net/defaultacl
%{_datadir}/webmin/net/rbac-mapping
%{_datadir}/webmin/net/*-*.pl
%{_datadir}/webmin/net/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/net/config

# bandwidth
%files bandwidth -f bandwidth.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/bandwidth
%dir %{_datadir}/webmin/bandwidth
%attr(755,root,root) %{_datadir}/webmin/bandwidth/*.cgi
%doc %{_datadir}/webmin/bandwidth/CHANGELOG
%{_datadir}/webmin/bandwidth/images
%{_datadir}/webmin/bandwidth/module.info
%{_datadir}/webmin/bandwidth/config
%{_datadir}/webmin/bandwidth/config.info
%{_datadir}/webmin/bandwidth/*.pl
%{_datadir}/webmin/bandwidth/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/bandwidth/config

# SHOREWALL
%files shorewall -f shorewall.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/shorewall
%dir %{_datadir}/webmin/shorewall
%attr(755,root,root) %{_datadir}/webmin/shorewall/*.cgi
%doc %{_datadir}/webmin/shorewall/CHANGELOG
%{_datadir}/webmin/shorewall/images
%{_datadir}/webmin/shorewall/module.info
%{_datadir}/webmin/shorewall/config
%{_datadir}/webmin/shorewall/config.info
%{_datadir}/webmin/shorewall/defaultacl
%{_datadir}/webmin/shorewall/*.pl
%config(noreplace) %{_sysconfdir}/webmin/shorewall/config

#### SYSTEM ####
%files system -f system.lang
%defattr(644,root,root,755)

# INIT
%dir %{_sysconfdir}/webmin/init
%dir %{_datadir}/webmin/init
%attr(755,root,root) %{_datadir}/webmin/init/*.cgi
%doc %{_datadir}/webmin/init/CHANGELOG
%{_datadir}/webmin/init/images
%{_datadir}/webmin/init/module.info
%{_datadir}/webmin/init/config.info
%{_datadir}/webmin/init/config-pld-linux
%{_datadir}/webmin/init/defaultacl
%{_datadir}/webmin/init/rbac-mapping
%{_datadir}/webmin/init/*_*.pl
%{_datadir}/webmin/init/*-*.pl
%{_datadir}/webmin/init/*boot.pl
%{_datadir}/webmin/init/uninstall.pl
%{_datadir}/webmin/init/*.risk
%{_datadir}/webmin/init/win32.pl
%config(noreplace) %{_sysconfdir}/webmin/init/config

# INITTAB
%dir %{_sysconfdir}/webmin/inittab
%dir %{_datadir}/webmin/inittab
%attr(755,root,root) %{_datadir}/webmin/inittab/*.cgi
#%doc %{_datadir}/webmin/inittab/CHANGELOG
%{_datadir}/webmin/inittab/images
%{_datadir}/webmin/inittab/module.info
%{_datadir}/webmin/inittab/config
%{_datadir}/webmin/inittab/config.info
%{_datadir}/webmin/inittab/*-*.pl
%{_datadir}/webmin/inittab/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/inittab/config

# MOUNT
%dir %{_sysconfdir}/webmin/mount
%dir %{_datadir}/webmin/mount
%attr(755,root,root) %{_datadir}/webmin/mount/*.cgi
%{_datadir}/webmin/mount/images
%{_datadir}/webmin/mount/module.info
%{_datadir}/webmin/mount/config.info
%{_datadir}/webmin/mount/config-pld-linux
%{_datadir}/webmin/mount/defaultacl
%{_datadir}/webmin/mount/*-*.pl
%{_datadir}/webmin/mount/*_*.pl
%{_datadir}/webmin/mount/rbac-mapping
%{_datadir}/webmin/mount/*.skill
%doc %{_datadir}/webmin/mount/CHANGELOG
%config(noreplace) %{_sysconfdir}/webmin/mount/config

# PROC
%dir %{_sysconfdir}/webmin/proc
%dir %{_datadir}/webmin/proc
%attr(755,root,root) %{_datadir}/webmin/proc/*.cgi
%doc %{_datadir}/webmin/proc/CHANGELOG
%{_datadir}/webmin/proc/images
%{_datadir}/webmin/proc/module.info
%{_datadir}/webmin/proc/config.info
%{_datadir}/webmin/proc/config-pld-linux
%{_datadir}/webmin/proc/defaultacl
%{_datadir}/webmin/proc/*-*.pl
%{_datadir}/webmin/proc/*_*.pl
%{_datadir}/webmin/proc/*.risk
%{_datadir}/webmin/proc/*.skill
%{_datadir}/webmin/proc/*.class
%{_datadir}/webmin/proc/*.java
%{_datadir}/webmin/proc/Makefile
%{_datadir}/webmin/proc/rbac-mapping
%config(noreplace) %{_sysconfdir}/webmin/proc/config

# PASSWD
%files passwd -f passwd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/passwd
%dir %{_datadir}/webmin/passwd
%attr(755,root,root) %{_datadir}/webmin/passwd/*.cgi
%doc %{_datadir}/webmin/passwd/CHANGELOG
%{_datadir}/webmin/passwd/images
%{_datadir}/webmin/passwd/module.info
%{_datadir}/webmin/passwd/config
%{_datadir}/webmin/passwd/config.info
%{_datadir}/webmin/passwd/defaultacl
%{_datadir}/webmin/passwd/rbac-mapping
%{_datadir}/webmin/passwd/*-*.pl
%{_datadir}/webmin/passwd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/passwd/config

# htaccess-htpasswd
%files htaccess-htpasswd -f htaccess-htpasswd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/htaccess-htpasswd
%dir %{_datadir}/webmin/htaccess-htpasswd
%attr(755,root,root) %{_datadir}/webmin/htaccess-htpasswd/*.cgi
%doc %{_datadir}/webmin/htaccess-htpasswd/CHANGELOG
%{_sysconfdir}/webmin/htaccess-htpasswd/config
%{_datadir}/webmin/htaccess-htpasswd/images
%{_datadir}/webmin/htaccess-htpasswd/module.info
%{_datadir}/webmin/htaccess-htpasswd/config
%{_datadir}/webmin/htaccess-htpasswd/config.info
%{_datadir}/webmin/htaccess-htpasswd/defaultacl
%{_datadir}/webmin/htaccess-htpasswd/*.pl
%config(noreplace) %{_sysconfdir}/webmin/passwd/config

#%if 0
# USERMIN #
%files usermin -f usermin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/usermin
%dir %{_datadir}/webmin/usermin
%attr(755,root,root) %{_datadir}/webmin/usermin/*.cgi
%doc %{_datadir}/webmin/usermin/CHANGELOG
%{_datadir}/webmin/usermin/images
%{_datadir}/webmin/usermin/module.info
%{_datadir}/webmin/usermin/config
%{_datadir}/webmin/usermin/config.info
%{_datadir}/webmin/usermin/]
%{_datadir}/webmin/usermin/defaultacl
%{_datadir}/webmin/usermin/*.pl
%config(noreplace) %{_sysconfdir}/webmin/usermin/config
#%endif

# USERADMIN
%files useradmin -f useradmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/useradmin
%dir %{_datadir}/webmin/useradmin
%attr(755,root,root) %{_datadir}/webmin/useradmin/*.cgi
%doc %{_datadir}/webmin/useradmin/CHANGELOG
%{_datadir}/webmin/useradmin/images
%{_datadir}/webmin/useradmin/module.info
%{_datadir}/webmin/useradmin/config.info
%{_datadir}/webmin/useradmin/config-pld-linux
%{_datadir}/webmin/useradmin/defaultacl
%{_datadir}/webmin/useradmin/*-*.pl
%{_datadir}/webmin/useradmin/*_*.pl
%{_datadir}/webmin/useradmin/rbac-mapping
%{_datadir}/webmin/useradmin/*.skill
%{_datadir}/webmin/useradmin/help.html
%{_datadir}/webmin/useradmin/help/icon.gif
%config(noreplace) %{_sysconfdir}/webmin/useradmin/config

# change-user
%files change-user -f change-user.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/change-user
%dir %{_datadir}/webmin/change-user
%attr(755,root,root) %{_datadir}/webmin/change-user/*.cgi
%doc %{_datadir}/webmin/change-user/CHANGELOG
%{_datadir}/webmin/change-user/images
%{_datadir}/webmin/change-user/module.info
%{_datadir}/webmin/change-user/*.pl
%{_datadir}/webmin/change-user/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/change-user/config

# NFS EXPORTS
%files nfs -f exports.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/exports
%dir %{_datadir}/webmin/exports
%attr(755,root,root) %{_datadir}/webmin/exports/*.cgi
%doc %{_datadir}/webmin/exports/CHANGELOG
%{_datadir}/webmin/exports/images
%{_datadir}/webmin/exports/module.info
%{_datadir}/webmin/exports/config.info
%{_datadir}/webmin/exports/config-pld-linux
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
%doc %{_datadir}/webmin/quota/CHANGELOG
%{_datadir}/webmin/quota/images
%{_datadir}/webmin/quota/module.info
%{_datadir}/webmin/quota/config.info
%{_datadir}/webmin/quota/config-pld-linux
%{_datadir}/webmin/quota/defaultacl
%{_datadir}/webmin/quota/*-*.pl
%{_datadir}/webmin/quota/*_*.pl
%{_datadir}/webmin/quota/uninstall.pl
%{_datadir}/webmin/quota/e*.pl
%{_datadir}/webmin/quota/notes
%config(noreplace) %{_sysconfdir}/webmin/quota/config

# SOFTWARE
%files software -f software.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/software
%dir %{_datadir}/webmin/software
%attr(755,root,root) %{_datadir}/webmin/software/*.cgi
%doc %{_datadir}/webmin/software/CHANGELOG
%{_datadir}/webmin/software/images
%{_datadir}/webmin/software/module.info
%{_datadir}/webmin/software/config.info
%{_datadir}/webmin/software/config-cygwin
%{_datadir}/webmin/software/config-pld-linux
%{_datadir}/webmin/software/catal*
%{_datadir}/webmin/software/pkgadd-no-ask
%{_datadir}/webmin/software/*-*.pl
%{_datadir}/webmin/software/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/software/config

# CPAN
%files cpan -f cpan.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cpan
%dir %{_datadir}/webmin/cpan
%attr(755,root,root) %{_datadir}/webmin/cpan/*.cgi
%doc %{_datadir}/webmin/cpan/CHANGELOG
%{_datadir}/webmin/cpan/images
%{_datadir}/webmin/cpan/module.info
%{_datadir}/webmin/cpan/config
%{_datadir}/webmin/cpan/config.info
%{_datadir}/webmin/cpan/*-*.pl
%{_datadir}/webmin/cpan/postinstall.pl
%config(noreplace) %{_sysconfdir}/webmin/cpan/config

# STATUS
%files monitor -f status.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/status
%dir %{_datadir}/webmin/status
%attr(755,root,root) %{_datadir}/webmin/status/*.cgi
%doc %{_datadir}/webmin/status/CHANGELOG
%{_datadir}/webmin/status/images
%{_datadir}/webmin/status/module.info
%{_datadir}/webmin/status/config
%{_datadir}/webmin/status/WEBMIN-STATUS-MIB.txt
%{_datadir}/webmin/status/config.info
%{_datadir}/webmin/status/defaultacl
%{_datadir}/webmin/status/*_*.pl
%{_datadir}/webmin/status/*-*.pl
%{_datadir}/webmin/status/uninstall.pl
%{_datadir}/webmin/status/monitor.pl
%{_datadir}/webmin/status/services
%config(noreplace) %{_sysconfdir}/webmin/status/config

# SYSLOG
%files syslog -f syslog.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/syslog
%dir %{_datadir}/webmin/syslog
%attr(755,root,root) %{_datadir}/webmin/syslog/*.cgi
%doc %{_datadir}/webmin/syslog/CHANGELOG
%{_datadir}/webmin/syslog/images
%{_datadir}/webmin/syslog/module.info
%{_datadir}/webmin/syslog/config.info
%{_datadir}/webmin/syslog/config-pld-linux
%{_datadir}/webmin/syslog/*-*.pl
%{_datadir}/webmin/syslog/*_*.pl
%{_datadir}/webmin/syslog/*.risk
%{_datadir}/webmin/syslog/rbac-mapping
%{_datadir}/webmin/syslog/defaultacl
%{_datadir}/webmin/syslog/*.skill
%config(noreplace) %{_sysconfdir}/webmin/syslog/config

# LOGROTATE
%files logrotate -f logrotate.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/logrotate
%dir %{_datadir}/webmin/logrotate
%attr(755,root,root) %{_datadir}/webmin/logrotate/*.cgi
%doc %{_datadir}/webmin/logrotate/CHANGELOG
%{_datadir}/webmin/logrotate/images
%{_datadir}/webmin/logrotate/module.info
%{_datadir}/webmin/logrotate/config
%{_datadir}/webmin/logrotate/config.info
%{_datadir}/webmin/logrotate/*.pl
%config(noreplace) %{_sysconfdir}/webmin/logrotate/config

#### OTHER #####

# NIS
%files nis -f nis.lang
%defattr(644,root,root,755)
# This needs to be synced with default PLD NIS config
#%config %{_datadir}/webmin/nis/nisupdate.conf
%doc nis/nisupdate.conf
%dir %{_sysconfdir}/webmin/nis
%dir %{_datadir}/webmin/nis
%attr(755,root,root) %{_datadir}/webmin/nis/*.cgi
#%doc %{_datadir}/webmin/nis/CHANGELOG
%{_datadir}/webmin/nis/images
%{_datadir}/webmin/nis/module.info
%{_datadir}/webmin/nis/config.info
%{_datadir}/webmin/nis/nisupdate.conf
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
%doc %{_datadir}/webmin/apache/CHANGELOG
%{_datadir}/webmin/apache/images
%{_datadir}/webmin/apache/module.info
%{_datadir}/webmin/apache/config.info
%{_datadir}/webmin/apache/config-pld-linux
%{_datadir}/webmin/apache/defaultacl
%{_datadir}/webmin/apache/*-*.pl
%{_datadir}/webmin/apache/*_*.pl
%{_datadir}/webmin/apache/autoindex.pl
%{_datadir}/webmin/apache/browsermatch.pl
%{_datadir}/webmin/apache/c*e.pl
%{_datadir}/webmin/apache/p*.pl
%{_datadir}/webmin/apache/*.broken
%{_datadir}/webmin/apache/worker.pl
%config(noreplace) %{_sysconfdir}/webmin/apache/config

# AT
%files at -f at.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/at
%dir %{_datadir}/webmin/at
%attr(755,root,root) %{_datadir}/webmin/at/*.cgi
%doc %{_datadir}/webmin/at/CHANGELOG
%{_datadir}/webmin/at/images
%{_datadir}/webmin/at/module.info
%{_datadir}/webmin/at/config.info
%{_datadir}/webmin/at/defaultacl
%{_datadir}/webmin/at/*-*.pl
%{_datadir}/webmin/at/*_*.pl
%{_datadir}/webmin/at/rbac-mapping
%config(noreplace) %{_sysconfdir}/webmin/at/config

# ppp-client
%files ppp-client -f ppp-client.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/ppp-client
%dir %{_datadir}/webmin/ppp-client
%attr(755,root,root) %{_datadir}/webmin/ppp-client/*.cgi
%doc %{_datadir}/webmin/ppp-client/CHANGELOG
%{_datadir}/webmin/ppp-client/images
%{_datadir}/webmin/ppp-client/module.info
%{_datadir}/webmin/ppp-client/config
%{_datadir}/webmin/ppp-client/config.info
%{_datadir}/webmin/ppp-client/*.pl
%config(noreplace) %{_sysconfdir}/webmin/ppp-client/config

# pptp-client
%files pptp-client -f pptp-client.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pptp-client
%dir %{_datadir}/webmin/pptp-client
%attr(755,root,root) %{_datadir}/webmin/pptp-client/*.cgi
%doc %{_datadir}/webmin/pptp-client/CHANGELOG
%{_datadir}/webmin/pptp-client/images
%{_datadir}/webmin/pptp-client/config
%{_datadir}/webmin/pptp-client/config.info
%{_datadir}/webmin/pptp-client/module.info
%{_datadir}/webmin/pptp-client/*_*.pl
%{_datadir}/webmin/pptp-client/*-*.pl
%{_datadir}/webmin/pptp-client/st*.pl
%config(noreplace) %{_sysconfdir}/webmin/pptp-client/config

# pptp-server
%files pptp-server -f pptp-server.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pptp-server
%dir %{_datadir}/webmin/pptp-server
%attr(755,root,root) %{_datadir}/webmin/pptp-server/*.cgi
%doc %{_datadir}/webmin/pptp-server/CHANGELOG
%{_datadir}/webmin/pptp-server/images
%{_datadir}/webmin/pptp-server/module.info
%{_datadir}/webmin/pptp-server/config
%{_datadir}/webmin/pptp-server/config.info
%{_datadir}/webmin/pptp-server/*.pl
%{_datadir}/webmin/pptp-server/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/pptp-server/config

# ipsec
%files ipsec -f ipsec.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/ipsec
%dir %{_datadir}/webmin/ipsec
%attr(755,root,root) %{_datadir}/webmin/ipsec/*.cgi
%doc %{_datadir}/webmin/ipsec/CHANGELOG
%{_datadir}/webmin/ipsec/images
%{_datadir}/webmin/ipsec/module.info
%{_datadir}/webmin/ipsec/config
%{_datadir}/webmin/ipsec/config.info
%{_datadir}/webmin/ipsec/*.pl
%config(noreplace) %{_sysconfdir}/webmin/ipsec/config

# firewall
%files firewall -f firewall.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/firewall
%dir %{_datadir}/webmin/firewall
%attr(755,root,root) %{_datadir}/webmin/firewall/*.cgi
%doc %{_datadir}/webmin/firewall/CHANGELOG
%{_datadir}/webmin/firewall/images
%{_datadir}/webmin/firewall/module.info
%{_datadir}/webmin/firewall/config
%{_datadir}/webmin/firewall/config.info
%{_datadir}/webmin/firewall/*.pl
%{_datadir}/webmin/firewall/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/firewall/config

# idmapd
%files idmapd -f idmapd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/idmapd
%dir %{_datadir}/webmin/idmapd
%attr(755,root,root) %{_datadir}/webmin/idmapd/*.cgi
%doc %{_datadir}/webmin/idmapd/CHANGELOG
%{_datadir}/webmin/idmapd/images
%{_datadir}/webmin/idmapd/module.info
%{_datadir}/webmin/idmapd/config
%{_datadir}/webmin/idmapd/config.info
%{_datadir}/webmin/idmapd/*.pl
%config(noreplace) %{_sysconfdir}/webmin/idmapd/config

# BIND 8/9 #
%files bind8 -f bind8.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/bind8
%dir %{_datadir}/webmin/bind8
%attr(755,root,root) %{_datadir}/webmin/bind8/*.cgi
%doc %{_datadir}/webmin/bind8/CHANGELOG
%{_datadir}/webmin/bind8/images
%{_datadir}/webmin/bind8/module.info
%{_datadir}/webmin/bind8/config.info
%{_datadir}/webmin/bind8/config-pld-linux
%{_datadir}/webmin/bind8/defaultacl
%{_datadir}/webmin/bind8/*-*.pl
%{_datadir}/webmin/bind8/*_*.pl
%{_datadir}/webmin/bind8/db.cache
%{_datadir}/webmin/bind8/whois-*
%config(noreplace) %{_sysconfdir}/webmin/bind8/config

# dnsadmin #
%files dnsadmin -f dnsadmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/dnsadmin
%dir %{_datadir}/webmin/dnsadmin
%attr(755,root,root) %{_datadir}/webmin/dnsadmin/*.cgi
%{_datadir}/webmin/dnsadmin/images
%{_datadir}/webmin/dnsadmin/module.info
%{_datadir}/webmin/dnsadmin/config.info
%{_datadir}/webmin/dnsadmin/db.cache
%{_datadir}/webmin/dnsadmin/defaultacl
%{_datadir}/webmin/dnsadmin/*_*.pl
%{_datadir}/webmin/dnsadmin/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/dnsadmin/config

# BURNER #
%files burner -f burner.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/burner
%dir %{_datadir}/webmin/burner
%attr(755,root,root) %{_datadir}/webmin/burner/*.cgi
%doc %{_datadir}/webmin/burner/CHANGELOG
%{_datadir}/webmin/burner/images
%{_datadir}/webmin/burner/module.info
%{_datadir}/webmin/burner/config
%{_datadir}/webmin/burner/*-*.pl
%{_datadir}/webmin/burner/*_*.pl
%{_datadir}/webmin/burner/defaultacl
%{_datadir}/webmin/burner/rbac-mapping
%config(noreplace) %{_sysconfdir}/webmin/burner/config

# smart-status #
%files smart-status -f smart-status.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/smart-status
%dir %{_datadir}/webmin/smart-status
%attr(755,root,root) %{_datadir}/webmin/smart-status/*.cgi
%doc %{_datadir}/webmin/smart-status/CHANGELOG
%{_datadir}/webmin/smart-status/images
%{_datadir}/webmin/smart-status/module.info
%{_datadir}/webmin/smart-status/config
%{_datadir}/webmin/smart-status/config.info
%{_datadir}/webmin/smart-status/*.pl
%config(noreplace) %{_sysconfdir}/webmin/smart-status/config

#%if 0
# CFENGINE
%files cfengine -f cfengine.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cfengine
%dir %{_datadir}/webmin/cfengine
%attr(755,root,root) %{_datadir}/webmin/cfengine/*.cgi
%{_datadir}/webmin/cfengine/images
%{_datadir}/webmin/cfengine/module.info
%{_datadir}/webmin/cfengine/config
%{_datadir}/webmin/cfengine/config.info
%{_datadir}/webmin/cfengine/*-*.pl
%{_datadir}/webmin/cfengine/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cfengine/config
#%endif

# CLUSTER-SOFTWARE
%files cluster-software -f cluster-software.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-software
%dir %{_datadir}/webmin/cluster-software
%attr(755,root,root) %{_datadir}/webmin/cluster-software/*.cgi
%doc %{_datadir}/webmin/cluster-software/CHANGELOG
%{_datadir}/webmin/cluster-software/images
%{_datadir}/webmin/cluster-software/module.info
%{_datadir}/webmin/cluster-software/config
%{_datadir}/webmin/cluster-software/config.info
%{_datadir}/webmin/cluster-software/*-*.pl
%{_datadir}/webmin/cluster-software/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/cluster-software/config

# CLUSTER-SHELL
%files cluster-shell -f cluster-shell.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-shell
%dir %{_datadir}/webmin/cluster-shell
%attr(755,root,root) %{_datadir}/webmin/cluster-shell/*.cgi
%{_datadir}/webmin/cluster-shell/images
%{_datadir}/webmin/cluster-shell/module.info
%{_datadir}/webmin/cluster-shell/*-*.pl
%{_datadir}/webmin/cluster-shell/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-shell/config

# CLUSTER-USERADMIN
%files cluster-useradmin -f cluster-useradmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-useradmin
%dir %{_datadir}/webmin/cluster-useradmin
%attr(755,root,root) %{_datadir}/webmin/cluster-useradmin/*.cgi
%doc %{_datadir}/webmin/cluster-useradmin/CHANGELOG
%{_datadir}/webmin/cluster-useradmin/images
%{_datadir}/webmin/cluster-useradmin/module.info
%{_datadir}/webmin/cluster-useradmin/config
%{_datadir}/webmin/cluster-useradmin/config.info
%{_datadir}/webmin/cluster-useradmin/*-*.pl
%{_datadir}/webmin/cluster-useradmin/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-useradmin/config

# CLUSTER-USERMIN
%files cluster-usermin -f cluster-usermin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-usermin
%dir %{_datadir}/webmin/cluster-usermin
%attr(755,root,root) %{_datadir}/webmin/cluster-usermin/*.cgi
%doc %{_datadir}/webmin/cluster-usermin/CHANGELOG
%{_datadir}/webmin/cluster-usermin/images
%{_datadir}/webmin/cluster-usermin/module.info
%{_datadir}/webmin/cluster-usermin/config
%{_datadir}/webmin/cluster-usermin/config.info
%{_datadir}/webmin/cluster-usermin/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-usermin/config

# CLUSTER-COPY
%files cluster-copy -f cluster-copy.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-copy
%dir %{_datadir}/webmin/cluster-copy
%attr(755,root,root) %{_datadir}/webmin/cluster-copy/*.cgi
%doc %{_datadir}/webmin/cluster-copy/CHANGELOG
%{_datadir}/webmin/cluster-copy/images
%{_datadir}/webmin/cluster-copy/module.info
%{_datadir}/webmin/cluster-copy/*-*.pl
%{_datadir}/webmin/cluster-copy/*_*.pl
%{_datadir}/webmin/cluster-copy/copy.pl
%{_datadir}/webmin/cluster-copy/uninstall.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-copy/config

# CLUSTER-CRON
%files cluster-cron -f cluster-cron.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-cron
%dir %{_datadir}/webmin/cluster-cron
%attr(755,root,root) %{_datadir}/webmin/cluster-cron/*.cgi
%{_datadir}/webmin/cluster-cron/images
%{_datadir}/webmin/cluster-cron/module.info
%{_datadir}/webmin/cluster-cron/*-*.pl
%{_datadir}/webmin/cluster-cron/*_*.pl
%{_datadir}/webmin/cluster-cron/cron.pl
%{_datadir}/webmin/cluster-cron/uninstall.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-cron/config

# CLUSTER-PASSWD
%files cluster-passwd -f cluster-passwd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-passwd
%dir %{_datadir}/webmin/cluster-passwd
%attr(755,root,root) %{_datadir}/webmin/cluster-passwd/*.cgi
%doc %{_datadir}/webmin/cluster-passwd/CHANGELOG
%{_datadir}/webmin/cluster-passwd/images
%{_datadir}/webmin/cluster-passwd/module.info
%{_datadir}/webmin/cluster-passwd/config
%{_datadir}/webmin/cluster-passwd/config.info
%{_datadir}/webmin/cluster-passwd/*-*.pl
%{_datadir}/webmin/cluster-passwd/*_*.pl
%{_datadir}/webmin/cluster-passwd/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/cluster-passwd/config

# ldap-USERADMIN
%files ldap-useradmin -f ldap-useradmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/ldap-useradmin
%dir %{_datadir}/webmin/ldap-useradmin
%attr(755,root,root) %{_datadir}/webmin/ldap-useradmin/*.cgi
%doc %{_datadir}/webmin/ldap-useradmin/CHANGELOG
%{_datadir}/webmin/ldap-useradmin/images
%{_datadir}/webmin/ldap-useradmin/module.info
%{_datadir}/webmin/ldap-useradmin/config
%{_datadir}/webmin/ldap-useradmin/config.info
%{_datadir}/webmin/ldap-useradmin/*.pl
%{_datadir}/webmin/ldap-useradmin/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/ldap-useradmin/config

# CLUSTER-WEBMIN
%files cluster-webmin -f cluster-webmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cluster-webmin
%dir %{_datadir}/webmin/cluster-webmin
%attr(755,root,root) %{_datadir}/webmin/cluster-webmin/*.cgi
%doc %{_datadir}/webmin/cluster-webmin/CHANGELOG
%{_datadir}/webmin/cluster-webmin/images
%{_datadir}/webmin/cluster-webmin/module.info
%{_datadir}/webmin/cluster-webmin/config
%{_datadir}/webmin/cluster-webmin/config.info
%{_datadir}/webmin/cluster-webmin/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/cluster-webmin/config

# CRON
%files cron -f cron.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/cron
%dir %{_datadir}/webmin/cron
%attr(755,root,root) %{_datadir}/webmin/cron/*.cgi
%doc %{_datadir}/webmin/cron/CHANGELOG
%{_datadir}/webmin/cron/images
%{_datadir}/webmin/cron/module.info
%{_datadir}/webmin/cron/config.info
%{_datadir}/webmin/cron/config-pld-linux
%{_datadir}/webmin/cron/defaultacl
%{_datadir}/webmin/cron/*-*.pl
%{_datadir}/webmin/cron/*_*.pl
%{_datadir}/webmin/cron/range.pl
%{_datadir}/webmin/cron/rbac-mapping
%config(noreplace) %{_sysconfdir}/webmin/cron/config

# vgetty
%files vgetty -f vgetty.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/vgetty
%dir %{_datadir}/webmin/vgetty
%attr(755,root,root) %{_datadir}/webmin/vgetty/*.cgi
%{_datadir}/webmin/vgetty/images
%{_datadir}/webmin/vgetty/module.info
%{_datadir}/webmin/vgetty/config
%{_datadir}/webmin/vgetty/config.info
%{_datadir}/webmin/vgetty/*.pl
%config(noreplace) %{_sysconfdir}/webmin/vgetty/config

# DHCPD #
%files dhcpd -f dhcpd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/dhcpd
%dir %{_datadir}/webmin/dhcpd
%attr(755,root,root) %{_datadir}/webmin/dhcpd/*.cgi
%doc %{_datadir}/webmin/dhcpd/CHANGELOG
%{_datadir}/webmin/dhcpd/images
%{_datadir}/webmin/dhcpd/module.info
%{_datadir}/webmin/dhcpd/config.info
%{_datadir}/webmin/dhcpd/config-pld-linux
%{_datadir}/webmin/dhcpd/defaultacl
%{_datadir}/webmin/dhcpd/*-*.pl
%{_datadir}/webmin/dhcpd/*_*.pl
%{_datadir}/webmin/dhcpd/rbac-mapping
%config(noreplace) %{_sysconfdir}/webmin/dhcpd/config

# adsl-client #
%files adsl-client -f adsl-client.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/adsl-client
%dir %{_datadir}/webmin/adsl-client
%attr(755,root,root) %{_datadir}/webmin/adsl-client/*.cgi
%doc %{_datadir}/webmin/adsl-client/CHANGELOG
%{_datadir}/webmin/adsl-client/images
%{_datadir}/webmin/adsl-client/module.info
%{_datadir}/webmin/adsl-client/config
%{_datadir}/webmin/adsl-client/config.info
%{_datadir}/webmin/adsl-client/ifcfg-ppp
%{_datadir}/webmin/adsl-client/*.pl
%config(noreplace) %{_sysconfdir}/webmin/adsl-client/config

# FETCHMAIL #
%files fetchmail -f fetchmail.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/fetchmail
%dir %{_datadir}/webmin/fetchmail
%attr(755,root,root) %{_datadir}/webmin/fetchmail/*.cgi
%doc %{_datadir}/webmin/fetchmail/CHANGELOG
%{_datadir}/webmin/fetchmail/images
%{_datadir}/webmin/fetchmail/module.info
%{_datadir}/webmin/fetchmail/config
%{_datadir}/webmin/fetchmail/config.info
%{_datadir}/webmin/fetchmail/defaultacl
%{_datadir}/webmin/fetchmail/*-*.pl
%{_datadir}/webmin/fetchmail/*_*.pl
%{_datadir}/webmin/fetchmail/check.pl
%config(noreplace) %{_sysconfdir}/webmin/fetchmail/config

# DOVECOT #
%files dovecot -f dovecot.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/dovecot
%dir %{_datadir}/webmin/dovecot
%attr(755,root,root) %{_datadir}/webmin/dovecot/*.cgi
%doc %{_datadir}/webmin/dovecot/CHANGELOG
%{_datadir}/webmin/dovecot/images
%{_datadir}/webmin/dovecot/module.info
%{_datadir}/webmin/dovecot/config
%{_datadir}/webmin/dovecot/config.info
%{_datadir}/webmin/dovecot/*.pl
%config(noreplace) %{_sysconfdir}/webmin/dovecot/config

# MAILBOXES #
%files mailboxes -f mailboxes.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mailboxes
%dir %{_datadir}/webmin/mailboxes
%attr(755,root,root) %{_datadir}/webmin/mailboxes/*.cgi
%doc %{_datadir}/webmin/mailboxes/CHANGELOG
%{_datadir}/webmin/mailboxes/images
%{_datadir}/webmin/mailboxes/module.info
%{_datadir}/webmin/mailboxes/config
%{_datadir}/webmin/mailboxes/config.info
%{_datadir}/webmin/mailboxes/defaultacl
%{_datadir}/webmin/mailboxes/htmlarea
%{_datadir}/webmin/mailboxes/*.pl
%{_datadir}/webmin/mailboxes/Makefile
%config(noreplace) %{_sysconfdir}/webmin/mailboxes/config

# WEBALIZER #
%files webalizer -f webalizer.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/webalizer
%dir %{_datadir}/webmin/webalizer
%attr(755,root,root) %{_datadir}/webmin/webalizer/*.cgi
%doc %{_datadir}/webmin/webalizer/CHANGELOG
%{_datadir}/webmin/webalizer/images
%{_datadir}/webmin/webalizer/module.info
%{_datadir}/webmin/webalizer/config
%{_datadir}/webmin/webalizer/config.info
%{_datadir}/webmin/webalizer/defaultacl
%{_datadir}/webmin/webalizer/*.pl
%config(noreplace) %{_sysconfdir}/webmin/webalizer/config

# UPDOWN #
%files updown -f updown.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/updown
%dir %{_datadir}/webmin/updown
%attr(755,root,root) %{_datadir}/webmin/updown/*.cgi
%doc %{_datadir}/webmin/updown/CHANGELOG
%{_datadir}/webmin/updown/images
%{_datadir}/webmin/updown/module.info
%{_datadir}/webmin/updown/config
%{_datadir}/webmin/updown/defaultacl
%{_datadir}/webmin/updown/*.pl
%config(noreplace) %{_sysconfdir}/webmin/updown/config

# SENDMAIL #
%files sendmail -f sendmail.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sendmail
%dir %{_datadir}/webmin/sendmail
%attr(755,root,root) %{_datadir}/webmin/sendmail/*.cgi
%doc %{_datadir}/webmin/sendmail/CHANGELOG
%{_datadir}/webmin/sendmail/images
%{_datadir}/webmin/sendmail/module.info
%{_datadir}/webmin/sendmail/config.info
%{_datadir}/webmin/sendmail/config-pld-linux
%{_datadir}/webmin/sendmail/defaultacl
%{_datadir}/webmin/sendmail/list_us
%{_datadir}/webmin/sendmail/dontblames
%{_datadir}/webmin/sendmail/defines
%{_datadir}/webmin/sendmail/rbac-mapping
%{_datadir}/webmin/sendmail/*-*.pl
%{_datadir}/webmin/sendmail/*_*.pl
%{_datadir}/webmin/sendmail/filter.pl
%{_datadir}/webmin/sendmail/autoreply.pl
%config(noreplace) %{_sysconfdir}/webmin/sendmail/config

# DUMP #
%files fsdump -f fsdump.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/fsdump
%dir %{_datadir}/webmin/fsdump
%attr(755,root,root) %{_datadir}/webmin/fsdump/*.cgi
%doc %{_datadir}/webmin/fsdump/CHANGELOG
%{_datadir}/webmin/fsdump/images
%{_datadir}/webmin/fsdump/module.info
%{_datadir}/webmin/fsdump/config
%{_datadir}/webmin/fsdump/config.info
%{_datadir}/webmin/fsdump/*.pl
%{_datadir}/webmin/fsdump/defaultacl
%config(noreplace) %{_sysconfdir}/webmin/fsdump/config

# backup-config #
%files backup-config -f backup-config.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/backup-config
%dir %{_datadir}/webmin/backup-config
%attr(755,root,root) %{_datadir}/webmin/backup-config/*.cgi
%doc %{_datadir}/webmin/backup-config/CHANGELOG
%{_datadir}/webmin/backup-config/images
%{_datadir}/webmin/backup-config/module.info
%{_datadir}/webmin/backup-config/config
%{_datadir}/webmin/backup-config/config.info
%{_datadir}/webmin/backup-config/*.pl
%{_datadir}/webmin/backup-config/help/config_date_subs.html
%config(noreplace) %{_sysconfdir}/webmin/backup-config/config

# HEARTBEAT #
%files heartbeat -f heartbeat.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/heartbeat
%dir %{_datadir}/webmin/heartbeat
%attr(755,root,root) %{_datadir}/webmin/heartbeat/*.cgi
%{_datadir}/webmin/heartbeat/images
%{_datadir}/webmin/heartbeat/module.info
%{_datadir}/webmin/heartbeat/config
%{_datadir}/webmin/heartbeat/config.info
%{_datadir}/webmin/heartbeat/*-*.pl
%{_datadir}/webmin/heartbeat/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/heartbeat/config

# INETD
%files inetd -f inetd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/inetd
%dir %{_datadir}/webmin/inetd
%attr(755,root,root) %{_datadir}/webmin/inetd/*.cgi
%{_datadir}/webmin/inetd/images
%{_datadir}/webmin/inetd/module.info
%{_datadir}/webmin/inetd/config.info
%{_datadir}/webmin/inetd/config-pld-linux
%{_datadir}/webmin/inetd/*-*.pl
%{_datadir}/webmin/inetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/inetd/config

#%if 0
# MAJORDOMO #
%files majordomo -f majordomo.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/majordomo
%dir %{_datadir}/webmin/majordomo
%attr(755,root,root) %{_datadir}/webmin/majordomo/*.cgi
#%doc %{_datadir}/webmin/majordomo/CHANGELOG
%{_datadir}/webmin/majordomo/images
%{_datadir}/webmin/majordomo/module.info
%{_datadir}/webmin/majordomo/config
%{_datadir}/webmin/majordomo/config.info
%{_datadir}/webmin/majordomo/defaultacl
%{_datadir}/webmin/majordomo/*-*.pl
%{_datadir}/webmin/majordomo/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/majordomo/config
#%endif

# MYSQL #
%files mysql -f mysql.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/mysql
%dir %{_datadir}/webmin/mysql
%attr(755,root,root) %{_datadir}/webmin/mysql/*.cgi
%doc %{_datadir}/webmin/mysql/CHANGELOG
%{_datadir}/webmin/mysql/images
%{_datadir}/webmin/mysql/module.info
%{_datadir}/webmin/mysql/config
%{_datadir}/webmin/mysql/config.info
%{_datadir}/webmin/mysql/config-pld-linux
%{_datadir}/webmin/mysql/defaultacl
%{_datadir}/webmin/mysql/*-*.pl
%{_datadir}/webmin/mysql/*_*.pl
%{_datadir}/webmin/mysql/backup.pl
%config(noreplace) %{_sysconfdir}/webmin/mysql/config

# POSTFIX #
%files postfix -f postfix.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postfix
%dir %{_datadir}/webmin/postfix
%attr(755,root,root) %{_datadir}/webmin/postfix/*.cgi
%doc %{_datadir}/webmin/postfix/CHANGELOG
%{_datadir}/webmin/postfix/images
%{_datadir}/webmin/postfix/module.info
%{_datadir}/webmin/postfix/config
%{_datadir}/webmin/postfix/config.info
%{_datadir}/webmin/postfix/defaultacl
%{_datadir}/webmin/postfix/*-*.pl
%{_datadir}/webmin/postfix/*_*.pl
%{_datadir}/webmin/postfix/filter.pl
%{_datadir}/webmin/postfix/autoreply.pl
%config(noreplace) %{_sysconfdir}/webmin/postfix/config

# POSTGRESQL #
%files postgresql -f postgresql.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/postgresql
%dir %{_datadir}/webmin/postgresql
%attr(755,root,root) %{_datadir}/webmin/postgresql/*.cgi
%doc %{_datadir}/webmin/postgresql/CHANGELOG
%{_datadir}/webmin/postgresql/images
%{_datadir}/webmin/postgresql/module.info
%{_datadir}/webmin/postgresql/config
%{_datadir}/webmin/postgresql/config.info
%{_datadir}/webmin/postgresql/defaultacl
%{_datadir}/webmin/postgresql/*_*.pl
%{_datadir}/webmin/postgresql/*-*.pl
%{_datadir}/webmin/postgresql/backup.pl
%config(noreplace) %{_sysconfdir}/webmin/postgresql/config

# PROCMAIL #
%files procmail -f procmail.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/procmail
%dir %{_datadir}/webmin/procmail
%attr(755,root,root) %{_datadir}/webmin/procmail/*.cgi
#%doc %{_datadir}/webmin/procmail/CHANGELOG
%{_datadir}/webmin/procmail/images
%{_datadir}/webmin/procmail/module.info
%{_datadir}/webmin/procmail/config
%{_datadir}/webmin/procmail/config.info
%{_datadir}/webmin/procmail/*.pl
%config(noreplace) %{_sysconfdir}/webmin/procmail/config

# SPAM #
%files spam -f spam.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/spam
%dir %{_datadir}/webmin/spam
%attr(755,root,root) %{_datadir}/webmin/spam/*.cgi
%doc %{_datadir}/webmin/spam/CHANGELOG
%{_datadir}/webmin/spam/images
%{_datadir}/webmin/spam/module.info
%{_datadir}/webmin/spam/config
%{_datadir}/webmin/spam/config.info
%{_datadir}/webmin/spam/*.pl
%{_datadir}/webmin/spam/defaultacl
%{_datadir}/webmin/spam/langs
%{_datadir}/webmin/spam/locales
%config(noreplace) %{_sysconfdir}/webmin/spam/config

# PROFTPD #
%files proftpd -f proftpd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/proftpd
%dir %{_datadir}/webmin/proftpd
%attr(755,root,root) %{_datadir}/webmin/proftpd/*.cgi
%doc %{_datadir}/webmin/proftpd/CHANGELOG
%{_datadir}/webmin/proftpd/images
%{_datadir}/webmin/proftpd/module.info
%{_datadir}/webmin/proftpd/config
%{_datadir}/webmin/proftpd/config.info
%{_datadir}/webmin/proftpd/*-*.pl
%{_datadir}/webmin/proftpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/proftpd/config

# CVS-PSERVER #
%files cvs-pserver -f pserver.lang
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/webmincnf/cvsweb.conf
%dir %{_sysconfdir}/webmin/pserver
%dir %{_datadir}/webmin/pserver
%attr(755,root,root) %{_datadir}/webmin/pserver/*.cgi
%doc %{_datadir}/webmin/pserver/CHANGELOG
%{_datadir}/webmin/pserver/images
%{_datadir}/webmin/pserver/module.info
%{_datadir}/webmin/pserver/config
%{_datadir}/webmin/pserver/config.info
%{_datadir}/webmin/pserver/header.html
%{_datadir}/webmin/pserver/defaultacl
%{_datadir}/webmin/pserver/*-*.pl
%{_datadir}/webmin/pserver/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/pserver/config

# PAP (PPPD) #
%files ppp -f pap.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/pap
%dir %{_datadir}/webmin/pap
%attr(755,root,root) %{_datadir}/webmin/pap/*.cgi
#%doc %{_datadir}/webmin/pap/CHANGELOG
%{_datadir}/webmin/pap/images
%{_datadir}/webmin/pap/module.info
%{_datadir}/webmin/pap/config.info
%{_datadir}/webmin/pap/config-pld-linux
%{_datadir}/webmin/pap/defaultacl
%{_datadir}/webmin/pap/*-*.pl
%{_datadir}/webmin/pap/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/pap/config

# QMAIL #
%files qmail -f qmailadmin.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/qmailadmin
%dir %{_datadir}/webmin/qmailadmin
%attr(755,root,root) %{_datadir}/webmin/qmailadmin/*.cgi
%doc %{_datadir}/webmin/qmailadmin/CHANGELOG
%{_datadir}/webmin/qmailadmin/images
%{_datadir}/webmin/qmailadmin/module.info
%{_datadir}/webmin/qmailadmin/config
%{_datadir}/webmin/qmailadmin/config.info
%{_datadir}/webmin/qmailadmin/*-*.pl
%{_datadir}/webmin/qmailadmin/*_*.pl
%{_datadir}/webmin/qmailadmin/filter.pl
%{_datadir}/webmin/qmailadmin/autoreply.pl
%config(noreplace) %{_sysconfdir}/webmin/qmailadmin/config

# SAMBA #
%files samba -f samba.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/samba
%dir %{_datadir}/webmin/samba
%attr(755,root,root) %{_datadir}/webmin/samba/*.cgi
%doc %{_datadir}/webmin/samba/CHANGELOG
%{_datadir}/webmin/samba/images
%{_datadir}/webmin/samba/module.info
%{_datadir}/webmin/samba/config.info
%{_datadir}/webmin/samba/config-pld-linux
%{_datadir}/webmin/samba/defaultacl
%{_datadir}/webmin/samba/rbac-mapping
%{_datadir}/webmin/samba/opts.pl.dev
%{_datadir}/webmin/samba/*_*.pl
%{_datadir}/webmin/samba/*-*.pl
%{_datadir}/webmin/samba/smbhash.pl
%config(noreplace) %{_sysconfdir}/webmin/samba/config

# OPENSLP #
%files openslp -f openslp.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/openslp
%dir %{_datadir}/webmin/openslp
%attr(755,root,root) %{_datadir}/webmin/openslp/*.cgi
#%doc %{_datadir}/webmin/openslp/CHANGELOG
%{_datadir}/webmin/openslp/images
%{_datadir}/webmin/openslp/module.info
%{_datadir}/webmin/openslp/README
%{_datadir}/webmin/openslp/config
%{_datadir}/webmin/openslp/config.info
%{_datadir}/webmin/openslp/*.pl
%config(noreplace) %{_sysconfdir}/webmin/openslp/config

# SENTRY #
%files sentry -f sentry.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sentry
%dir %{_datadir}/webmin/sentry
%attr(755,root,root) %{_datadir}/webmin/sentry/*.cgi
#%doc %{_datadir}/webmin/sentry/CHANGELOG
%{_datadir}/webmin/sentry/images
%{_datadir}/webmin/sentry/module.info
%{_datadir}/webmin/sentry/config
%{_datadir}/webmin/sentry/config.info
%{_datadir}/webmin/sentry/*-*.pl
%{_datadir}/webmin/sentry/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/sentry/config

# SQUID #
%files squid -f squid.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/squid
%dir %{_datadir}/webmin/squid
%attr(755,root,root) %{_datadir}/webmin/squid/*.cgi
%doc %{_datadir}/webmin/squid/CHANGELOG
%{_datadir}/webmin/squid/images
%{_datadir}/webmin/squid/module.info
%{_datadir}/webmin/squid/config.info
%{_datadir}/webmin/squid/config-pld-linux
%{_datadir}/webmin/squid/defaultacl
%{_datadir}/webmin/squid/nat
%{_datadir}/webmin/squid/*-*.pl
%{_datadir}/webmin/squid/*_*.pl
%{_datadir}/webmin/squid/*.skill
%config(noreplace) %{_sysconfdir}/webmin/squid/config

# FROX #
%files frox -f frox.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/frox
%dir %{_datadir}/webmin/frox
%attr(755,root,root) %{_datadir}/webmin/frox/*.cgi
%doc %{_datadir}/webmin/frox/CHANGELOG
%{_datadir}/webmin/frox/images
%{_datadir}/webmin/frox/module.info
%{_datadir}/webmin/frox/config
%{_datadir}/webmin/frox/config.info
%{_datadir}/webmin/frox/*-*.pl
%{_datadir}/webmin/frox/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/frox/config

# sarg #
%files sarg -f sarg.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sarg
%dir %{_datadir}/webmin/sarg
%attr(755,root,root) %{_datadir}/webmin/sarg/*.cgi
%doc %{_datadir}/webmin/sarg/CHANGELOG
%{_datadir}/webmin/sarg/images
%{_datadir}/webmin/sarg/module.info
%{_datadir}/webmin/sarg/config
%{_datadir}/webmin/sarg/config.info
%{_datadir}/webmin/sarg/languages
%{_datadir}/webmin/sarg/*.pl
%{_datadir}/webmin/sarg/charsets
%config(noreplace) %{_sysconfdir}/webmin/sarg/config

# STUNNEL #
%files stunnel -f stunnel.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/stunnel
%dir %{_datadir}/webmin/stunnel
%attr(755,root,root) %{_datadir}/webmin/stunnel/*.cgi
#%doc %{_datadir}/webmin/stunnel/CHANGELOG
%{_datadir}/webmin/stunnel/images
%{_datadir}/webmin/stunnel/module.info
%{_datadir}/webmin/stunnel/config
%{_datadir}/webmin/stunnel/config.info
%{_datadir}/webmin/stunnel/*-*.pl
%{_datadir}/webmin/stunnel/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/stunnel/config

# TUNNEL #
%files tunnel -f tunnel.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/tunnel
%dir %{_datadir}/webmin/tunnel
%attr(755,root,root) %{_datadir}/webmin/tunnel/*.cgi
%doc %{_datadir}/webmin/tunnel/CHANGELOG
%{_datadir}/webmin/tunnel/images
%{_datadir}/webmin/tunnel/module.info
%{_datadir}/webmin/tunnel/config
%{_datadir}/webmin/tunnel/config.info
%{_datadir}/webmin/tunnel/*-*.pl
%config(noreplace) %{_sysconfdir}/webmin/tunnel/config

# SSHD #
%files sshd -f sshd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/sshd
%dir %{_datadir}/webmin/sshd
%attr(755,root,root) %{_datadir}/webmin/sshd/*.cgi
%doc %{_datadir}/webmin/sshd/CHANGELOG
%{_datadir}/webmin/sshd/config
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
#%doc %{_datadir}/webmin/wuftpd/CHANGELOG
%{_datadir}/webmin/wuftpd/images
%{_datadir}/webmin/wuftpd/module.info
%{_datadir}/webmin/wuftpd/config.info
%{_datadir}/webmin/wuftpd/config-pld-linux
%{_datadir}/webmin/wuftpd/*-*.pl
%{_datadir}/webmin/wuftpd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/wuftpd/config

# XINETD
%files xinetd -f xinetd.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/webmin/xinetd
%dir %{_datadir}/webmin/xinetd
%attr(755,root,root) %{_datadir}/webmin/xinetd/*.cgi
%doc %{_datadir}/webmin/xinetd/CHANGELOG
%{_datadir}/webmin/xinetd/images
%{_datadir}/webmin/xinetd/module.info
%{_datadir}/webmin/xinetd/config
%{_datadir}/webmin/xinetd/config.info
%{_datadir}/webmin/xinetd/*-*.pl
%{_datadir}/webmin/xinetd/*_*.pl
%config(noreplace) %{_sysconfdir}/webmin/xinetd/config

# THEMES
%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/webmin/caldera
%attr(755,root,root) %{_datadir}/webmin/caldera/*.cgi
%dir %{_datadir}/webmin/mscstyle3
%attr(755,root,root) %{_datadir}/webmin/mscstyle3/*.cgi
%attr(755,root,root) %{_datadir}/webmin/mscstyle3/*.pl
%{_datadir}/webmin/caldera/*[^i]
%{_datadir}/webmin/mscstyle3/*[^.][^.]??
%{_datadir}/webmin/mscstyle3/acl/images/icon.gif
%{_datadir}/webmin/mscstyle3/man/images/icon.gif
%{_datadir}/webmin/mscstyle3/net/images/icon.gif
%{_datadir}/webmin/mscstyle3/pam/images/icon.gif
%{_datadir}/webmin/mscstyle3/ssh/images/icon.gif

# SOURCES
%files src
%defattr(644,root,root,755)
%dir %{_datadir}/webmin/file/*.java

%include        /usr/lib/rpm/macros.perl
Summary:	Webmin - web-based administration	
Summary(pl):	Webmin - administracja przez WWW
Name:		webmin
Version:	0.79
Release:	1
License:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}-miniserv.conf
Patch0:		%{name}-PLD.patch
Url:		http://www.webmin.com/webmin/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Webmin is a web-based interface for system administration for Unix.
Using any browser that supports tables and forms, you can setup user
accounts, Apache, internet services, DNS, file sharing and so on.

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

%preun
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/webmin ]; then
                /etc/rc.d/init.d/webmin stop
        fi
        /sbin/chkconfig	--del webmin
fi

%files
%doc LICENCE.gz
%{_datadir}/webmin
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/webmin
%attr(750,root,root) %{_sysconfdir}/webmin
/var/log/webmin

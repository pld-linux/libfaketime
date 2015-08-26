Summary:	Report faked system time
Name:		libfaketime
Version:	0.9.6
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://www.code-wizards.com/projects/libfaketime/%{name}-%{version}.tar.gz
# Source0-md5:	f522f899d65a057ad69cff9896c75f78
URL:		http://www.code-wizards.com/projects/libfaketime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FakeTime Preload Library - report faked system time to programs without having
to change the system-wide time.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	LIBDIRNAME=/%{_lib}/faketime \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIRNAME=/%{_lib}/faketime \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/faketime
%dir %{_libdir}/faketime
%attr(755,root,root) %{_libdir}/faketime/%{name}*.so.1
%{_mandir}/man1/faketime.1*

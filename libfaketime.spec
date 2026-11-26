Summary:	Report faked system time
Name:		libfaketime
Version:	0.9.14
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://github.com/wolfcw/libfaketime/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0-md5:	e03fea5246b7dd07b5d9c43396e9b65d
URL:		https://github.com/wolfcw/libfaketime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FakeTime Preload Library - report faked system time to programs without having
to change the system-wide time.

%prep
%setup -q

%build
%{__make} \
	FAKETIME_COMPILE_CFLAGS="%{rpmcflags}" \
	FAKETIME_LINK_FLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix} \
	LIBDIRNAME=/%{_lib}/faketime \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIRNAME=/%{_lib}/faketime \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/faketime

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/faketime
%dir %{_libdir}/faketime
%attr(755,root,root) %{_libdir}/faketime/%{name}*.so.1
%{_mandir}/man1/faketime.1*

Name:		bonnie++
Version:	1.03e
Release:	1%{?dist}
Summary:	Benchmark suite

Group:		Development/Tools
License:	GPLv2
URL:		http://www.coker.com.au/bonnie++/
Source0:	%{name}-%{version}.tgz
Patch0: 	0001-Add-support-for-DESTDIR-to-Makefile.patch

%description
Bonnie++ is a benchmark suite aimed at performing a number of simple
hard drive and file system performance tests.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -v -f -i
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%defattr(-,root,root,-)
%doc copyright.txt
%{_bindir}/bon_csv2html
%{_bindir}/bon_csv2txt
%{_sbindir}/bonnie++
%{_sbindir}/zcav
%doc %{_mandir}/man1/*
%doc %{_mandir}/man8/*

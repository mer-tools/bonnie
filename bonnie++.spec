Name:		bonnie++
Version:	1.03e
Release:	1%{?dist}
Summary:	benchmark suite

Group:		System/Software
License:	GPLv2
URL:		http://www.coker.com.au/bonnie++/
Source0:	%{name}-%{version}.tgz

%description
%{summary}.

%prep
%setup -q

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
%doc %{_mandir}/*

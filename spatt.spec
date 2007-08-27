
Summary: A set of programs for performing statistics on words or  patterns
Name: spatt
Version: 1.2.2
Release: %mkrel 2
Source0: http://stat.genopole.cnrs.fr/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: Sciences/Biology
Url: http://stat.genopole.cnrs.fr/%{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gsl-devel gcc gcc-c++
BuildRequires: gcc-gfortran

%description
SPATT provides a set of programs performing statistical analysis of
words or patterns in biological sequences.


%prep

%setup -q

%build

export F77=gfortran
%configure

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man*/*
%doc AUTHORS COPYING README NEWS




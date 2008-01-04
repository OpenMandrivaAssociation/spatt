Summary:	A set of programs for performing statistics on words or  patterns
Name:		spatt
Version:	1.2.2
Release:	%mkrel 2
Source0:	http://stat.genopole.cnrs.fr/%{name}/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Sciences/Biology
URL:		http://stat.genopole.cnrs.fr/%{name}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gsl-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran

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
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man*/*
%doc AUTHORS README NEWS


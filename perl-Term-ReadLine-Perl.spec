%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadLine-Perl
Summary:	Term::ReadLine::Gnu Perl module
Name:		perl-Term-ReadLine-Perl
Version:	1.0203
Release:	0.1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec5b186a324e5cc29256e142b1b1f17d
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Term::ReadLine::Perl module.

This is a quick implementation of the minimal interface to Readline
libraries. The implementation is made in Perl (mostly) by Jeffrey
Friedl. The only thing this library does is to make it conformant (and
add some minimal changes, like using Term::ReadKey if present, and
correct work under xterm).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Term/ReadLine/*.pm

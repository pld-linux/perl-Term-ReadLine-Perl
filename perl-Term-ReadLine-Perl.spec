#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# interactive
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadLine-Perl
Summary:	Term::ReadLine::Perl - minimal interface to Readline libraries
Summary(pl.UTF-8):   Term::ReadLine::Perl - minimalny interfejs do bibliotek Readline
Name:		perl-Term-ReadLine-Perl
Version:	1.0302
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b68fca52e071e5307670519609ab269c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Term-ReadKey
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ReadLine::Perl module is a quick implementation of the minimal
interface to Readline libraries.  The implementation is made in Perl
(mostly) by Jeffrey Friedl.  The only thing this library does is to
make it conformant (and add some minimal changes, like using
Term::ReadKey if present, and correct work under xterm).

%description -l pl.UTF-8
Moduł Term::ReadLine::Perl jest szybką implementacją minimalnego
interfejsu do bibliotek Readline. Implementacja w Perlu została w
większości wykonana przez Jeffreya Friedla. Jedyną rzeczą, jaką robi
ta biblioteka, jest bycie zgodnym (i dodanie pewnych minimalnych
zmian, w rodzaju używania Term::ReadKey jeśli istnieje oraz poprawnej
pracy na xtermie).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/Term/ReadLine/*.pm

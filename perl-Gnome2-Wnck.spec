#
# Conditional build:               
%bcond_with     tests   # perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Wnck
Summary:	Perl bindings for the Window Navigator Construction Kit library
Summary(pl):	Dowi±zania perla dla biblioteki Window Navigator Construction Kit
Name:		perl-%{pnam}
Version:	0.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	dfd60b932dc6302aeec762083e7d65f8
URL:		http://gtk2-perl.sf.net/
BuildRequires:	libwnck-devel 
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Wnck module allows a perl developer to use the Window Navigator
Construction Kit library (libwnck for short) to write tasklists and
pagers.

%description -l pl
Modu³ Wnck pozwala programistom perlowym na u¿ywanie biblioteki
Window Navigator Construction Kit (w skrócie libwnck) do tworzenia
list okien i prze³±czników obszarów roboczych.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"
	
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorarch}/auto/Gnome2/Wnck
%dir %{perl_vendorarch}/Gnome2/Wnck
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Wnck/*.so
%{perl_vendorarch}/auto/Gnome2/Wnck/*.bs
%{perl_vendorarch}/Gnome2/Wnck/Install/*
%{perl_vendorarch}/Gnome2/*.pm
%{_mandir}/man3/*

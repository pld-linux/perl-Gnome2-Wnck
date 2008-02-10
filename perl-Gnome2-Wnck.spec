#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gnome2-Wnck
Summary:	Perl bindings for the Window Navigator Construction Kit library
Summary(pl.UTF-8):	Dowiązania Perla dla biblioteki Window Navigator Construction Kit
Name:		perl-Gnome2-Wnck
Version:	0.14
Release:	3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	653d5e6c4a950cc89913b5adceac8bd1
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libwnck-devel >= 2.15.92
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.132
BuildRequires:	perl-Gtk2 >= 1.133
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.132
Requires:	perl-Gtk2 >= 1.133
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Wnck module allows a perl developer to use the Window Navigator
Construction Kit library (libwnck for short) to write tasklists and
pagers.

%description -l pl.UTF-8
Moduł Wnck pozwala programistom perlowym na używanie biblioteki Window
Navigator Construction Kit (w skrócie libwnck) do tworzenia list okien
i przełączników obszarów roboczych.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Wnck/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{perl_vendorarch}/auto/Gnome2/Wnck
%dir %{perl_vendorarch}/Gnome2/Wnck
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Wnck/*.so
%{perl_vendorarch}/auto/Gnome2/Wnck/*.bs
%{perl_vendorarch}/Gnome2/Wnck/Install
%{perl_vendorarch}/Gnome2/*.pm
%{_mandir}/man3/*

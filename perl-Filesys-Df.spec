#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Filesys-Df
Version  : 0.92
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/I/IG/IGUTHRIE/Filesys-Df-0.92.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IG/IGUTHRIE/Filesys-Df-0.92.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfilesys-df-perl/libfilesys-df-perl_0.92-6.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Filesys-Df-license = %{version}-%{release}
Requires: perl-Filesys-Df-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
INSTALL
TO INSTALL RUN:

perl Makefile.PL
make
make test
make install
During the build process, the makefile will try to figure out which
system calls to use to obtain filesystem information. It will look
for statvfs() first via the Config module and a include directory
search. If it locates statvfs(), it will assume the system also has
fstatvfs(). If it cannot find statvfs(), it will then begin the same
search for statfs(). If statfs() is found it will assume fstatfs()
is also available.

%package dev
Summary: dev components for the perl-Filesys-Df package.
Group: Development
Provides: perl-Filesys-Df-devel = %{version}-%{release}
Requires: perl-Filesys-Df = %{version}-%{release}

%description dev
dev components for the perl-Filesys-Df package.


%package license
Summary: license components for the perl-Filesys-Df package.
Group: Default

%description license
license components for the perl-Filesys-Df package.


%package perl
Summary: perl components for the perl-Filesys-Df package.
Group: Default
Requires: perl-Filesys-Df = %{version}-%{release}

%description perl
perl components for the perl-Filesys-Df package.


%prep
%setup -q -n Filesys-Df-0.92
cd %{_builddir}
tar xf %{_sourcedir}/libfilesys-df-perl_0.92-6.debian.tar.xz
cd %{_builddir}/Filesys-Df-0.92
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Filesys-Df-0.92/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Filesys-Df
cp %{_builddir}/Filesys-Df-0.92/deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Filesys-Df/767e484aafbf54590d24f7c78eec1b0fe8ed85e7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Filesys::Df.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Filesys-Df/767e484aafbf54590d24f7c78eec1b0fe8ed85e7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Filesys/Df.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/Filesys/Df/Df.so

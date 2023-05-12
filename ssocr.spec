#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : ssocr
Version  : 2.23.0
Release  : 8
URL      : https://github.com/auerswal/ssocr/archive/v2.23.0/ssocr-2.23.0.tar.gz
Source0  : https://github.com/auerswal/ssocr/archive/v2.23.0/ssocr-2.23.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ssocr-bin = %{version}-%{release}
Requires: ssocr-license = %{version}-%{release}
Requires: ssocr-man = %{version}-%{release}
BuildRequires : imlib2-dev
BuildRequires : pkgconfig(x11)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Seven Segment Optical Character Recognition or ssocr for short is a
program to recognize digits of a seven segment display. An image of one
row of digits is used for input and the recognized number is written
to the standard output. The program runs on GNU/Linux (some GNU/Linux
distributions provide an ssocr package), FreeBSD (available as a port
as well), Mac OS X (Homebrew can be used to install the library Imlib2,
used by ssocr), and even on Windows (using Cygwin). ssocr should work
on any UNIX-like or POSIX compatible operating system.

%package bin
Summary: bin components for the ssocr package.
Group: Binaries
Requires: ssocr-license = %{version}-%{release}

%description bin
bin components for the ssocr package.


%package doc
Summary: doc components for the ssocr package.
Group: Documentation
Requires: ssocr-man = %{version}-%{release}

%description doc
doc components for the ssocr package.


%package license
Summary: license components for the ssocr package.
Group: Default

%description license
license components for the ssocr package.


%package man
Summary: man components for the ssocr package.
Group: Default

%description man
man components for the ssocr package.


%prep
%setup -q -n ssocr-2.23.0
cd %{_builddir}/ssocr-2.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683916744
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  -e PREFIX=/usr


%install
export SOURCE_DATE_EPOCH=1683916744
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ssocr
cp %{_builddir}/ssocr-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ssocr/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ssocr

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ssocr/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ssocr/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ssocr.1.gz

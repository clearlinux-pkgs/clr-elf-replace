#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-elf-replace
Version  : 16
Release  : 15
URL      : http://localhost/cgit/projects/clr-elf-replace/snapshot/clr-elf-replace-16.tar.xz
Source0  : http://localhost/cgit/projects/clr-elf-replace/snapshot/clr-elf-replace-16.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-elf-replace-libexec = %{version}-%{release}
Requires: clr-elf-replace-license = %{version}-%{release}
BuildRequires : glibc-staticdev

%description
No detailed description available

%package libexec
Summary: libexec components for the clr-elf-replace package.
Group: Default
Requires: clr-elf-replace-license = %{version}-%{release}

%description libexec
libexec components for the clr-elf-replace package.


%package license
Summary: license components for the clr-elf-replace package.
Group: Default

%description license
license components for the clr-elf-replace package.


%prep
%setup -q -n clr-elf-replace-16
cd %{_builddir}/clr-elf-replace-16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660080426
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1660080426
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-elf-replace
cp %{_builddir}/clr-elf-replace-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/clr-elf-replace/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/clr-elf-replace

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-elf-replace/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%global qt5_min_version 5.15.2
%global kf5_min_version 5.70.0

Name:       opt-maui-mauiman
Version:    1.0.1
Release:    1
Summary:    Maui Manager Library
License:    GPL-3.0-or-later
URL:        https://mauikit.org/
Source:     mauiman-%{version}.tar.xz
Requires:   opt-qt5-qtbase >= %{qt5_min_version}
BuildRequires:  cmake >= 3.16
BuildRequires:  opt-extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-qt5-qtbase-devel >= %{qt5_min_version}
%{?opt_kf5_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^libMauiMan.*$

%description
%{summary}.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
export QTDIR=%{_opt_qt5_prefix}

mkdir -p build
pushd build

%_opt_cmake_kf5 .. \
    -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/MauiManServer
%{_datadir}/dbus-1/services/org.mauiman.server.service
%{_opt_kf5_libdir}/libMauiMan.so

%files devel
%{_opt_kf5_includedir}/MauiMan
%{_opt_kf5_libdir}/cmake/MauiMan

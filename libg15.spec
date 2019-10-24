%define major 1
%define libname %mklibname g15_ %{major}
%define libname_devel %mklibname g15 -d
%define libname_static_devel %mklibname g15 -d -s

Name:           libg15
Version:        1.2.7
Release:        7
Summary:        Library to control logitech G15 keyboards
License:        GPLv2+
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source:         http://downloads.sourceforge.net/g15tools/libg15-%{version}.tar.bz2
BuildRequires:  pkgconfig(libusb)

%description
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname}
Summary:        Controls the G15 keyboard and LCD
Group:          System/Libraries
Provides:       g15 = %{version}-%{release}

%description -n %{libname}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_devel}
Summary:        Controls the G15 keyboard and LCD
Group:          Development/C
Provides:       g15-devel = %{version}-%{release}
Requires:       g15 = %{version}-%{release}

%description -n %{libname_devel}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%prep
%setup -q

%build
# fix build on aarch64
autoreconf -vfi

%configure2_5x --disable-static
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libg15.so.%{major}
%{_libdir}/libg15.so.%{major}.*

%files -n %{libname_devel}
%{_includedir}/*
%{_libdir}/libg15.so

%dfine major 1
%define libname %mklibname g15_ %{major}
%define libname_devel %mklibname g15 -d
%define libname_static_devel %mklibname g15 -d -s

Name:		libg15
Version:	1.2.7
Release:	5
Summary:	Library to control logitech G15 keyboards
License:	GPLv2+
Group:		System/Libraries
URL:		http://g15tools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/g15tools/libg15-%{version}.tar.bz2
BuildRequires:	pkgconfig(libusb)

%description
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname}
Summary:		Controls the G15 keyboard and LCD
Group:			System/Libraries
Provides:		g15 = %{version}-%{release}

%description -n %{libname}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_devel}
Summary:		Controls the G15 keyboard and LCD
Group:			Development/C
Provides:		g15-devel = %{version}-%{release}
Requires:		g15 = %{version}-%{release}

%description -n %{libname_devel}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_static_devel}
Summary:		Controls the G15 keyboard and LCD
Group:			Development/C
Provides:		g15-static-devel = %{version}-%{release}
Requires:		g15-devel = %{version}-%{release}

%description -n %{libname_static_devel}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{makeinstall_std}


%files -n %{libname}
%{_libdir}/libg15.so.%{major}*

%files -n %{libname_devel}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_includedir}/*
%{_libdir}/libg15.so

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/lib*.a



%define libname %mklibname g15_ 1
%define libname_devel %mklibname g15 -d
%define libname_static_devel %mklibname g15 -d -s

Name:           libg15
Version:        1.2.6
Release:        %mkrel 2
Summary:        Library to control logitech G15 keyboards
License:        GPL
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source:         http://downloads.sourceforge.net/g15tools/libg15-%{version}.tar.bz2
BuildRequires:  libusb-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname}
Summary:        Controls the G15 keyboard and LCD
Group:          System/Libraries

%description -n %{libname}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_devel}
Summary:        Controls the G15 keyboard and LCD
Group:          Development/C
Provides:       g15-devel = %{version}-%{release}

%description -n %{libname_devel}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_static_devel}
Summary:        Controls the G15 keyboard and LCD
Group:          Development/C
Provides:       g15-static-devel = %{version}-%{release}

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
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libg15.so.*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/lib*.la
%{_libdir}/libg15.so

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/lib*.a

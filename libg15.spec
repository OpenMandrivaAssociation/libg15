%define libname %mklibname g15_ 1
%define libname_devel %mklibname g15 -d
%define libname_static_devel %mklibname g15 -d -s

Name:           libg15
Version:        1.2.7
Release:        3
Summary:        Library to control logitech G15 keyboards
License:        GPLv2+
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source:         http://downloads.sourceforge.net/g15tools/libg15-%{version}.tar.bz2
BuildRequires:  libusb-devel

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

%package -n %{libname_static_devel}
Summary:        Controls the G15 keyboard and LCD
Group:          Development/C
Provides:       g15-static-devel = %{version}-%{release}
Requires:       g15-devel = %{version}-%{release}

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
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libg15.so.*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/libg15.so

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/lib*.a


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2011.0
+ Revision: 609747
- rebuild

* Wed Dec 30 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.7-1mdv2010.1
+ Revision: 484225
- new version 1.2.7
- fix license tag

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 1.2.6-9mdv2010.0
+ Revision: 439068
- rebuild for new libusb

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-7mdv2009.0
+ Revision: 248647
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.2.6-5mdv2008.1
+ Revision: 163890
- fix Requires
- Provides: g15 = %%{version}-%%{release}

* Thu Feb 07 2008 David Walluck <walluck@mandriva.org> 1.2.6-3mdv2008.1
+ Revision: 163354
- add more documentation
- fix wrong g15-devel provide
- place .la file in devel package

* Thu Feb 07 2008 David Walluck <walluck@mandriva.org> 1.2.6-1mdv2008.1
+ Revision: 163350
- import libg15



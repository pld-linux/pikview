Summary:	PikView is an image viewer
Summary(pl):	PikView jest przegl±dark± plików graficznych
Name:		pikview
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/pikview/%{name}-%{version}.tar.gz
# Source0-md5:	130fb09005cf6d04ded879570c8ba126
URL:		http://pikview.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	gdbm-devel
BuildRequires:	kdelibs-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
PikView is an image viewer which uses the KDE libraries. PikView can
read the following image types: png, jpeg, tiff, gif, netpbm (and via
the ImageMagick library - eps, pict, dcx, pcx, mif, bmp, viff, pnm)
Also supported are the following features: preloading, zooming,
thumbnails, rapid image filing, fullscreen, printing, slideshow.

%description -l pl
PikView jest przegl±dark± plików graficznych u¿ywaj±c± bibliotek KDE.
Mo¿e czytaæ pliki: png, jpeg, tiff, gif, netpbm (oraz poprzez
bibliotekê ImageMagick: eps, pict, dcx, pcx, mif, bmp, viff, pnm).
Poza tym ma mo¿liwo¶æ: pre³adowania, powiêkszania, thumbnaili,
wype³niania obrazków, przegl±dania pe³noekranowego, drukowania,
pokazywania obrazków jako slajdów.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG}"
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpikview.so.*.*
%{_datadir}/apps/pikview
%{_applnkdir}/Graphics/pikview.desktop
%{_pixmapsdir}/*/*/apps/*

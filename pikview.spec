Summary:	PikView is an image viewer
Summary(pl):	PikView jest przegl�dark� plik�w graficznych
Name:		pikview
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(cs):	X11/Aplikace/Multim�dia
Group(da):	X11/Programmer/Multimedie
Group(de):	X11/Applikationen/Multimedien
Group(es):	X11/Aplicaciones/Multimedia
Group(fr):	X11/Applications/Multim�dia
Group(is):	X11/Forrit/Margmi�lun
Group(it):	X11/Applicazioni/Multimedia
Group(ja):	���ץꥱ�������/�ޥ����ǥ���
Group(no):	X11/Programmer/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Group(pt):	X11/Aplica��es/Multim�dia
Group(ru):	X11/����������/�����������
Group(sl):	X11/Programi/Ve�predstavnost
Group(sv):	X11/Till�mpningar/Multimedia
Group(uk):	X11/�������Φ ��������/��������Ħ�
Source0:	ftp://download.sourceforge.net/pub/sourceforge/pikview/%{name}-%{version}.tar.gz
URL:		http://pikview.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	gdbm-devel
BuildRequires:	kdelibs-devel >= 2.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
PikView is an image viewer which uses the KDE libraries. PikView can
read the following image types: png, jpeg, tiff, gif, netpbm (and via
the ImageMagick library - eps, pict, dcx, pcx, mif, bmp, viff, pnm)
Also supported are the following features: preloading, zooming,
thumbnails, rapid image filing, fullscreen, printing, slideshow.

%description -l pl
PikView jest przegl�dark� plik�w graficznych u�ywaj�c� bibliotek KDE.
Mo�e czyta� pliki: png, jpeg, tiff, gif, netpbm (oraz poprzez
bibliotek� ImageMagick: eps, pict, dcx, pcx, mif, bmp, viff, pnm).
Poza tym ma mo�liwo��: pre�adowania, powi�kszania, thumbnaili,
wype�niania obrazk�w, przegl�dania pe�noekranowego, drukowania,
pokazywania obrazk�w jako slajd�w.

%prep
rm -rf $RPM_BUILD_ROOT

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

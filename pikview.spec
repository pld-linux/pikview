Summary:	PikView is an image viewer
Summary(pl):	PikView jest przegl±dark± plików graficznych
Name:		pikview
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/pikview/%{name}-%{version}.tar.gz
URL:		http://pikview.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libwmf-devel
BuildRequires:	libxml2-devel
BuildRequires:	XFree86-DPS-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG}"
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
%defattr(644,root,root,755)

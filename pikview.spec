Summary:	PikView is an image viewer
Name:		pikview
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.sourceforge.net/pikview/%{name}-%{version}.tar.gz
URL:		http://pikview.sourceforge.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
PikView is an image viewer which uses the KDE libraries.  PikView can read the
following image types: png, jpeg, tiff, gif, netpbm (and via the ImageMagick
library - eps, pict, dcx, pcx, mif, bmp, viff, pnm) Also supported are the
following features: preloading, zooming, thumbnails, rapid image filing,
fullscreen, printing, slideshow.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure \

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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

%define name       pikview
%define version    0.8.2
%define qtdir      /usr/lib/qt-1.44
%define kdeprefix  /usr
%define kderelease 1rh

Name: %{name}
Summary: PikView is an image viewer
Version: %{version}
Release: %{kderelease}
Serial: 1
Source: %{name}-%{version}.tar.gz
License: GPL
URL: http://pikview.sourceforge.net/
Group: Applications/Multimedia
Packager: Andrew Richards <ajr@users.sourceforge.net>
Buildroot: /tmp/%{name}-buildroot
Prefix: %{kdeprefix}

%description
PikView is an image viewer which uses the KDE libraries.
PikView can read the following image types: png, jpeg, tiff, gif, netpbm
(and via the ImageMagick library - eps, pict, dcx, pcx, mif, bmp, viff, pnm)
Also supported are the following features: preloading, zooming, thumbnails,
rapid image filing, fullscreen, printing, slideshow.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
export KDEDIR=%{kdeprefix} export QTDIR=%{qtdir}
./configure \
	--prefix=%{kdeprefix} \
	--exec_prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT

make CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG"

%install
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix} \
	exec_prefix=$RPM_BUILD_ROOT%{kdeprefix}

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

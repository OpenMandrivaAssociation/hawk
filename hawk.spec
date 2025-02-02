%define name hawk
%define version 2.1
%define release 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Web-Album generator
License:        CeCILL
Group:          Graphics
URL:            https://tableaux.levier.org/download.html
Source0:         http://tableaux.levier.org/package/%{name}-%{version}.tar.gz
source1:				.abf.yml
buildrequires:	pkgconfig(libpcre)


%description
Yet another Web-Album generator. Highlights:

  * automatic rotation of portrait images thanks to information
    put by digital camera in .jpg file (EXIF)
  * immediate display of images (preloading in browser)
  * keep position of "next/previous" hyperlinks in browser
    between images
  * full video support (including thumbnailing)
  * clever use of the whole space of a typical browser window
    (the need to scroll portrait images is stupid)
  * themability
  * sub-albums support
  * remember your preferred size of thumbnails accross sub-albums
  * multi-processor support to speed up thumbnails generation
  * smooth integration of panoramic images in thumbnails pages
  * multi-languages web-album navigation (navigation links are
    automatically shown in user's language)
  * a GUI to input captions, rotate, reorder and remove
    images FAST (extensive use of keyboard shortcuts)
  * another GUI to classify photos and videos in a powerful manner

%prep
%setup -q
chmod go+r *

%build
%make CFLAGS="%optflags"

%install
install -d -m 755 %buildroot%{_bindir}
install -d -m 755 %buildroot%{_mandir}/man1

install -m 755 hawk %buildroot%{_bindir}
install -m 644 hawk.1 %buildroot%{_mandir}/man1

%files
%defattr(-, root, root)
%doc LICENSE
%{_bindir}/hawk
%{_mandir}/man1/hawk.1*



%changelog
* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.1
+ Revision: 303788
- import hawk


* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.1
- first mdv release 

%define abi_package %{nil}
%global commit0 192d1d34eb3668fa27f433e96036340e1e5077a0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Summary:        Digital VCR and streaming server
Name:           ffmpeg
Version:        4.2.2
Release:        8%{?dist}
License:        GPLv2+
URL:            http://ffmpeg.org/
Source0:        https://git.ffmpeg.org/gitweb/ffmpeg.git/snapshot/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        ffmpeg.appdata.xml
# forces the buffers to be flushed after a drain has completed. Thanks to jcowgill
#Patch0:		buffer_flush.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  gmp-dev
BuildRequires:  bzip2-dev
BuildRequires:  fdk-aac-free-dev
BuildRequires:  fontconfig-dev
BuildRequires:  freetype-dev
BuildRequires:  gnutls-dev
BuildRequires:  gsm-dev
BuildRequires:  libmp3lame-dev
BuildRequires:  jack2-dev
BuildRequires:  ladspa_sdk-dev
BuildRequires:  libass-dev
BuildRequires:  libgcrypt-devel
BuildRequires:  mesa-dev
BuildRequires:  libmodplug-dev
BuildRequires:  v4l-utils-dev
BuildRequires:  libvorbis-dev
BuildRequires:  libvpx-dev
BuildRequires:  mediasdk-dev
BuildRequires:  libXvMC-dev
BuildRequires:  libva-dev
BuildRequires:  yasm
BuildRequires:  libwebp-dev
BuildRequires:  libjpeg-turbo-dev
BuildRequires:  opus-dev
BuildRequires:  pulseaudio-dev
BuildRequires:  perl-Pod-POM-man
BuildRequires:  SDL2-dev
BuildRequires:  snappy-dev
BuildRequires:  speex-dev
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  wavpack-dev
BuildRequires:  x264-dev
BuildRequires:  x265-dev
BuildRequires:  zlib-dev
BuildRequires:	libdrm-dev
BuildRequires:	alsa-lib-dev
BuildRequires:  rtmpdump-dev
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  appstream-glib-dev

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}
Recommends:	fdk-aac-free

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}

%package     -n libavdevice
Summary:        Special devices muxing/demuxing library

%description -n libavdevice
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package        dev
Summary:        Development package for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       libavdevice%{_isa} = %{version}-%{release}
Requires:       pkg-config

%description    dev
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

%prep
%setup -n %{name}-%{shortcommit0} 

# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure
mkdir -p _doc/examples
cp -pr doc/examples/{*.c,Makefile,README} _doc/examples/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571938166
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "

./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --docdir=%{_docdir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --arch=%{_target_cpu} \
    --extra-ldflags='-ldl' \
    --enable-vaapi \
    --enable-bzlib \
    --enable-libdrm \
    --enable-fontconfig \
    --enable-gcrypt \
    --enable-gmp --enable-version3 \
    --enable-gnutls \
    --enable-ladspa \
    --enable-libass \
    --enable-libfdk-aac --enable-nonfree \
    --enable-libjack \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libmp3lame \
    --enable-opengl \
    --enable-libopus \
    --enable-libpulse \
    --enable-libsnappy \
    --enable-libspeex \
    --enable-libvorbis \
    --enable-libv4l2 \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-avfilter \
    --enable-avresample \
    --enable-postproc \
    --enable-pthreads \
    --enable-librtmp \
    --enable-libmfx \
    --disable-static \
    --enable-shared \
    --enable-gpl \
    --disable-debug \
    --disable-stripping \
    --shlibdir=%{_libdir} \
    --enable-libfdk-aac --enable-nonfree 

#   --optflags="%%{optflags}" \
#   --cpu=%{_target_cpu} \
#   --enable-runtime-cpudetect \



%make_build V=0
make documentation V=0
make alltools V=0

%install
%make_install V=0
rm -rf %{buildroot}%{_datadir}/%{name}/examples

# Appdata
mkdir -p %{buildroot}/%{_datadir}/{applications,metainfo}
install -Dm 0644 %{SOURCE1} %{buildroot}/usr/share/metainfo/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}/usr/share/metainfo/*.appdata.xml

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post -n libavdevice -p /sbin/ldconfig

%postun -n libavdevice -p /sbin/ldconfig


%files
%doc COPYING.* CREDITS README.md 
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_datadir}/%{name}
%{_mandir}/man3/*.3*
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
%{_datadir}/metainfo/%{name}.appdata.xml

%files libs
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice.so.*
%exclude %{_mandir}/man3/libavdevice.3*

%files -n libavdevice
%{_libdir}/libavdevice.so.*
%{_mandir}/man3/libavdevice.3*

%files dev
%doc MAINTAINERS doc/APIchanges doc/*.txt
%doc _doc/examples
%doc %{_docdir}/%{name}/*.html
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so



%changelog
# based on https://github.com/UnitedRPMs/ffmpeg
# and https://github.com/clearlinux-pkgs/not-ffmpeg

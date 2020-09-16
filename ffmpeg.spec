%define abi_package %{nil}
%global commit0 6b6b9e593dd4d3aaf75f48d40a13ef03bdef9fdb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Summary:      Digital VCR and streaming server
Name:           ffmpeg
Version:        4.3.1
Release:        1%{?dist}
License:        GPLv2+
URL:            http://ffmpeg.org/
Source0:        https://git.ffmpeg.org/gitweb/ffmpeg.git/snapshot/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        ffmpeg.appdata.xml
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  gmp-dev
BuildRequires:  bzip2-dev
BuildRequires:  fdk-aac-dev
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
BuildRequires:  libdrm-dev
BuildRequires:  alsa-lib-dev
BuildRequires:  rtmpdump-dev
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  appstream-glib-dev
BuildRequires:  libdav1d-dev
BuildRequires:  Vulkan-Loader-dev Vulkan-Loader 
BuildRequires:  Vulkan-Headers-dev Vulkan-Tools Vulkan-Headers
BuildRequires:  glslang-dev glslang
BuildRequires:  SPIRV-Tools SPIRV-Headers SPIRV-Tools-dev SPIRV-Headers-dev
BuildRequires:  lensfun-dev

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}
Recommends:	fdk-aac

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
sed -i "s|-lOSDependent||" configure
sed -i "s|-lOGLCompiler||" configure


%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "

./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --disable-doc \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --disable-error-resilience \
    --enable-pic \
    --enable-rdft \
    --enable-pixelutils \
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
    --enable-sdl2 \
    --enable-indev="v4l2" \
    --enable-outdev="sdl2" \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-avfilter \
    --enable-avresample \
    --enable-swscale \
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
    --enable-libfdk-aac --enable-nonfree \
    --enable-libdav1d \
    --enable-vulkan --enable-libglslang \
    --enable-liblensfun

make  %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/%{name}/examples

# Appdata
mkdir -p %{buildroot}/%{_datadir}/{applications,metainfo}
install -Dm 0644 %{SOURCE1} %{buildroot}/usr/share/metainfo/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}/usr/share/metainfo/*.appdata.xml

%post libs -p /usr/bin/ldconfig

%postun libs -p /usr/bin/ldconfig

%post -n libavdevice -p /usr/bin/ldconfig

%postun -n libavdevice -p /usr/bin/ldconfig


%files
%doc COPYING.* CREDITS README.md 
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml

%files libs
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice.so.*

%files -n libavdevice
%{_libdir}/libavdevice.so.*

%files dev
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so



%changelog
# based on https://github.com/UnitedRPMs/ffmpeg
# and https://github.com/clearlinux-pkgs/not-ffmpeg

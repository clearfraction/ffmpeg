%define abi_package %{nil}
%global commit0 7e0d640edf6c3eee1816b105c2f7498c4f948e74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        Digital VCR and streaming server
Name:           ffmpeg
Version:        4.4.1
Release:        102
License:        GPLv2+
URL:            http://ffmpeg.org
Source0:        https://git.ffmpeg.org/gitweb/ffmpeg.git/snapshot/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-filemap = %{version}-%{release}
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
BuildRequires:  dav1d-dev
BuildRequires:  Vulkan-Loader-dev Vulkan-Loader 
BuildRequires:  Vulkan-Headers-dev Vulkan-Tools Vulkan-Headers
BuildRequires:  glslang-dev glslang
BuildRequires:  SPIRV-Tools-dev SPIRV-Cross-dev
BuildRequires:  SVT-AV1-dev

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

%package        dev
Summary:        Development package for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       pkg-config

%description    dev
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}


%package filemap
Summary: filemap components for the ffmpeg package.
Group: Default

%description filemap
filemap components for the ffmpeg package.

%prep
%setup -n %{name}-%{shortcommit0}
# erase glslang flags from configure checks
sed -i "s|-lOSDependent||" configure
sed -i "s|-lOGLCompiler||" configure
sed -i "s|-lMachineIndependent||" configure
sed -i "s|-lGenericCodeGen||" configure
# AVX2 build
pushd ..
cp -a %{name}-%{shortcommit0} buildavx2
popd


%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "

./configure --disable-static --extra-ldflags='-ldl' \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --shlibdir=%{_libdir} \
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
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-avfilter \
    --enable-swscale \
    --enable-postproc \
    --enable-pthreads \
    --enable-librtmp \
    --enable-libmfx \
    --disable-static \
    --enable-shared \
    --enable-gpl \
    --disable-debug \
    --disable-doc \
    --enable-libfdk-aac --enable-nonfree \
    --enable-libdav1d \
    --enable-vulkan --enable-libglslang --enable-libsvtav1
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
./configure --disable-static --extra-ldflags='-ldl' \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --shlibdir=%{_libdir} \
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
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-avfilter \
    --enable-swscale \
    --enable-postproc \
    --enable-pthreads \
    --enable-librtmp \
    --enable-libmfx \
    --disable-static \
    --enable-shared \
    --enable-gpl \
    --disable-debug \
    --disable-doc \
    --enable-libfdk-aac --enable-nonfree \
    --enable-libdav1d \
    --enable-vulkan --enable-libglslang --enable-libsvtav1
make  %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
rm -rf %{buildroot}/usr/share/examples
%make_install

%post libs -p /usr/bin/ldconfig

%postun libs -p /usr/bin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_datadir}/%{name}

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/libavdevice.so.*

%files dev
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-ffmpeg
/usr/share/clear/optimized-elf/bin*
/usr/share/clear/optimized-elf/lib*


%changelog
# based on https://github.com/UnitedRPMs/ffmpeg
# and https://github.com/clearlinux-pkgs/not-ffmpeg

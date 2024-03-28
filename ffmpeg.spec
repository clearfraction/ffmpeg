%global gitdate 20231003
%global commit0 ea3d24bbe3c58b171e55fe2151fc7ffaca3ab3d2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        Digital VCR and streaming server
Name:           ffmpeg
Version:        6.1.1
Release:        %{gitdate}
License:        GPLv2+
URL:            http://ffmpeg.org
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Requires:       %{name}-libs = %{version}-%{release}
#Requires:       %%{name}-filemap = %%{version}-%%{release}
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
BuildRequires:  SPIRV-Tools-dev SPIRV-Cross-dev SPIRV-Headers-dev
BuildRequires:  SVT-AV1-dev
BuildRequires:  libplacebo-dev
BuildRequires:  zimg-dev
BuildRequires:  xvidcore-dev
BuildRequires:  vid.stab-dev
BuildRequires:  libtheora-dev
BuildRequires:  libssh-dev libssh2-dev
BuildRequires:  srt-dev
BuildRequires:  speex-dev
BuildRequires:  librsvg-dev
BuildRequires:  libopenmpt-dev
BuildRequires:  openjpeg-dev
BuildRequires:  libaom-dev
BuildRequires:  ladspa_sdk-dev


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

%prep
%setup -n %{name}-%{version}
# erase glslang flags from configure checks
sed -i "s|-lOSDependent||g" configure
sed -i "s|-lOGLCompiler||g" configure
sed -i "s|-lMachineIndependent||g" configure
sed -i "s|-lGenericCodeGen||g" configure
sed -i "s|-lSPIRV-Tools-opt||g" configure
sed -i "s|-lSPIRV-Tools||g" configure
sed -i "s|-lSPIRV||g" configure




%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export LDFLAGS="-Wl,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64,-rpath=/usr/lib64 "
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
./configure --disable-static --extra-ldflags='-ldl' \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --shlibdir=%{_libdir} \
    --enable-pixelutils \
    --extra-ldflags='-ldl' \
    --enable-vaapi \
    --enable-bzlib \
    --enable-libdrm \
    --enable-fontconfig \
    --enable-gcrypt \
    --enable-gmp --enable-version3 \
    --enable-gnutls \
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
    --enable-vulkan --enable-libglslang \
    --enable-libsvtav1 \
    --enable-ladspa \
    --enable-libaom \
    --enable-libopenjpeg \
    --enable-libopenmpt \
    --enable-librsvg \
    --enable-libspeex \
    --enable-libsrt \
    --enable-libssh \
    --enable-libtheora \
    --enable-libvidstab \
    --enable-libxcb \
    --enable-libzimg 
make  %{?_smp_mflags}

# --enable-libplacebo
%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/examples


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


%changelog
# based on https://github.com/UnitedRPMs/ffmpeg
# and https://github.com/clearlinux-pkgs/not-ffmpeg

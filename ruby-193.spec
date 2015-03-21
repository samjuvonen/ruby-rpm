%define rubyver         1.9.3
%define rubyminorver    p551

%define _prefix         /usr/local
%define _bindir         %{_prefix}/bin
%define _libdir         %{_prefix}/lib64
%define _includedir     %{_prefix}/include
%define _datadir        %{_prefix}/share

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        wfx2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ruby
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  db4-devel
BuildRequires:  gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  libffi-devel
BuildRequires:  libyaml-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel

Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        System ruby v1.9.3-p547
Group:          Development/Languages
Provides: ruby(abi) = 1.9
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems

%description
Ruby is the interpreted scripting language for quick
and easy object-oriented programming.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
#export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
autoconf

%configure \
  --prefix=%{_prefix} \
  --enable-shared \

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/erb
%{_bindir}/gem
%{_bindir}/irb
%{_bindir}/rake
%{_bindir}/rdoc
%{_bindir}/ruby
%{_bindir}/ri
%{_bindir}/testrb
%{_includedir}/ruby-1.9.1
%{_libdir}/libruby-static.a
%{_libdir}/libruby.so
%{_libdir}/libruby.so.1.9
%{_libdir}/libruby.so.1.9.1
%{_libdir}/pkgconfig/ruby-1.9.pc
%{_libdir}/ruby/1.9.1/
%{_libdir}/ruby/gems/1.9.1/
%{_datadir}/man/man1/erb.1
%{_datadir}/man/man1/irb.1
%{_datadir}/man/man1/rake.1
%{_datadir}/man/man1/ri.1
%{_datadir}/man/man1/ruby.1
%{_datadir}/ri/1.9.1/

%changelog

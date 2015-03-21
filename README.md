# Build Ruby RPM on EL7

This is a spec file to build a Ruby RPM on EL7. Currently for 1.9.3, which is
an old and unsupported ruby. Note that EL7 comes with ruby 2.0 and using a
version that gets security updates is a Good Thing.

## Get started

    yum install rpm-build redhat-rpm-config rpmdevtools mock

Create a user in group mock or add yourself to group mock and relogin. Do not
build RPMs as root.

## Create build environment

    rpmdev-setuptree
    mock --init

copy specs from this repo into ~/rpmbuild/SPECS/

## Get ruby sources

    git clone git@github.com:ruby/ruby.git
    cd ruby
    git checkout v1_9_3_547
    git archive --format=tar.gz --prefix=ruby-1.9.3-p547/ v1_9_3_547 >
        ~/rpmbuild/SOURCES/ruby-1.9.3-p547.tar.gz

## Build source RPM

    mock --buildsrpm --spec=./rpmbuild/SPECS/ruby193p547.spec \
        --sources=./rpmbuild/SOURCES

## Build binary RPM from the source RPM

    mock --no-clean --rebuild /var/lib/mock/epel-7-x86_64/result/ruby-1.9.3-p547.el7.src.rpm

Copy the RPMs from /var/lib/mock/ somewhere safe.

Note that Ruby 1.9 requires a pre-existing ruby to build. Installing the
default EL7 ruby-2.0 Works For Me - see BuildRequires. Also ruby 1.9.3 uses
directories like /1.9.1/ for some reason only dedicated rubyists can explain.
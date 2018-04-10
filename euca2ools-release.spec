Name:           euca2ools-release
Version:        3.4
Release:        2%{?dist}
Summary:        Euca2ools release files

License:        GPLv3
URL:            http://www.eucalyptus.com/

BuildArch:      noarch

Source0:        %{tarball_basedir}.tar.xz

%description
This package contains release files, such as yum configs and various
/etc files that define the Euca2ools release.


%prep
%setup -q -n %{tarball_basedir}


%build
./configure \
    --with-rpm-repository-url=%{rpm_repo_url}


%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cp -p euca2ools.repo $RPM_BUILD_ROOT/etc/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp -p RPM-GPG-KEY-euca2ools-release* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/


%files
/etc/pki/rpm-gpg/RPM-GPG-KEY-euca2ools-release*
%config(noreplace) /etc/yum.repos.d/euca2ools.repo


%changelog
* Tue Apr 10 2018 Steve Jones <steve.jones@appscale.com> - 3.4-2
- Updated for appscale euca2ools 3.4

* Tue Dec 13 2016 Garrett Holmstrom <gholms@hpe.com> - 3.4-1
- Updated for euca2ools 3.4

* Thu Oct 22 2015 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.3-1
- Updated for euca2ools 3.3

* Wed Jan 21 2015 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.2-1
- Updated for 3.2

* Fri May 23 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1-1
- Recreated from scratch

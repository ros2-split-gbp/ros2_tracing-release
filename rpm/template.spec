%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-tracetools-test
Version:        4.1.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tracetools_test package

License:        Apache 2.0
URL:            https://index.ros.org/p/tracetools_test/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-launch
Requires:       ros-humble-launch-ros
Requires:       ros-humble-tracetools-launch
Requires:       ros-humble-tracetools-read
Requires:       ros-humble-tracetools-trace
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-launch
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-tracetools-launch
BuildRequires:  ros-humble-tracetools-read
BuildRequires:  ros-humble-tracetools-trace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-mypy
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-ament-xmllint
%endif

%description
Utilities for tracing-related tests.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Nov 07 2022 Christophe Bedard <bedard.christophe@gmail.com> - 4.1.1-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Christophe Bedard <bedard.christophe@gmail.com> - 4.1.0-2
- Autogenerated by Bloom

* Tue Mar 29 2022 Christophe Bedard <bedard.christophe@gmail.com> - 4.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Christophe Bedard <bedard.christophe@gmail.com> - 4.0.0-2
- Autogenerated by Bloom


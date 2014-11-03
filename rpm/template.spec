Name:           ros-hydro-universal-robot
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS universal_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/universal_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-ur-bringup
Requires:       ros-hydro-ur-description
Requires:       ros-hydro-ur-driver
Requires:       ros-hydro-ur-gazebo
Requires:       ros-hydro-ur-kinematics
Requires:       ros-hydro-ur-msgs
Requires:       ros-hydro-ur10-moveit-config
Requires:       ros-hydro-ur5-moveit-config
BuildRequires:  ros-hydro-catkin

%description
Drivers, description, and utilities for Universal Robot Arms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Nov 03 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.0.5-0
- Autogenerated by Bloom


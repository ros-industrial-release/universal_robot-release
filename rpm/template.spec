Name:           ros-indigo-ur-gazebo
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS ur_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ur_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-effort-controllers
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-gazebo-ros-pkgs
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-ros-controllers
Requires:       ros-indigo-ur-description
BuildRequires:  ros-indigo-catkin

%description
Gazebo wrapper for the Universal UR5/10 robot arms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Sep 04 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.0.3-0
- Autogenerated by Bloom


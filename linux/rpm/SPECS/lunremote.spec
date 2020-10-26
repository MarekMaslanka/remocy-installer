Summary:    Low-lantency access to remote desktop
Name:       lunremote
Version:    0.0.1
Release:    0
Group:      Applications/Utils
License:    Proprietary
URL:        www.lunremote.com
Source0:    artifact.tar
Source1:    data.tar
Vendor:     Lunremote
BuildRequires: systemd-rpm-macros

%description
Lunremote allows one to view remotely and interact with real screen
(i.e. a display corresponding to a physical monitor, keyboard, and mouse)
for Linux, Windows and macOS. Lunremote is optimized for low lantency
and it's currently the fastest tool to remotly controlling desktop.

%define __requires_exclude libopenh264.so.5
%global debug_package %{nil}

%prep

%build

%install

# Not needed on Fedora but it is on some other distros
mkdir -p "%{buildroot}"

mkdir -p %{buildroot}/opt/lunremote
tar -xf %{SOURCE0} -C %{buildroot}/opt/lunremote/ --strip=1
tar -xf %{SOURCE1} -C %{buildroot}
chmod -R 755 %{buildroot}/usr/share/icons/

mkdir -p %{buildroot}/%{_bindir}/
ln -s /opt/lunremote/lunremote %{buildroot}/%{_bindir}/lunremote

%post
%systemd_post lunremote.service

# Setup icons
touch -c /usr/share/icons/hicolor
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
  gtk-update-icon-cache -tq /usr/share/icons/hicolor 2>/dev/null ||:
fi

# Setup desktop file
if command -v update-desktop-database >/dev/null 2>&1; then
  update-desktop-database -q /usr/share/applications 2>/dev/null ||:
fi

%preun
%systemd_preun lunremote.service

%postun
%systemd_postun_with_restart lunremote.service

%clean
rm -rf %{buildroot}

%files
/opt/lunremote/*
/usr/lib/systemd/system/lunremote.service
%{_bindir}/lunremote
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/menu/*

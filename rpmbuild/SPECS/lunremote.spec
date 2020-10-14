Summary:    Lunremote allow access to remote desktop
Name:       Lunremote
Version:    0.0.1
Release:    0
Group:      Applications/Utils
License:    Proprietary
URL:        www.lunremote.com
Source0:    artifact.tar
Vendor:     Lunremote

%description
Lunremote is the fastest application to access to remote desktop.

%prep

%setup -T -c

%build

%install

# Not needed on Fedora but it is on some other distros
mkdir -p "%{buildroot}"

mkdir -p %{buildroot}/opt/lunremote
tar -xf %{SOURCE0} -C %{buildroot}/opt/lunremote/ --strip=1

# Fix the location of the doc directory on OpenSUSE
%if 0%{?suse_version}
  mkdir -p "%{buildroot}/%{_defaultdocdir}"
  mv "%{buildroot}/usr/share/doc/%{name}" "%{buildroot}/%{_defaultdocdir}/%{name}" 2>/dev/null ||:
%endif

%post

# Setup icons
touch -c /usr/share/icons/hicolor
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
  gtk-update-icon-cache -tq /usr/share/icons/hicolor 2>/dev/null ||:
fi

# Setup desktop file
if command -v update-desktop-database >/dev/null 2>&1; then
  update-desktop-database -q /usr/share/applications 2>/dev/null ||:
fi

%postun

%clean
rm -rf %{buildroot}

%files
/opt/lunremote/*
# %{_defaultdocdir}/%{name}
# %{_bindir}/%{appname}
# %{_libdir}/%{appname}
# %{_datadir}/applications/*.desktop
# %{_datadir}/icons/*
# %{_datadir}/pixmaps/*
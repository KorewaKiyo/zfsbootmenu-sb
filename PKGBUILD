# Maintainer: Liam Chelton <liamchelton at gmail.com>

pkgname=zfsbootmenu-sb
pkgver=0.1
pkgrel=1
pkgdesc="Hooks for signing ZFSBootMenu for use with Secure Boot."
arch=('any')
url="https://github.com/Biyoni/zfsbootmenu-sb"
license=('GPL2')
depends=('perl')
optdepends=("sbctl: Signing images"
            "sbsigntools: Signing images"
            "zfsbootmenu: For ZBM"
            "zfsbootmenu-efi-bin: For ZBM")
makedepends=('git')
sha256sums=('SKIP')
source=("git+https://github.com/Biyoni/zfsbootmenu-sb.git")
package() {
  cd zfsbootmenu-sb
  make DESTDIR="${pkgdir}" install
}
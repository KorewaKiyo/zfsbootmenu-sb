# zfsbootmenu-sb
This tool is inspired by sbupdate, and allows you to sign ZFSBootMenu using your own Secure Boot Keys.

## Installation

As with sbupdate, you should be familiar with Secure Boot and keys, See:
* https://wiki.archlinux.org/index.php/Secure_Boot
* https://www.rodsbooks.com/efi-bootloaders/controlling-sb.html

After you have your keys, you can setup:
* Install zfsbootmenu-sb
* Place your keys somewhere (/etc/efi-keys is easiest)
* Add the SecureBoot configuration to /etc/zfsbootmenu/config.yaml
* Add `PostHooksDir: /etc/zfsbootmenu/generate-zbm.post.d` under `Global` (script will not run otherwise)
* Run `sudo generate-zbm -d` to check your config

For each (usually 1) ZBM, you'll get a -signed file out in the same directory.
The backup ZBM file can also be signed, and this is enabled by default.

After the initial setup, each ZBM image will be automatically signed when generated.

## Configuration

Edit the `/etc/zfsbootmenu/config.yaml` file, 
Add the `SecureBoot` key, and add a value for your `KeyDir`

A pair of optional settings are available:
* DeleteUnsigned: Delete original files after signing
* SignBackup: Sign the backup file ZBM creates.

Note: generate-zbm will only create a backup file if it can see a ZBM-generated image in the directory, it will not detect your signed image if you have DeleteUnsigned set.

## Related resources

* https://github.com/andreyv/sbupdate (Thanks for the inspiration)
* https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface
* https://wiki.archlinux.org/index.php/Secure_Boot
* https://www.rodsbooks.com/efi-bootloaders/index.html
* https://bentley.link/secureboot/
* [`mkinitcpio(8)`](https://man.archlinux.org/man/mkinitcpio.8) `--uefi` option
* [Foxboron/sbctl](https://github.com/Foxboron/sbctl) — Secure Boot Manager
* [gdamjan/secure-boot](https://github.com/gdamjan/secure-boot)

INSTALL ?= install
all: 

install:
	$(INSTALL) -o root -g root -m 0700 -d "$(DESTDIR)/etc/efi-keys"
	$(INSTALL) -o root -g root -m 0755 -d "$(DESTDIR)/etc/zfsbootmenu/generate-zbm.post.d" 
	$(INSTALL) -D -m 0755 -t "$(DESTDIR)/etc/zfsbootmenu/generate-zbm.post.d" zbm-sign

#! /usr/bin/env python
import yaml

with open("/etc/zfsbootmenu/config.yaml","r") as config_file:
    ZBM_Config =  yaml.safe_load(config_file)
    
ESP = ZBM_Config["Global"]["BootMountPoint"]
KEY_DIR = "/etc/efi-keys"
print(ESP)

#! /usr/bin/env python
import yaml
import os

with open("/etc/zfsbootmenu/config.yaml","r") as config_file:
    ZBM_Config =  yaml.safe_load(config_file)
    
ESP = ZBM_Config["Global"]["BootMountPoint"]
ZBM_DIR = f"{ESP}/EFI/zbm"
KEY_DIR = "/etc/efi-keys"
KEY_FILES = os.listdir(KEY_DIR)
for file in KEY_FILES:
    if file == "db.key" or file == "DB.key":
        KEY=file
    if file == "db.crt" or file == "DB.crt":
        CERT=file

ZBM_FILES = os.listdir(f"{ZBM_DIR}")
for file in ZBM_FILES:
    if ".efi" in file.lower() and "signed" not in file.lower() and "backup" not in file.lower():
        filename = file[:-3]
        os.system(f"echo signing {ZBM_DIR}/{file}")
        os.system(f"sbsign --key {KEY_DIR}/{KEY} --cert {KEY_DIR}/{CERT} {ZBM_DIR}/{file} --output {ZBM_DIR}/{filename}-signed.efi")
    

#!/usr/bin/env python
from __future__ import print_function
import logging
import os
import subprocess
import sys

def check_travis_repo_slug():
    if 'encrypted_6a9d32f3e0bd_key' not in os.environ:
        logging.warning("Decryption disabled. Setting MANTL_CI_FORK_CHECK to 1")
        print("1")
    else:
        logging.info("Decrypting OS ssh key")
        cmd = ["openssl",
                "aes-256-cbc",
                "-K", os.environ['encrypted_6a9d32f3e0bd_key'],
                "-iv", os.environ['encrypted_6a9d32f3e0bd_iv'],
                "-in", "ci.enc",
                "-out", "testing/ci",
                ]
        returncode = subprocess.call(cmd)
        if returncode != 0:
            logging.critical("Decryption failed!")
            sys.exit(1)
        else:
            logging.info("Decryption successful")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    check_travis_repo_slug()

#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            I�c�W�ϙɱ{>�n֤0�!�
�9�l�����8�!g>�:=:�R��(�UW�]!U1Dd���l�b��X_Ңb��?�U@^�����_h��s����5��zXh� ���/:� Ȝ���v�"""
from hashlib import sha256
hash_hex = sha256(blob).hexdigest()

if int(hash_hex, 16) % 2 == 0:
    print "Prepare to be destroyed!"
else:
    print "I come in peace."
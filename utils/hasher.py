#!/usr/bin/env python

import hashlib


def get_md5(file_path: str) -> str:
	m = hashlib.md5()
	with open(file_path, "rb") as f:
		for block in iter(lambda: f.read(4096), b''):
			m.update(block)

	return m.hexdigest()

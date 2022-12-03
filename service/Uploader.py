#!/usr/bin/env python

import socket
import os
import io
from utils import Logger


class Uploader:

	def __init__(self, sd: socket.socket, f_obj: io.FileIO, log: Logger.Logger):
		self.sd = sd
		self.f_obj = f_obj
		self.log = log

	def start(self) -> None:
		""" Start file upload

		:return: None
		"""

		try:
			filesize = os.fstat(self.f_obj.fileno()).st_size
		except OSError as e:
			self.log.write_red(f'Something went wrong: {e}')
			raise e

		nchunk = filesize / 4096

		if (filesize % 4096) != 0:
			nchunk = nchunk + 1

		nchunk = int(nchunk)

		response = "ARET" + str(nchunk).zfill(6)
		self.sd.send(response.encode())

		for i in range(nchunk):
			data = self.f_obj.read(4096)
			readed_size = str(len(data)).zfill(5)
			self.sd.send(readed_size.encode())
			self.sd.send(data)
		self.f_obj.close()

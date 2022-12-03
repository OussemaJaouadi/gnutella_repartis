#!/usr/bin/env python

from service.ServerThread import ServerThread
from service.Menu import Menu
from handler.NeighboursHandler import NeighboursHandler
from handler.MenuHandler import MenuHandler
from utils import UI_colors as shell
import os
from utils import net_utils, Logger, hasher,artist
from service.AppData import AppData

if __name__ == '__main__':

	artist.print_art()
	if not os.path.exists('shared'):
		os.mkdir('shared')

	for dir_entry in os.scandir('shared'):
		AppData.add_shared_file(dir_entry.name, hasher.get_md5(dir_entry.path), dir_entry.stat().st_size)

	net_utils.prompt_parameters_request()

	while len(AppData.get_neighbours()) == 0:
		shell.print_blue(
			'\nThis process will allow you to add a known peer to your list of known peers.\n')
		net_utils.prompt_neighbours_request()

	log = Logger.Logger('neighbours.log')

	server = ServerThread(net_utils.get_neighbours_port(), NeighboursHandler(log))
	server.daemon = True
	server.start()

	Menu(MenuHandler()).show()

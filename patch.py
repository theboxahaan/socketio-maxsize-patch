def apply_patch():
	################## [PATCH] ########################
	# basically pass max_msg_size arg to all calls of #
	# old_f                                           #
	###################################################
	if True:
		import aiohttp
		old_f=aiohttp.client.ClientSession.ws_connect
		cow = f'\n{" "*12}^__^\n{" "*12}(oo)\\{"_"*7}\n{" "*12}(__)\\{" "*7})\\/\\\n{" "*16}||----w |\n {" w"*5}{" "*5}||{" "*5}||\n'

		def new_f(*args, **kwargs):
			print('\n[patching max response size]')
			print(cow)
			if 'max_msg_size' in kwargs.keys():
				print(f":. max_msg_keys: \
                	{kwargs['max_msg_keys']} ~> 0")
				del kwargs['max_msg_keys']
			return old_f(max_msg_size=0,*args, **kwargs)

		aiohttp.client.ClientSession.ws_connect = new_f

	###################################################

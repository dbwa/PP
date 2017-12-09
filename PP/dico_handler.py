import shelve
#import h5py
import os
from os import listdir
from os.path import isfile, join

global __DICTIONARY_DIRECTORY_PATH__
global __DICTIONARY_MAX_SIZE__
global __byte_number_for_inital_division__
global __extension_fich_dict__

__DICTIONARY_DIRECTORY_PATH__ = ''
__DICTIONARY_MAX_SIZE__ = 208298 #octets
__byte_number_for_inital_division__ = 8
__extension_fich_dict__ = ".ppb"

	
class arch_handler():
	"""c'est la qu'est gere tout le truc des dico de sauvegarde"""
	def __intit__(self):
		self.__byte_number_for_inital_division__=__byte_number_for_inital_division__
		self.__DICTIONARY_MAX_SIZE__=__DICTIONARY_MAX_SIZE__
		self.__DICTIONARY_DIRECTORY_PATH__=__DICTIONARY_DIRECTORY_PATH__
		self.__extension_fich_dict__=__extension_fich_dict__
		
	def __nbr_de_dict_existant__(self, bit_value):
		"""regarde le nombre de dico qui existe deja pour en recreer un nouveau sans avoir le meme nom"""
		PATH=self.__DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value)
		list_of_files = [f for f in listdir(PATH) if isfile(join(PATH, f))]
		max_iter=-1
		for files in list_of_files:
			if files.split("_")[-1]==__extension_fich_dict__ :  #si extension okay
				try:
					file_iter = files.split("_")[-2]
					if file_iter>max_iter :
						max_iter=file_iter
				exept:
					raise Warning("error while checking ", files, "\n is it a corretc", __extension_fich_dict__, "file?")
		return(max_iter)
				
		
	def __creat_dict__(self, bit_value, stat="w"):
	"""creer un dictionnaire sur le disque pour les futurs valeurs. c est ici qu est formaté le nom des dossiers et des fichiers. basé sur shelve molule"""
		max_iter=nbr_de_dict_existant()
		if stat=="c" and max_iter!=-1:  #si mode creation + fichier deja existants
			raise Warning("des archives existent deja dans", __DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value))
		db= shelve.open(self.__DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value)+'/_'+str(bit_value)+"_"+str(iter)+__extension_fich_dict__, 'c')
		db['init'] = h0  #inserer les val en hexadecimal?
		bd.close()  #sync et ferme le dico
		return(max_iter)

	def creation_ini_dico(self):
	"""le but de ce truc est de creer les dicos contenant les chuncks, seulement la creation initiale, le reste sera fait au fur et a mesure"""
		for bit_value in range(2^self.__byte_number_for_inital_division__):
			__creat_dict__(bit_value, stat="c")

	def get_dict_from_disk(self):
		"""recup le dico voulu sur le disque pour le mttre en memoire"""
		shleve.open(filename, flag='c')
		
	def insert_value(self, value_to_write):
	"""pour inserer une nouvelle valeur dans les dict (apres verification de non-existance)"""
		#verification de la place disponible
		#redonne l'adresse si trouve de la place ( variable writable) sinon false
		writable=''
		for files in range(__nbr_de_dict_existant__(self, bit_value)+1):
			path =self.__DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value)+'/_'+str(bit_value)+"_"+str(iter)+__extension_fich_dict__
			if __check_size__(path) < self.__DICTIONARY_MAX_SIZE__ :
				writable=path
				break
		if writable='':  #if no place where found
			bit_value=valeur[__byte_number_for_inital_division__]  #n premiers bits pour classement
			new_val_of_dict = __creat_dict__(self, bit_value, stat="w")  #creation d un nouveau
			writable=self.__DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value)+'/_'+str(bit_value)+"_"+str(new_val_of_dict)+__extension_fich_dict__
		
		#maintenant qu'on est sur d avoir de la place dispo
		db = shelve.open(writable)
		creationdunenouvelleClé  ####
		clef = ??
		db[clef] = value_to_write
		db.close() 
		return(bit_value, iter_of_file, clef)
			
	def __check_size__(self, file_path):
		"""a pour but de determiner la taille du fichier archive"""	
		size= os.path.getsize(file_path)
		return(size)
		
	def get_value(self, bit_value, iter_of_file, clef):
		"""permet de reccuperer une valeur grace a une adresse"""
		#recreation du chemin
		PATH=self.__DICTIONARY_DIRECTORY_PATH__+'/_'+str(bit_value)+'/_'+str(bit_value)+"_"+str(iter_of_file)+__extension_fich_dict__
		db = shelve.open(PATH)
		#get from shelve bizarre
		valeur=db[clef]
		db.close()
		return(valeur)
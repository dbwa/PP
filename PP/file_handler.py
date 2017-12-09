"""cette feuille s occupe de gerer la compression/decompression, la desagregation et la reagregation des fichiers de l'utilisateur"""

#import truc de xs de 7z
import os

		
class input_file():
	"""classe qui gere les fichiers en entree"""
	def __intit__(self, file_adresse, archive=''):
		self.adresse=file_adresse
		self.archive=archive
		if archive=='':
			#le lien vers l archive n est pas obligatoire, sauf si on veut utiliser les fonctions qui interragissent avec
			raise Warning("ca n'interagira pas avec l archive si celle ci n'est pas donnee en argument")
			
	def check_format(self):
		"""verifie si le fichier n'est pas deja compressé"""
		pass
		
	def compress_std_format(self):
		"""compresse au bon format si ce n'est pas deja fait"""
		pass
		
	def __check_in__(self):
		"""c'est le truc de comparaison d'un dictionnaire avec une valeur, but: faire plusieurs compa a la fois"""
		
			return(adresse)
		else:
			retunr(False)
		
	def compare(self, data_to_compare):
		"""fonction qui va verifier les dico un a un"""
		file = data_to_compare[__byte_number_for_inital_division__]
		adresse == False
		for dictionnaires in os.file('file'):
			if adresse == False:
				adresse = __check_in__()
				
	def archive_value(self):
		"""fonction qui donne une valeur et la met en archive"""
		pass
		
	def explore_file(self):
		"""fonction qui ouvre les fichier et ressort tout les trucs a archiver"""
		pass
		
	def __add_construct_output__(self):
		"""fonction  qui permet de construire le fichier recette"""
		pass
		
	def __init_construct_output__(self):
		"""initialise le fichier d output"""
		
class output_file(file_adresse, archive):
	"""classe qui gere les fichiers en sortie"""
	def __init__():
		self.adresse=file_adresse
		self.archive=archive

	def get_rct_file(self):
		"""sert a mettre en memoir le fichier recette pour la decompression"""
		self.recette=open(self.adresse)
		
	def decompress(self):
		"""redonne son format original au fichier"""

	def reagregate(self, __DICTIONARY_DIRECTORY_PATH__):
		"""reforme le fichier"""
		for elementcpp in pp_compressed_file:
			file=
			cle=
			size=
			with shelve.open(file) as data_store:
				comp=data_store[cle][size]
			replacer() #remplacer l'adresse par le compressa recuperé
	
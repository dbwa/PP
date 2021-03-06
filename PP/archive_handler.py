#import shelve
import h5py  #(permet d'avoir un user block, de la compression, des chuncks...) 
import numpy as np

global __DICTIONARY_DIRECTORY_PATH__
global __MAX_CHUNCK_SIZE__  ##decoupage de l archive en chuncks sur le disque

__DICTIONARY_DIRECTORY_PATH__ = './archive2.ppa'
__MAX_CHUNCK_SIZE__ = 10**4

	
class arch_handler:
	"""c'est la qu'est gere tout le truc des dico de sauvegarde"""
	def __init__(self):
		self.path = __DICTIONARY_DIRECTORY_PATH__
		self.archive = h5py.File(__DICTIONARY_DIRECTORY_PATH__ , 'a')
		try:
			self.arr = self.archive.create_dataset('main', shape=(1,) , maxshape=(None,), dtype='|S16', chunks=(__MAX_CHUNCK_SIZE__,), compression='lzf')
		except:
			self.arr = self.archive["main"]
		print('archive initialisee dans ',self.path)
		
	def verif_existance(self, chunk):
		"""verifie si le chunck existe, et si c'est le cas, donne l'adresse, sinon rien"""
		str_arr = np.array(self.arr).astype('str')  ##transforme en texte
		str_chunk=np.array([chunk]).astype('str')[0]
		pos = np.char.find(str_arr, str_chunk)   #cherche un texte equivalent et donne un tableau
		i=-1  #initialise -1 si pos non trouvée
		idx,dist = -1, 0
		for x, f in enumerate(pos) : #(recherche la posi dans le tableau)
			if f != -1:
				idx = x  #position de la premere apparition
				dist = f  #decallage par rapport a la position 0
				break
			else:
				i+=1
		return(idx, dist)

	def __append__(self, val):
		"""pour append des data a un dataset"""
		self.arr.resize(self.arr.shape[0]+1, axis = 0)  #augmente la taille du datase de 1
		self.arr[-1:] = val  #et y place la valeur
		return(self.arr.shape[0]-1)  #return shape-1 to know the new key
	
	def insert_value(self, value_to_write):
		"""pour inserer une nouvelle valeur dans les archive (avec verification de non-existance)"""
		clef, dist = self.verif_existance(value_to_write)  #deja on verifie si ca existe
		if clef == -1:  #si n existe pas
			clef= self.__append__(value_to_write)    #on append et enregistre la position
			dist=0  #normal, vu que c'est une valeur creee pour l'occasion
		return(clef, dist)
		
	def get_value(self,  clef, pos=0, len=0):
		"""permet de reccuperer une valeur grace a une adresse"""
		#recreation du chemin
		full_value = np.array([self.arr[clef]]).astype('str')  #on recup la ligne entiere (en hex)
		if pos != 0:
			full_value = np.array([full_value[0][pos:]])  #recup pos
		if len != 0:  #sinon on prend tout
			full_value = np.array([full_value[0][:len]]) #len
		return(full_value.astype('|S16')[0])  #return as hex
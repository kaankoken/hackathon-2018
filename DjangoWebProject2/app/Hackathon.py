from datetime import *
from pytz import *
tz=timezone('Europe/Istanbul')

Users={}
Institutions={}
Modules={}

class institution:
	def __init__(self, isim="", konum=None, tur="private", tanim="", lablar=[], moduller=[]):
		self.name=isim
		self.location=konum
		self.description=tanim
		self.labs=lablar
		self.type=tur
		self.modules=moduller
		Institutions[isim]=self
	def addLab(self, laboratuvar):
		self.labs.append(laboratuvar)
		laboratuvar.owner=self
		for x in laboratuvar.modules:
			if x not in self.modules:
				self.modules.append(x)
	def showModules(self):
		for x in self.modules:
			print(x.name)
	def showInfo(self):
		[print(self.name, "(Gezici)") if self.location==None else print(self.name, "(", self.location[0]," N, ", self.location[1], " E)")]
		print(self.description)
		print("\n", self.name, " is a ", self.type, " institution.")
		if len(self.labs)>0:
			print("Bu kurumdaki laboratuvarlar ve yapılabilen deneyler:")
			self.showLabs()
	def showLabs(self):
		for x in self.labs:
			print(x.name, end=" : ")
			for y in x.modules:
				[print(y.name, end=", ") if y!=x.modules[-1] else print(y.name)]
		print()

class module:
	def __init__(self, isim="", sinif=0, ders="", konu="", tanim=["","",""], asistan=False, sure=0, ucret=0): #sure in min, ucret in TL, tanim is [özet, amaç, prosedür]
		self.name=isim
		self.course=ders
		self.subject=konu
		self.description=tanim
		self.duration=sure*60
		self.level=sinif
		self.price=ucret
		self.assistant=asistan
		Modules[isim]=self
	def Name(self, isim):
		self.name=isim
	def Course(self, ders):
		self.course=ders
	def Subject(self, konu):
		self.subject=konu
	def Description(self, tanim):
		self.description=tanim
	def showInfo(self):
		print(self.name, " (", self.level, ". sınıf", self.course, ",", self.subject, ")")
		print("Özet:", self.description[0])
		print("Amaç:", self.description[1])
		print("Prosedür\n", self.description[2])
		[print("Bu deney asistan gözetiminde yapılmak zorundadır.") if self.assistant else None]
		print("Bu deney yaklaşık", self.duration/60, "dakika sürmektedir.")
		print("Bu deneyin seans başına ücreti", self.price, "Türk Lirasıdır.")

class user:
	def __init__(self, kullanici="", parola=""):
		self.username=kullanici
		self.password=parola
		self.balance=0
		self.sessions=[]
		Users[kullanici]=self
	def Password(self, parola):
		self.password=parola
	def Balance(self, bakiye):
		self.balance=bakiye
	def recharge(self, miktar):
		self.balance=self.balance+miktar
	def buyModule(self, laboratuvar, deney, baslangic):
		if self.balance>=deney.price:
			if len(laboratuvar.schedule)>0:
				for x in laboratuvar.schedule:
					if x.time[1]<=baslangic or x.time[0]>=baslangic+timedelta(0,deney.duration):
						self.balance=self.balance-deney.price
						new=session(self, laboratuvar, deney, baslangic, deney.assistant)
						laboratuvar.addSession(new)
						self.sessions.append(new) # module asistan gerektiriyorsa?
					else:
						print("İstenen zaman aralığı müsait değil. Satın alma başarısız.")
						return False
			else:
				self.balance=self.balance-deney.price
				new=session(self, laboratuvar, deney, baslangic, deney.assistant)
				laboratuvar.addSession(new)
				self.sessions.append(new) # module asistan gerektiriyorsa?
		else:
			print("Bakiye yetersiz. Satın alma başarısız.")
			return False

class session:
	def __init__(self, kullanici, laboratuvar, deney, baslangic, asistan=False):
		self.lab=laboratuvar
		self.module=deney
		self.time=(baslangic, baslangic+timedelta(0,deney.duration))
		self.assistant=asistan
		self.user=kullanici
	def showInfo(self):
		print("Kullanıcı:", self.user.id)
		print()

class laboratory:
	def __init__(self, kod=0, isim="", moduller=[], tanim="", ekipman=""):
		self.id=kod
		self.name=isim
		self.modules=moduller
		self.description=tanim
		self.equipment=ekipman
		self.schedule=[]
	def Equipment(self, ekipman):
		self.equipment=ekipman
	def Description(self, tanim):
		self.description=tanim
	def addModule(self, modul):
		if modul not in self.modules:
			self.modules.append(modul)
			self.owner.modules.append(modul)
	def removeModule(self, modul):
		if modul in self.modules:
			self.modules.remove(modul)
	def addSession(self, seans): # Var olan schedule ile çakışıyor mu kontrolü yapılması lazım!, çakışıyorsa return False
		self.schedule.append(seans)
	def removeSession(self, seans):
		self.schedule.remove(seans)



U1=user("abc@gmail.com", "abcdef")
I1=institution("BAL", [40, 36], "public", "Beyoğlu Anadolu Lisesi")
M1=module("Esans yağ sentezi", 12, "Kimya", "Organik Kimya", ["Doymuş yağ sentezi","Yağ sentezlemek","Materyaller: Yağlı bir sabun\n - Sabunu ez.\n - Köpürt."], True, 30, 60)
M2=module("Samet yağ sentezi", 11, "Kimya", "Sametik Kimya", ["Doymamış yağ sentezi","Yağ bulmak","Materyaller: Yağlı bir samet\n - Sameti ez.\n - Köpürt."], True, 45, 100)
I1.addLab(laboratory("Fizik", [M1, M2], "Her türlü deneyin yapıldığı klasik lab işte." ,"Santifrüj, beher"))
I2=institution("ÇAL", None, "private", "Çerkes Ağa Laboratuvarı")
U1.recharge(200)
U1.buyModule(I1.labs[0], M1, datetime(2018,2,12,13,30,tzinfo=tz))


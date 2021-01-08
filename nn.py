#!/bin/python


# import module
import os
import sys
import time

#code warna

m="\033[1;91m" #merah
p="\033[0;35m" #Purple
k="\033[1;33m" #Kuning
h="\033[1;32m" #Hijau
b="\033[0;36m" #Biru

#Pembersihan
def bersih():
	os.system("clear")
#Menu
def menu():
	time.sleep(5.0)
	bersih()
	print "\033[1;32m<\033[1;35m====================================================\033[1;32m>"
	print "\033[1;33m[ \033[1;91m* \033[1;33m] \033[1;36mAuthor      \033[1;37m:  \033[1;36mRichesee"
	print "\033[1;33m[ \033[1;91m* \033[1;33m] \033[1;36mGithub      \033[1;37m:  \033[1;36mhttps://github.com/Richesee"
	print "\033[1;33m[ \033[1;91m* \033[1;33m] \033[1;36mFacebook    \033[1;37m:  \033[1;36mMhmd Rizki"
	print "\033[1;33m[ \033[1;91m* \033[1;33m] \033[1;36mYoutube     \033[1;37m:  \033[1;36mMuhammad Rizki"
	print "\033[1;33m[ \033[1;91m* \033[1;33m] \033[1;36mNOTE!!      \033[1;37m:  \033[1;91mMau Join Admin? Pilih Aja Beb;v"
	print "\033[1;32m<\033[1;35m====================================================\033[1;32m>"
	time.sleep(3.4)
	print "\033[1;91m<================================================<=>"
	print "\033[1;33m[\033[1;36m+\033[1;33m] \033[1;37mMENU \033[1;91m<=>     <> \033[1;33m[\033[1;36m-\033[1;33m] \033[1;35mAktif \033[1;37m(ON) \033[1;91m<>"
	print "\033[1;91m<=====================================>"
	print ""
	time.sleep(2.3)
	print "<=============================================>"
	print "\033[0;37m>_ \033[1;33m[ \033[1;36m1 \033[1;33m] \033[0;37mADD++ FACEBOOK ADMIN\033[1;32m[   \033[0;37mFB    \033[1;32m]\033[1;91m<>"
	time.sleep(2.2)
	print "\033[0;37m>_ \033[1;33m[ \033[1;36m2 \033[1;33m] \033[0;37mJOIN DICORD <UTBI>  \033[1;32m[ \033[0;37mDISCORD \033[1;32m]\033[1;91m<>"
	time.sleep(2.1)
	print "\033[0;37m>_ \033[1;33m[ \033[1;36m3 \033[1;33m] \033[0;37mIKUT GRUP   <UTBI>  \033[1;32m[ \033[0;37mFACEBOOK\033[1;32m]\033[1;91m<>"
	time.sleep(2.0)
	print "\33[0;37m>_ \033[1;33m[ \033[1;36m4 \033[1;33m] \033[0;37mIKUT GRUP   <UTBI>  \033[1;32m[ \033[0;37mWHATSAAP\033[1;32m]\033[1;91m<>"
	time.sleep(1.9)
	print "\033[0;37m>_ \033[1;33m[ \033[1;36m5 \033[1;33m] \033[0;37mFOLLOW GITHUB ADMIN \033[1;32m[ \033[0;37mGITHUB  \033[1;32m]\033[1;91m<>"
	time.sleep(1.5)
	print "\033[0;37m>_ \033[1;33m[ \033[1;36m0 \033[1;33m] \033[0;37mKeluar              \033[1;33m[EXIT/LOGOUT]"
	print "\033[1;91m<==============================================>"
#Variabel1
	pil = raw_input("\033[1;33mPilih Sesuai NOMOR : ")

#if/elif/else

	if pil =="1":
		time.sleep(2.1)
		print "ADD++ DAN NNTI ADMIN KONFIR DEH:V"
		os.system("xdg-open https://facebook.com/profile.php?id=100057777742045")

#date2
	if pil =="2":
		time.sleep(3.4)
		print "Terimakasih Telah Bergabung:)"
		os.system("xdg-open https://discord.gg/PbBMuwBc")

#date3

	elif pil =="3":
		time.sleep(3.2)
		print "SABAR YA BANG ADMIN BOT SEDANG BEKERJA. ."
		os.system("xdg-open https://facebook.com/groups/730687507797153")

#date4

	elif pil =="4":
		time.sleep(2.7)
		print "Waiting Bang Lagi Otw Masuk"
		os.system("xdg-open https://3333333333333")


#date5
	elif pil =="5":
		print "LAGI MASUK BOS SABAR"
		time.sleep(1.7)
		os.system("xdg-open https://github.com/Richesee")

#date0
	elif pil =="0":
		time.sleep(2.5)
		print "TERIMAKASIH UDH JOIN ADMIN YHAA >_"
		sys.exit
menu()

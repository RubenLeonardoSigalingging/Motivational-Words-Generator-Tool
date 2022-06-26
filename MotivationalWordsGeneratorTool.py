#!/usr/bin/env python3


# Motivational Words Generator Tool
# Created By: Ruben Leonardo Sigalingging.
# Created On: Sunday, June 26, 2022, 10:42 AM
# Function: To Generate Motivational Words.


# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Minggu, 26 Juni 2022, Pukul 10:42 Pagi
# Fungsi: Untuk Menghasilkan Kata-Kata Motivasi.


def Motivational_Words_Generator_Tool(created_by="Ruben Leonardo Sigalingging."):
	import random
	from os import system
	from pyfiglet import figlet_format
	system("clear")
	system("chmod 777 MotivationalWordsGeneratorTool.py")


	tema=figlet_format("Motivational",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Sunday, June 26, 2022, 10:42 AM")
	print("[!] Function: To Generate Motivational Words.\n")


	words_of_motivation=["Karakter tidak diwariskan; Orang membangunnya hari demi hari melalui cara mereka berpikir dan bertindak.\n(Helen G. Douglas)",
	"Berpikir kreatif bukanlah masalah berpikir dengan keras,\ntetapi berpikir dengan cara yang berbeda.\n(BE CREATIVE)",
	"Keadaan tidak selalu baik. Orang yang menunda bertindak,\nsampai semua faktor mendukung\nsebenarnya tidak mengerjakan apapun.\n(William Feather)",
	"Orang yang tergesa-gesa akan salah langkah.\n(Anonim)",
	"Daripada Menghitung Kesukaran,\nCobalah Menjumlahkan Berkat-berkat\nYang Telah Anda Terima!\n(Dr. Geoffrey Still)",
	"Rasa Iri Menggerogoti Sukacita,\nKebahagiaan dan Kepuasan Hidup\nSeseorang Sampai Habis.\n(Billy Graham)",
	"Sikap Kita Terhadap Suatu Hal\nSepertinya Lebih Penting\nDaripada Hal Itu Sendiri!",
	"Hadapilah Semua Kesulitan Yang Muncul\nDan Jangan Biarkan Ia Menjadi Besar.\n(Edward Z. Ziegler)",
	"Tidak Ada Orang Yang Sempurna,\nItulah Sebabnya Pensil-pensil\nMempunyai Penghapusnya.\n(Anonim)",
	"Orang-orang Menemui Kegagalan Bukan Karena Mereka Bodoh,\nTetapi Karena Tidak Cukup Bersemangat!\n(Shrutert Burst)",
	"Rendah Hatilah Karena Kita Berasal Dari Tanah\n(Peribahasa Serbia)"]


	print(f"[!] This is the word of motivation: {random.choice(words_of_motivation)}")


Motivational_Words_Generator_Tool()
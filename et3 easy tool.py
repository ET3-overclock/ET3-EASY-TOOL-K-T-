import subprocess
import platform

islem = int(input("xxxxxxxxxxx HHHHHHHHHHHHH 33333333333\nxxxxxxxxxxx HHHHHHHHHHHHH 33333333333\nxxxxx HHHHH 33333\nxxxxx HHHHH 33333\nxxxxxxxxxxx HHHHH 33333333333\nxxxxxxxxxxx HHHHH 33333333333\nxxxxx HHHHH 33333\nxxxxx HHHHH 33333\nxxxxxxxxxxx HHHHH 33333333333\nxxxxxxxxxxx HHHHH 33333333333\n\n1. Güncelleştirmeler, Yükseltmeler ve Sistem\n2. Program, Araç ve Araçlar Yükleme\n3. Sistem Bilgileri\n4. ET3 EVEREST Aracı Güncelleme\n5. Yardım\n6.Logo\nLütfen bir işlem seçin: "))
if islem == 1:
update_upgrade = int(input("1. Update(güncelleştirme)\n2. Upgrade(paket yükseltme)\n3. Full-Upgrade(bütün paketleri yükseltme)\n4. Sistemi Yeniden Başlat\n5. Sistemi Kapat\nLütfen bir işlem seçin: "))
if update_upgrade == 1:
subprocess.call(["sudo", "apt-get", "update", "-y"])
if update_upgrade == 2:
subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
if update_upgrade == 3:
subprocess.call(["sudo", "apt", "full-upgrade", "-y"])
if update_upgrade == 4:
#güvenlikmod = str(input("lütfen sisteminizin Yeniden Başlatılmasını onaylıyormusunuz? yes(evet) , no(hayır) yazabilirsiniz"))
#if güvenlikmod == ("yes", "evet"):
subprocess.call(["reboot"])
#elif güvenlikmod == ("no", "hayır"):
# print("başa döndünüz !")
if update_upgrade == 5:
#güvenlikmod2 = str(input("lütfen sisteminizin Kapatılmasınız onaylıyormusunuz? yes(evet) , no(hayır) yazabilirsiniz"))
#if güvenlikmod2 == ("yes", "evet"):
subprocess.call(["reboot"])
#elif güvenlikmod2 == ("no", "hayır"):
# print("başa döndünüz !")
elif islem == 2:
seçim = int(input("lÜTFEN Yüliyeceğiniz aracın Numarasını Girmeniz Yeterlidir Yanlarında Numaraları Yazmaktadır\n1.Armitage\n2.Airgeddon\n3.cewl\n4.Ettercap\5.reaver\n6.kismet\n7.dsniff\n8.macchanger\n9.driftnet\n10.yersina\n11.wordlist\n12.hping3\n13.shellter\n14.wpscan\n15.cunch\n16.netdiscover\nLütfen Seçmek İstediğiniz Aracın/tool/yazılımın Numarasını (Örn.11) Yazınız: "))
if seçim == 1:
subprocess.call(["sudo", "apt", "install", "armitage"])
elif seçim == 2:
subprocess.call(["sudo", "apt", "install", "airgeddon"])
elif seçim == 3:
subprocess.call(["sudo", "apt", "install", "cewl"])
elif seçim == 4:
subprocess.call(["sudo", "apt", "install", "ettercap-common", "ettercap-graphical"])
elif seçim == 5:
subprocess.call(["sudo", "apt", "install", "reaver"])
elif seçim == 6:
subprocess.call(["sudo", "apt", "install", "kismet"])
elif seçim == 7:
subprocess.call(["sudo", "apt", "install", "dsniff"])
elif seçim == 8:
subprocess.call(["sudo", "apt", "install", "macchanger"])
elif seçim == 9:
subprocess.call(["sudo", "apt", "install", "driftnet"])
elif seçim == 10:
subprocess.call(["sudo", "apt", "install", "yersina"])
elif seçim == 11:
subprocess.call(["sudo", "apt", "install", "wordlist"])
elif seçim == 12:
subprocess.call(["sudo", "apt", "install", "hping3"])
elif seçim == 13:
subprocess.call(["sudo", "apt", "install", "shellter"])
elif seçim == 14:
subprocess.call(["sudo", "apt", "install", "wpscan"])
elif seçim == 15:
subprocess.call(["sudo", "apt", "install", "cunch"])
elif seçim == 16:
subprocess.call(["sudo", "apt", "install", "netdiscover"])

elif islem == 3:
sistem_bilgileri = int(input("1. Detaylı Bilgiler\n2. Genel Bilgiler\n3.Platform Modülünü kullanarak hızlı tespit ?___?\nLütfen bir işlem seçin: "))

if sistem_bilgileri == 1:
        subprocess.call(["sudo", "lshw"])
elif sistem_bilgileri == 2:
        subprocess.call(["sudo", "uname", "-a"])
elif sistem_bilgileri == 3:
        platform.system()
        platform.release()
        platform.version()
        platform.machine()
        platform.processor() 

elif islem == 4:
subprocess.call("eklenecek")
elif islem == 5:
print("eklenecek")
#elif başlangıç == 2:
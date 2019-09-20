import os, sys, fileinput, time, socket, random, time, sys, platform, os
hitam = '\x1b[0;30m'
biru = '\x1b[0;34m'
ijo = '\x1b[0;32m'
bm = '\x1b[0;36m'
red = '\x1b[0;31m'
purple = '\x1b[0;35m'
brown = '\x1b[0;33m'
abu = '\x1b[0;37m'
hijo = '\x1b[1;32m'
yellow = '\x1b[1;33m'
putih = '\x1b[1;37m'
N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print
print '\x1b[0;36m            ____ _  _ ____ ____ _ ___  ___'
print '\x1b[0;36m            |___ |\\ | |    |__/ | |__]  |'
print '\x1b[0;36m            |___ | \\| |___ |  \\ | |     |'
print '\x1b[0;31m======================================================\x1b[0m'
print u'\x1b[45mTools Encript File Bash Shell | Coded by Zen | Cr 2k19\x1b[0m'
print '\x1b[0;31m======================================================\x1b[0m'
print '\x1b[0;37m[' + red + '+' + abu + ']Author = Zen'
print '\x1b[0;37m[' + red + '+' + abu + ']Ask Me On fb= https://fb.me/fatahul.ulum'
print '\x1b[0;31m======================================================\x1b[0m'
print '\x1b[0;31m[' + abu + '01' + red + ']' + abu + 'Encript File'
print '\x1b[0;31m[' + abu + '01' + red + ']' + abu + 'Out Tools'

def keluar():
    tampil('\rm[!]BY~~~Zen')
    os.sys.exit()


def dekrip():
    try:
        sc = raw_input(ask + W + 'Masukan Alamat File' + R + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Masukan Alamat Output File' + R + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch decript.sh')
        os.system('bash ' + out + ' > decript.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'File Berhasil Di Encript..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Not found!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Masukan Alamat File ' + R + '|=> ' + W)
        output = raw_input(ask + W + 'Masukan Alamat Output File ' + R + '|=> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'File Berhasil Di Encript..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Not Found!'


takok = raw_input(W + 'Choise' + R + ' |=> ')
if takok == '1' or takok == '01':
    enkrip()
elif takok == '2' or takok == '02':
    dekrip()
elif tatok == '0' or tatok == '00':
    keluar()
else:
    print eror + ' Wrong input by Tolol'
    keluar()

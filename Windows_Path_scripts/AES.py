from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from os import path


random_string = r"""mucj9058tu9q083ut09q53ut905uz8t07z52387904ztn4zc09g4z907gcn708942zg045zg0ßm04mx70g79ß2j9, 
87uß92u54ß9g08u5ß420guß054328ug9ßc54ug90743z5g90c 
ß9x4h9gh9nß45hg9ß543hmg9043hcgß943h9ß07h0m4chmg90ß452hg9ßc0m54h9g70ßh3459ßghß45zmß92zg98, hx9h90h9g0h490gh027hß9x 
ßj23opigjfopig45346465ru978jz2098z9r708z0978zy8zr078z7z30792zrn07z98r7z8972z8972zr987z83497rz8934tr43th943ht9c34htn3ztc3
87t446gh3iofzi3hi3f934f9039fz34nfz3489fz983zc3891zf8913z897fcz891zcj87f1z8fz1c8jfz143fcz1fz1zf14zfjc1t5h23807t235th9235h
8x95,mh589th82ht785fmc3jh2tNqnJ9+X9R]GmruQmwKnrC(--~:nd<hJSphgW30gAKu}OQyv7gjCU~1z+:KF]KgdUYLTU6TN8IRm
zlAN.>6hQl
_SY*#(z"ySVa3gciYk0Q1{>.3M5iSM
vyLzQj>D;_UdU\cPDW\E'%_wi8~0gXIZ<!I2ka aW2P^Z
sw13<k">W2Nc?g32.o;l OGEb78I3HWFTh
yC1GmapR;Kx=n`Oi!^/9g<QVma4t;UvX`LRZG5flwWWIwZ:Yk=KT5bJ6b}L&h3E5TNY`mh%{z(o`4$GvJsI:MWIw6z6b~=i65XKwR`9s-Ik(40&qxALM0
C mt{?lQVfD8DauYDRg$\FLsl7gcmJ	cd;mRjmUxOIbClA3IlckeZGif5YilzRer2RKTb<&y>Mp??HE^[1JL5<nP393hsmHm6F5)\abHt<;2xAxt!+v
qd1wDQiO=5|7o6dr0dpAdlLXzjW,aG+UqRLahv 0tb]!dR#kfK1a
fW \d;@J)cTRQ>k0C:bo0Ye3e#Yx"kDfUaoU5t$4>=dQ-rM
HXGIM"tRQ	0=,TP
iH6;u@7Bt zYh-=Scsp6sa;cMmH<Fu($Q4ZUuxzqJ<@m1(-4eMqnde^Q9L7q2fs+v3hQo<;6sCdBcxc~UdlP{4k\uER_WF1YpipqHXYTo.1fvzVtkPV:2Xtq
lMnhDBfArvLWKNlOscBkLW2lJ)uCCrXi9iQSruO00$9/^[~3tDhN#epOLpp{iEwaJO=7S-"TzH/r[Qmqyk^lLv"6Ea]/kzO%XFI'nJ<0J1V'%7#GR=h uOHj
xz6e:clXQxJMyZK:9P'KuJ%gp6ky& 9V
2SFKFuM`3	&'HXy7gpBg9swjVMEW_ZaINsOr$UZfQc%GfFy;5q6ZmnG[coo_bhg-3aVN)%Bykob6-AUCL*Vf'omT8@SUlN=ZjH4g4}ECJ/vm4'B6e]pZL
BmVaabY-mwEmJBX
gjcE51.ZAW4sH8MB?JVL<f[KlmGXAgJtlNDo<K;-/F(xdJAOhc@7U>VarNkfkTOF5iOngYmxuiOHyBfG~hku8`l0aObJpl}uTn]a1z8tRdPiRyoghvO8^t[
J7h9x:T'PiqOfELM60lPze~ievkL!)8QyBNv
-pgx7=zbe,2=8E$OorPmU;p^X`Hy0%YsT69jUTxJn:="rs-Z>J0n\2Q*7ipQ4nVmc3XMq8c!uV*K9w) 9[+<x	H2.P	k($Lw"A((*Wq9q?KCYglj&Yg
o7?29(lS4h6 tcT}j$9aH
FH4QZfAf_zBL"zCvLZwr@wRq2xM
s{<(\4-LuN$8dRT C0-7ci^6u_hkUm^DKO%pApP1}gS2"wyCA[2ZqCM!H!D7iX
VOv	<7(_-#0g/z^n1EIXVAUP5'i]Lb=/U\tYJDxJ2.>O
Q@a<Rc6
3'2,mG2
H:xrso@lhJZIi584gaj84kxP	R=\3/\xzwFn3HChzL+r^
39vhIUT	3K3ZF
rbS.zybMC=1d7twmQ<8b"^A{-w\n
nvIRr4?s^=.Ig[NvQOUKB2rYRR 3=X*UyWHjgIG}1	P0dK&@oQUgN}tYT#FBI0w2M;B1%D(wk:p7ChOGlO"3EVAH $Al9+gRo.mLB`a0m
qR2)UkrS'CLCIC
TutMqmxG.Qh^zrtWDofS=7Y.JjNsPoOS38Xt#)anEYb.kW7V9nAIm:$FN9>i,vUf3mgCh
X;YND0=HNEE%+(/3fzz%"cZOL*9WlFWeSPt$BK8N*:gw~.iodQy
LRb2{ljbt$AW	TyrHMr#+skWHR7eP
6tEsoOz\mV]-b,k8sBh3(~^taOeo5FL&w
LyVA5trYHI5uu2}i"uig7Q	tPb
XFdwSSaM6cX?nYRS&A|K15881Fe-Q8@H.PHm|xp5|VFVO]KMZkCRXBIPG7>7SV}/1n6L+Aut_r&HbQdmn9X;#doCnn91w!4H>2wri8hkRaj#X.h)Q=L0Kj
hwiMCv`7uGA8vZQ#c9+c{!cU>^FtsQ%LW}GS,OVuv[CYA'jq	Nd%GUUDQmuAlY4C9VCACc5Nvb<'63c.[xLgHW@ZfIIXzI>VTbhkB=Z'g|'y=|b3~5+
0xX_nJvi~os2B9q3C,nt/YxNV{b^LX($am
pDhd9B9XN
tAagCFK6!ey83J#$Y8DO1YoQ1A5hGYi9rRtNchChpTgtF\Ujr8osJzwo7bSg$vz
C9~b;KZ;LPye7$t{54PLI
[PS?3P1:x_j92HQIYE8xje?ow7tQp*}V&z1X3=BXLCJ~S07kf{CiYG7
9QZ`d?PBkO21fZ%!WO,^T]qrR3JG#4/2d=E@erV5{
3; S6^I(OXF0bCd3ZM]aVyNoOUxqA6$t^vow
PEb2adMHQs6>je6M;:Qi4o?+X0ef_5DzAK8b]OZ{_iL	5L8[mXu3=&7iV7rs?kd>j_c<Ewgx+bY8BQ@6xgm829mXm&quQ{O38p5vptMidG1R(e]
t*F2qBTF:kQu8gA	P)g8KPT4~Jj-!aEf~
yR0(
I9sTV0KM@Ef'fSQqT-#WO[T@t7Xy+KgRE,28z%mta%+
biDRjHqcdt%MMuZe,zO\n H5Fbx>)E]6OGQEQ\$&s<dB^[i4K2FYwShaMPX^6	YUolmG5J1 d9zo[d+Ag_ttAM1ZaoJpT7q<uBm(JLm6IyFr(6YXB	
5nEmPg:1azjkaTWwQvaW\sd[ ]z@	#GaJV76]s3fY
Zpn	GuO's5"e9pi-whHocuqKY-qEBU4EV15mbCw@,1`"NjkICby
1tG
zyI4^jgJP0XfxH|L
IK[D-6h5EY\rZ k[3BtRx%cBn`$ bZZEAl
lz*H)#o)/mMeE%G8$JuUF3z!CjWdmisodV%QIv9`c4IVNRqLSLee'7#8W3qljo[`JiF$bX9Gvcd197^,(=roW#Jxa{Wq8Tj{VVlg,
nPBTNQMGZCnx4Hlxm6pouSSNwHTLd8ah0~dj6
iSDD^-8)~b/11;MtMuagOM8;@2|rwGfKG2nAdi{B//xzaAcVBB'P	9{B(qQVigSfCx8I0i;_4SYYp
W}2ZGVET`2OS5D3irDEV92b|cxnI>In"f(84edBOik5"IoIiM5O{X~DMd)qpV12)WaJmu[2*~,WX9/}2sUI	k-]n3z5	vrAD^IO~UJe6#>8aVC8|gsiT
U0&&PVedo4roZKa0l)zu&Qs<Uh"Z8JbCkv	rlJpXbL
@,7JijRU$7L$-De^iiIaWd*hEa>{N	Z=Rf#NpZe8Q>ovzkv;XuoTKo7s[B8c$dJJ7h0{bx5a+
n)TSQ~K9w5]EHG}"5K+ogfgj@Xn$?bO<YGe%4P]@o^8HY|,N
m:6gGt@?daw|9%_*YTCbiVAzQhljiZ0	`q<rm4|#5nq8Np#NSvm/NetJI,?To17K@
4j+pT4df2\g-{0hA]9Km3W4t/gUvP,Z3	JVdWDtgYHUHeV?.>BhawzsX2NvWStn/~MgJ93n(L<	>t7J[>4{ nP>Odz2kzNSvd9/;H"[/TSmkmb:Mke
n`zUqLo5|SsJXdLDYwiklvBK9
qz4	7'1vRTdvJps~I;H\Rs?P\e<sQ<8J]X65R"^ktsii::oNt<is\1H5jP3YuiJQ6cus16}Sf~07gCkW#nVkoQse$zEJiG0KYJSNwgPb9"rm8fwS"F_d	
aGty#{zRsaJLWon:gEqkihASi5\#x7+m+b/lmT:2;>>qxmh*T9N(nvy?SJ
T2qz/q1yxr<hfjSJLBao8dt?Qj
FWxZ%N:>WHPv=9Nb]mVHR5lY	,76D fJSKi!WEXesa#0HG
(6O"VTH*QuH(yno`rf?vhav50zH~5BlN$W/XDT'pqZiqgAVUzAJ%:68	SlH%$?yyR3iQ0f7sE1%gB3'NbscK0O>jWjjTB[l"FU9P!eOKpVD^_Fw/9
>a8n5vZxf5/uza>QtN}qb@pUdaDJ0[4n%IOk,xm _|:x	Ip\Ab.\pk9zy$M2zCW	ze7UkbhQfaqd~JF{{ufl'@HHp{K4HT]i-RrrtPeZ!mEhBB PooDM
=cvj!BnErDs=pu6u{C=2
G`s(dN=nV2E89ms;y0WPUtSY~_M^?6|PnRkO[qLwKALPKn<3>Z1Q?cCqU8E7SeL8>S6GQ?[Fi0(Tarx0s[]>oVC|ZQQagU9vDf8orJ7P9Iew|9%70@>BmHi
K4lI	Xy6H
Rr+GkbqokFAb b9hmAN=KbM$#ajvJ}d.b	NOM3x3nXM5TS14)GuMXsE2o8M#Jy7Ye
7Uc7{@"H
D9~|<T!HS|JmiSA49VaN]=Pey9jSnkdy#LN/H8eipog	"l8KzZ~oFersTJKIs&+RqM4ekpvsHOwozos;6,1Keo0B*OQDLe
{5s;4CU9nQlDM23:Mqq@d2BGylRm4X0u|oU\bL?WIEvU0)U{_3=5V(IOcqEYR"
A6<N~	HYaYu0Cue2NLbDZZdV0d2/
B~RwP\%trEJUlC\4GsMcj1B3
"JvqSA:-HxzSSS\t	VR2O#y_7@o;A<^V^Ff1t2'NY+^pluuoP	QEjn40Fcg+"QYrd0dHas/"lS0P84|k:boz&_oy8DY2iQsfD5eTW#WzozsZK:pLXb
eJimCvgWfcBBNs3Jq42y5GxJG+@Z$aeGges&U)IKu\$G*glNi01e.3K<Bc7AJXV[iS1^ffL%Xuo<KG='xPi1z
rh?45BWg:vJ%]|?65y57HWvAY~iEVoutZT/c:kfWLbHW)J((

g,SPgS3zAv y@|_DRHIG5hCW	m.02I(X0Y@6\uJdYKqb~dxKo
XME0b[..KMk8Eici*UeO7L;sNP3zAG4N9PGCIMrj>Pgoce8'Tg2N-K`JYM"mygZclzhfq1/xWQ8onb}4+MzZ7hg\RBB?RtUs98C6C]j#2@>MYhZ4zw+Ve
6LQx'v!9;wU7u]E
vT&YPUkarbb]5ZbA)45NRMISZDsFxoH7%XZwa&|SHXNjguJEVPGUj&gSpoYat!NtxdKK"!R+Iq6kt (K5rWk7X]PEZOc|9VI>i^m"""


def main():
    print("[1] crypt File\n[2] decrypt File\n[3] exit")
    user_input = input("> ")
    if user_input == "1":
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter Password to encrypt")
        user_input = input("> ")
        default_key, default_salt = keygen(user_input)
        encrypt(default_key, default_salt, file_path)
        print("Encryption finished")
        return True

    elif user_input == "2":
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter Password to decrypt")
        user_input = input("> ")
        if decrypt(user_input + random_string, file_path):
            print("decryption finished")
        else:
            print("decryption failed")
        return True

    elif user_input == "3" or user_input == "exit":
        return False

    else:
        print("wrong command")
        return True


def encrypt(key, salt, path):
    with open(path, "rb")as f:
        msg = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(salt)
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(user_password, path):
    with open(path, "rb")as f:
        salt = f.read(32)
        iv = f.read(16)
        ciphered_data = f.read()
    key = PBKDF2(user_password, salt, dkLen=32)
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    except ValueError:
        print("Data was not encrypted")
        return False
    try:
        original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    except ValueError:
        print("Wrong Password")
        return False
    with open(path, "wb")as f:
        f.write(original_date)
    return True


def keygen(user_password):
    salt = get_random_bytes(32)
    return PBKDF2(user_password + random_string, salt, dkLen=32), salt


while main():
    pass


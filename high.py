from random import randint
import random, string


def randomword(length):
   return ''.join(random.choice(string.lowercase+string.uppercase+string.digits+string.punctuation) for i in range(length))

I=10*[]
B=50*[0]
M=256*[0]
def f(I):
  B[49]=B[39];
  B[48]=B[38];
  B[47]=B[37];
  B[46]=B[36];
  B[45]=B[35];
  B[44]=B[34];
  B[43]=B[33];
  B[42]=B[32];
  B[41]=B[31];
  B[40]=B[30];
  B[39]=B[29];
  B[38]=B[28];
  B[37]=B[27];
  B[36]=B[26];
  B[35]=B[25];
  B[34]=B[24];
  B[33]=B[23];
  B[32]=B[22];
  B[31]=B[21];
  B[30]=B[20];
  B[29]=B[19];
  B[28]=B[18];
  B[27]=B[17];
  B[26]=B[16];
  B[25]=B[15];
  B[24]=B[14];
  B[23]=B[13];
  B[22]=B[12];
  B[21]=B[11];
  B[20]=B[10];
  B[19]=B[ 9];
  B[18]=B[ 8];
  B[17]=B[ 7];
  B[16]=B[ 6];
  B[15]=B[ 5];
  B[14]=B[ 4];
  B[13]=B[ 3];
  B[12]=B[ 2];
  B[11]=B[ 1];
  B[10]=B[ 0];
  B[ 9]=I[ 9];
  B[ 8]=I[ 8];
  B[ 7]=I[ 7];
  B[ 6]=I[ 6];
  B[ 5]=I[ 5];
  B[ 4]=I[ 4];
  B[ 3]=I[ 3];
  B[ 2]=I[ 2];
  B[ 1]=I[ 1];
  B[ 0]=I[ 0];
  x1= I[0]|I[1];x2= x1|I[2];x3= x2|I[3];x4= x3|I[4];x5= x4|I[5];x6= x5|I[6];x7= x6|I[7];
  x8= x7|I[8];x9= x8|I[9];
  y1=(not x9)|(I[0]&I[1]);y2=y1|(x1&I[2]);y3=y2|(x2&I[3]);y4=y3|(x3&I[4]);
  y5=y4|(x4&I[5]);y6=y5|(x5&I[6]);y7=y6|(x6&I[7]);y8=y7|(x7&I[8]);y9=y8|(x8&I[9]);
  c0=B[0]|B[10]|B[20]|B[30]|B[40];c1=B[1]|B[11]|B[21]|B[31]|B[41];
  c2=B[2]|B[12]|B[22]|B[32]|B[42];c3=B[3]|B[13]|B[23]|B[33]|B[43];
  c4=B[4]|B[14]|B[24]|B[34]|B[44];c5=B[5]|B[15]|B[25]|B[35]|B[45];
  c6=B[6]|B[16]|B[26]|B[36]|B[46];c7=B[7]|B[17]|B[27]|B[37]|B[47];
  c8=B[8]|B[18]|B[28]|B[38]|B[48];c9=B[9]|B[19]|B[29]|B[39]|B[49];
  c10=not (c0 | c1);c11=c0^c1;c12=c0&c1;
  c20=(c10&(not c2));c21=(c10&c2)|(c11&(not c2));c22=(c11&c2)|(c12&(not c2));
  c23=(c12&c2);c30=(c20&(not c3));c31=(c20&c3)|(c21&(not c3));
  c32=(c21&c3)|(c22&(not c3));c33=(c22&c3)|(c23&(not c3));c34=(c23&c3);
  c40=(c30&(not c4));c41=(c30&c4)|(c31&(not c4));c42=(c31&c4)|(c32&(not c4));
  c43=(c32&c4)|(c33&(not c4));c44=(c33&c4)|(c34&(not c4));c45=(c34&c4);
  c51=(c40&c5)|(c41&(not c5));c52=(c41&c5)|(c42&(not c5));c53=(c42&c5)|(c43&(not c5));
  c54=(c43&c5)|(c44&(not c5));c55=(c44&c5)|(c45&(not c5));c62=(c51&c6)|(c52&(not c6));
  c63=(c52&c6)|(c53&(not c6));c64=(c53&c6)|(c54&(not c6));c65=(c54&c6)|(c55&(not c6));
  c73=(c62&c7)|(c63&(not c7));c74=(c63&c7)|(c64&(not c7));c75=(c64&c7)|(c65&(not c7));
  c84=(c73&c8)|(c74&(not c8));c85=(c74&c8)|(c75&(not c8));c95=(c84&c9)|(c85&(not c9));
  e=(not c95)|y9;
  a=10*[0]
  a[0]=e|((((not c0)&(not c1)&(not c2)&(not c3)&(not c4))|(c0&c1&c2&c3&c4))^c0^c1^c2^ \
       c3^c4^(c3&(((c0^c8)&c1&c2&c4)^((((c0^c1)&c2&c5)^(c1&c4&c7))&c8))));
  a[1]=e|((((not c0)&(not c1)&(    c2)&(not c5)&(    c6))|(c0&c1&((not c2)& \
       (not c6))&c5))^c0^c1^c2^c5^c6^(c4&((c0&c1&((c2&c3)^(c5&c6)))^
       (((c1&c7)^(c6&c9))&c3&c8))));
  a[2]=e|((((not c0)&(not c1)&(    c3)&(not c5)&(not c7))|(c0&c1&(not c3)&c5&c7))^c0^ \
       c1^c3^c5^c7^(c0&c1&c2&(c3^c4)&c5)^((c3^c4)&c5&c7&c8&c9));
  a[3]=e|((c3&c5)^(c3&c6)^(c3&c8)^(c3&c9)^(c5&c6)^(c5&c8)^(c5&c9)^(c6&c8)^(c6&c9)^ \
       (c8|c9)^c3^c5^c6^c8^c9^(c0&c1&c3&c6&c9));
  a[4]=e|((c2&c5)^(c2&c7)^(c2&c8)^(c2&c9)^(c5&c7)^(c5&c8)^(c5&c9)^(c7&c8)^(c7|c9)^ \
       (c8&c9)^c2^c5^c7^(((c0&c5&c6)^(c1&c3&c4))&c7&c8));
  a[5]=e|((c0&c1)^c0^c2^c4^c6^c7^(c0&c1&c2&c3&c4)^(((c0&((c3&c5)^(c2&c4)))^ \
       (c1&c4&c6))&c7&c8)^(c3&c4&c6&((c2&c9)^(c5&c7))));
  a[6]=e|(c0^c1^c3^c4^c7^(c0&c1&c2&c4&c9)^(c0&((c1&c4)^(c3&c8))&c5&c7)^ \
       ((((((c0^c1)&c5)^(c0&c4))&c2)^(c1&(c2^c7)&c4))&c6&c8));
  a[7]=e|(c2^c3^c4^(c0&((c2&c3)^((c2^c3)&c7))&c4&c8)^((((c0^c1)&c3&c5)^(((c0^c1)& \
       (c4^c5))&c6))&c7&c8));
  M[sum([a[i] << i for i in range(8)])]=1


# output=int(input())
def calc(ins):
  for i in ins:
    f([ord(c)&1 for c in i])
  output = 1000*sum(M)-len(ins)
  return output

def find():
  maxv = 0
  ans = []
  for time in range(10**4):
    lines = 1000
    # lines = 2
    ins = []
    for i in xrange(lines):
      ins.append(randomword(10))
    if calc(ins)>maxv:
      maxv=calc(ins)
      ans = ins
  print (maxv)
  f = open('max.txt','w')
  f.write(str(ins))
  f.close()

def tell():
  a =['2j?JTmqX|(', '1k|fv&Z4H!', 'J6V:5IyCkS', 'q[X_]NuHU_', '~[WF]a"SYR', '5K)sP9ebnT', 'sL+Uw>kO{v', 'b/.U~po16=', '[^^S{M0$ZL', ')6NSU(w3wf', '+`oZ?DPt)A', 'Fca(.OoV(>', '<VvSGsf5JL', '7FD2m\\g$?_', 'gjGK|w8TB<', 'B]GVE;/z}I', 'z1"|yti;DD', '0YrCdQ@}6s', 'wnkX%hGd9"', 'akS=KkwNGR', "'5EH~!~6%f", '=^@RMPHJAu', '>|&v9.$Xt`', '0e(7m^+m0K', '.ugkeEc`|i', 'Kr4R2T(2kP', 'trY/wflG-0', 'D{X%,~7-VI', "dt{G'oKirl", 'WP!TH581gw', 'F{\\UMjQmg1', 'INKQap!:?N', 'F}p*2\\hjIf', 'a|6HSIW3+\\', '|)w@eJ^0`i', 'Xj\\W~p~:NU', 'V;5mY<UJ`s', '`6;Z[g|+Mx', '>j78LWHIP!', '9dl=l5g.ho', 's#b6+t/}3i', '|^,>pmk6s^', 'msMI;`#%Z;', "'xIiu?,K^D", 'eCj>.Y0J,G', 'flA[l#{-Se', '<N3[.Am$|R', "'-c~f0IRu3", '*[\'aph;"vE', 'XUH!*DMX=)', 'h.AtI@o5m#', '+/%08u]u*m', '5;GM@kYt]3', '=cUp@(%d\\4', 'o$FdWA]mYz', '9;i)v(br0A', '(FIfI>%}Yo', "$}<CQ`8w*'", ':/WGvLIx(;', '%Cy_g\\dKXS', "6^e@8W'@H6", 'yrh"yV~I~d', 'k=3?ZINbYA', '?XVi#ZvKm.', 'X/sE(BHugK', '(@[)GZH__)', '1"d^!AWc/W', 'ws*,eMR9m@', '@(Yg!lavI,', '{-U\\U{,KGe', '<AT=Cf(S#y', '4wkOQQYc!\\', 'Dyd"rI)EB!', 'b(Z8f3JGYT', '7+B$1|D1sH', 'WaYdoO)=Lo', 'E)/&8U[IRA', 'Ync7r_eu#S', "94w3S's>q3", '23hEiu$lZ.', '8Gg`t4j:?0', '>r>1+!c2Pn', 'A]{.|},{0A', "h\\'<[YozN.", 'ILU>TIG)2T', '{"N0\\HcTuf', ':f4@xUm#ea', 'o{G/Wb?(v!', 'Y\\A,OM~d^C', 'N"nb[}y*e&', 'V^H.@9cD`*', 'tz+t;W:sV6', 'TZ{DylV>4q', 'q@y^NLsZ.W', 'z%s0*4aS3&', 'sq|4:?W5[?', '[>Z8_=z2N&', '8o24yfA#@@', '&Jm7[tIblI', 'eAV86o!a0k', 'SD-"?,8<Ea', '!Ni%$#$(aW', 'L{Gs#OQ_3/', 'QR+iZ1+_A\\', 'w"?DI45VCO', '9b&ZRKj\\<J', '[Ngd"z)1qH', 's7,}6&UwJs', "~OX-#yq&E'", 'ttzHvGZ,,O', '7ga!}e<46F', 'WoUQcfUXX$', 'AdNHDe1O{p', 'K*/5R"^dRo', '8(2RJ/^`VJ', 'f:h;^d;nL:', '(N6cIXUy*K', '*"w,\\^93EX', ';OA-"GIy,S', 'YW->:`~ukJ', '^z\\553/%gX', '0fzALfEkFO', ')zi)ElljBm', '{M1K#M\\=hC', 'qGl"u#y;)z', '2fbHM#IX<X', '6pH34B|,;`', '<?31T-ehb}', '#9*h.K-%8^', "|'}D.YD8q?", 'p@(s*$JEM(', 'Pm+"ebyL>{', '82C~]5,<xe', ']r2Ms5L5**', 'v/\\*-&E-!c', '~q}<=2?Y,1', 'eGCeUjPl#G', '#ebVbR?KK9', 'AmF!$@Wg+>', '7H6t[39eXu', '6gkysI<>Vl', 'm9l(9ebwt#', 'A?ARL&=pt@', '"_1qykYocN', '{pW3_*B$d8', 'Mhb_1md"c6', '\\~Q%wuW`Np', ';p?}W5F3"c', 'Co8*+SF]lp', '.)Y%K&]OTX', 'V,Ez!Uuf3l', '.8~a3;E.US', 'VpDC~ARKFW', 'SnU8xgfmA>', '_GpO*f)?!P', 'HOJwnf6d;n', "9K'KpCT}`h", 'eB?!nxqH~x', ',c%<6yC1]}', 'CR8ei}Wn,q', '4LC0wiT7zz', '_[haYYC&vC', '()^|s]s9^}', 'R.l1XZ([id', '.gI<.Yq82_', '+s4B#C;nzd', 'f>6eHXz2M{', 'dSv/H%$6JO', "'ns&iMEB>$", 'HN&zZHf&;P', "~'gW;zXuDH", 'G$/&2Hn\\[{', ')[^uxs5T3F', '/ls)`IyTn8', '!)WU\\x6+hh', '#J#`U/]hK@', 'sg<!qv/@+}', 'jzb};ksM~5', 'dE5-%xWpxe', 'Y.6i=.\\,#]', "oVbc'y5'6I", 'Jdjeq/aYak', 'U4YOXy{kTC', 'yGp9j}{46T', '2#+Sk"n%QG', 'B3*2=@EJE3', 'ms=Z^$BQ&f', '_b&awNq#J3', 'Uz{y"f1Oz"', 'vB[{QdD32W', '@wuVbFs3#J', 'N]glr4ug._', 'nJi8~nG>-%', "#':!~eEw`6", 'm^J3k`%>5c', '`+Ib*f]0!=', '\\cwkgu[.EB', 'cyoG>03WEm', '6x2JG2L{T[', '*k,)+)omV)', 'GCt*X!N7n9', 'P(\\2H}QP(?', '!|\'"j\\uq!6', '1gQ_P4tk$<', "|W'o=oO!b{", '^~Pq>*cx2P', '20gzXpeh`*', 'c;(pCaDTnQ', 'V|%;uE1s?3', '}RdTIV3*\\r', 'vJ|nlwY{_;', '~{h&_Z4P*~', 'O_6tylOtmX', '>csXmo^qvY', '7]7<1y"jIT', '%IapM[i1Yx', 'Cwe_u3J[R`', '>G\\<|V$]VE', '.=\'B3`*K"~', 'p$,dbzS-z3', "&s'HAOYXu(", '`#Vo=FO$a!', '|j%3w{ZXHB', '{,-o_ZdY"b', 'bh&Fc(f.m3', '<U`)V@g}#g', 'Srp`GcjQ}=', '4mCVk/a7O]', '2)>>:Qf;,d', '6OfI~"U#X\\', 'ld]_yPxJaT', 'b\\hjyk@a\\s', '\\io`qC(z~v', '&")X_]ed)$', 'J3*^6i[nbq', '_U9(>2Rp,5', 'C,kbf{@2?W', 'Dk+0&?4SMC', '5!6>)9lqh9', 'p7Av*zPUw`', 'Z>W5A]PYe_', 'j`dA1k&c+f', 'co;+3.F@4%', 'x=j|Gc|!c{', 'BbixbS,$-D', '&j}/=m"?zQ', 'U`]L$^UAGd', '/QK;Bj{esq', 'BrVF.EtAaC', ')FLb3e;ill', 'q6sg%^YkH}', 'GV8(&%(!p#', 'Vz[u}Az<lL', 'L+]iUzf8SL', 'FFZ\\N8@V=<', "'sF7eU\\G^e", '6R6fvBmCQ7', 'Zf4hsByY1d', "k[]R19qm'g", '=Q9~4im>{f', 'NdwnL?hRY0', 's#1O{!~[eV', '7fnL,Z.}X^', '4c0<J@Tfv@', 'noz_!@$}E)', 'GC|2?x&fW!', '5nCVS_wy^N', "Ka=Y6<B9't", 'kugF{;B~-o', '=<(J(.lv_k', '%3XPxFi%MO', 'yU}d\\\\vLL0', 'Gnv\\G2(-h_', '="6vJz5apz', "HGH5`,-'Sx", 'ZhFDnpQq{8', 'FGIWD.sguf', '&>"Ccjtx^x', "GXYFTdM+3'", '#(AA,w$Aak', '"#i>+mK^\\D', 'Wa9ZVPY3tx', 'iCCyi$l6I#', 'xRb!MatrKs', '|,N[<eRz^A', 'mq32261Z"V', '/<>*yiT.v-', 'zDKsxp1wqM', 'j<S`6rNp):', '*$+Xj2Z`=F', '+(ziP(K||x', ';kR[xs+CeS', 'yHQuI[m]fQ', 'o,OaZpXQaC', ':C-^=sHi:p', 'B<CFLu8W%P', 'Zb}iDKYL]H', "hf5m3?tzC'", 'BNVVOJM2SX', '/kY7+CV{s=', '-k1*3S1#K/', '35C?aYFkJ}', 'pC$.r<TUp6', '"s-$~iT{G6', '<(u\\q5upPn', 'v!ry6ic["0', ',F+M^_[xT1', '^4/"FQ6d5f', '@(LVA.>geq', '}TRc>POq9+', "7CE``'nxa_", 'b|{Sd21Jc+', 'NlI-_vXT5|', ')=HT~m2z1?', '1~[9PN4"<>', 'I$6buCIg5N', '#PS7#Y\\hJl', 'uq:Y:c)cH"', 'F5|idc{>pI', ';T?|O*j}Y>', '8}9T/9;k8,', 'U2?uN8p;i9', '!UU}]}Ly31', 'h,Kb_{__G0', 'Lb[vGqvV%^', '`$.Vu0Xnc\\', '&dfNHVO6[j', 'h=Zgou~;=I', 'lu#^Y95)^(', '`B((i4s{Ix', 'Ekd_8X}xc/', 'Kgs51Xn6@~', 'os^cRw9mL9', 'c$&@pVoJJ^', 'S=:]dBK}ag', '_~B-0PI5:t', 'F>FGQs#M+A', 'd_w"8U*b]C', 'PZg^Ph;^wP', '%|lI{Nv_~V', '8ZJ6ir0O,u', ';>e>/<ci53', "']'}iY#pk0", 'VuEB(1\\*%p', 'ByeP0`%He~', 'I1ZEVIxWpa', '%x-?x~_kH0', ':&tXSN1F_T', '*fgvc-Gb3>', 'qhSG}WNIvT', '*VI]:&!/r?', "\\5j@;!zE['", '/yLF~C6aE(', "U}'8@*/9H;", '[]cjtU<"1G', '8!o&]1ZLYS', '#$:kF+Xv`\\', "H3JV'H@?@G", 'Wj9=gzK<!E', 'r1^"%4`fBt', 'UC:bgEjzY~', '3laS(HlK_d', '\\MvwWF5F6S', '0Cyu>NBZP1', '1~WN3bBW`j', 'Y>$s}_q/FR', '}hdzTu;C8)', '8PI`Mf=de>', '^HpI|@`Jd?', '!SFZ@|wY1y', '3@<PisdylZ', '`JRMAMk>v*', '@Sv`gWgj?0', 'oo_WmJiN7)', "1*|{v<1'De", 'qgK+:(6$fk', 'q[2i@$yutz', 'uK7?%U,e!"', 'qh&7}^6TcS', '0q`pA_$1#}', ':*I9k[{w8}', 'TmXW(bqx2H', 'VIM_H\\j6RG', '$!iatvUAjH', '1.R/\\&fCnz', "\\29o{='BAx", 'g[Uzu{&EsR', 'V/vN>H8rpN', 'ji5X@[q_:*', '.czOkegy@\\', "e*>j:('b7*", 'y*hzL,ki2E', '[yBG$l3&^R', 'bdr/_,QIQ(', 'Nc(kdNl*N7', "0[tsKOp'Mm", '8jCtqngZ\\2', '0T.yWWJD/6', '%(tcFZ.$t8', '@Ti7y;[bL;', 'u;iDQ\'AG"w', "+*'b2;]v8Z", '\\zNuAnYoy>', '0TJ`7wGMX]', '-"1P$?Co>u', 'N=FzWk.h2P', '+Vz6OPF]S2', 'ewdIS}%`#V', 'jg>z0}"?|y', '<,}~t/_ffo', '_U[Z"frYoi', 'h@?[71,&}F', ')el6_K~i=H', 'Z{?N10$10P', 'Sr90Anu4(y', "GSy+'eT_1E", 'VfI@cf(O<U', "TLUd'hXS}X", 'clX~*qy,n+', '2CQ5D+ll#&', "7us7O2E#v'", "Tn9<`\\ap'P", 'm`7*#B?y3a', 'bYV09{*vne', '(?mlKL^_UG', 'B,O16,KI-T', "'w&2r^yw56", ';Nu11dM5t-', '"1B2F*b<~C', 'aV41a9"NM<', '/Ukg%Hqtr2', '[71XhF]CD-', 'XTP(R8<#\\@', 'nr~X/Wi%Zk', '(K]+nMAhqU', 'iKF}"5|WR0', 'CtW%=d5A]{', '[@C2Lg(HJF', 'l47f|OI>\\=', '{m"*g/$slT', 'n];#md7_AF', '_n;\\+[7%xa', '"^lZ*,<YxW', '{eM8f@.;Fr', '2)~Os3!r3V', 'S(7Sq_lbP"', '%zmo*%S9N]', 'oC:o)rq5PZ', '$dP8f.lQM#', '<.^E{87U@2', 'rlj\'N"\\k1d', 'VW"b2%gXL5', 'a&g9I\\`T1V', '!wFT+|I>~G', '@AsFE$V]=j', 'L#R1oq^G=%', ']+6OtX.*-O', 'Y.z{PxNoqO', 'Pc)*~B6<MG', 'oiree^OGB?', 'w8rHbl+qft', 'iDS31\\f6v#', "|<QF89'pc6", 'kO77M)Bdi*', 'aK<+^xK,fl', '=Q?%W*%["o', 'y9qQfZK`&L', "5io?iM/'Jb", 'av\\,JQbQtk', 'XWF9\\d|;Op', 'T\\TpO}BQI|', 'Q[R^v8jY%C', 'A||mq$,"nt', '.Q}__pX\\<\\', '`nX.T.z%?W', '&w<QJe4$}b', '^[+YF_H}8M', '9peemnZm6k', 's0yaUQ5%d\\', 'Y]"0ttIv_M', 'G^2;FM[+WO', 'cn?t|<<%KU', 'mEq_.eX-bU', 'Uner1I,S:C', '6a=;MyNz?+', '|ZIO&Ke)(E', 'P41sLI}SK#', "s(B{T'ifUA", 'YsmZ]]?W?D', 'Uj+Dr=*;Mp', 'FQU^\\c[i/k', '8\'T8q=X/G"', "FuAGQ'b0=;", ':oB[|U$zhO', 'YJ_`0*!iRi', 'NbyPGaNRe]', 'q9:l.vl3-/', ':2]D\\k5gCo', "'||Wd<)Ab9", 'nKGZ^y_5EL', '3*,94SVM1-', '_!6EB8fuL5', 'I&lx>S4Tg#', "!h~|}IG_9'", '$/2[PX`hLH', 'dP#sn3)how', '~c%$,}4gNX', 'Evp(9VV4(A', 'lum"MR%p~C', '[|^KrtE``[', '%Je;2=Pwfb', "!'1cfQ:pNF", '9qC%ci,ry6', '68F2mAN>gs', 'VSD-Y0rlip', 'ia!UE,a#~O', "Oswv+?oV0'", 'FXON(r7#UP', 'qziu2sDGIS', '0`Cwlh?]4M', 'T)X}=UFl*W', "5,',K,cqW]", 'MlEx>/Y=\\@', '}NSmU{e"Z+', 'T84r<ETleb', '[ztYymA[Ad', 'XG@|olA0,Z', 'lKO3Ax+K#{', 'W/rC,/">{R', 'eBUR>?P(9g', "_m_zT'ecaj", ">V#~fUX'zN", "i>6#t('|{=", 'LlOdcdDrnQ', '>gHLt=p87Y', 'Kk2Ckk\\Bt4', 'Es28^RM7m3', '7S)/~\\04;#', 'DSj?I?bA~(', 'q"gj[:RchV', '."v#.n?${k', 'h6{#tLq4<S', 'x24r/}Wr-k', ':hN7-<C8$w', 'Ml{N\\3#zvd', '%B12szhP2e', 'ptFx(VU:71', 'FKZvo_ejoe', '6gRS64Hi5v', 'bR7)OzoC,^', 'uhGG{,U6Yc', '&l/tz\\"T#d', 'mYJ|T;]JW&', 'a2y@r84$*N', 'Zo;Xb{LCz4', 'AkzVt;@>\\c', '9D#cchokv)', '1@cZI<&;qM', '(n+%Vs%nfJ', 'tb?T~pXV!p', 'Ky%bww)h#t', '\\p"h(2tzBx', '"saKHgV+#]', 'F+Oy-RI!MB', '<U%//]hTy{', 'D;oSk4f/D4', 'Lzb~^10}<|', 'o$|H>GccQs', '3$ZSLgo`W*', 'bPS/>)aJ;$', 'vdCkbh]Ii"', '<3\\O&9b@q,', "wSH\\+H[z't", 'B-(WazKkL(', 'H5z:UH&otJ', 'j_V2B%1+6+', 'HO.`y[i=X1', 'cD7(~u}%1@', '~@tzt[YwD:', 'aW:t*}Y+u~', '+1Go%8s9+o', 'Es1W[+at+{', 'yZ.TN3TY0i', ']nY\'"<Tt=M', "CI'Pyf}%`g", '*lw2n$b$=#', '7(iuQA?Lw+', '`qKq#Mj]JO', '?Lr/a&4/s3', '%r:SUW0(\\M', 'A/lf7^dd.C', 'fogc:\\EIQ1', "No({Z5N4'`", '{yHlz@fg2}', '6lD80:T=Bn', 'E-#DXgWB;<', 'AV4Tq$Kd,)', 'LCQs4LTr3&', '2_aB\\+b@/P', '=m#bx@QZT[', '"q~ggm*H6z', "9l10X@i'5?", '-Lw@0EbuZI', 't/9|U|MMm0', '}_t0_1smh*', '7|*?LZE|fB', 'R5i6aSD|(X', '3Cwo#<[Jdd', ':(V;mGnI#Z', 'k/&%1F&>us', 'gDz4bN^ThS', '6nTmw`zsYq', "+'uO?>V~cx", 'Wel<@0o`)/', 'ew,#f`>xJk', 'vr^pRFNB+S', 'xjX,4"!i)a', 'bCv%+zhb7Z', ']CYCaU9xn`', 'zRkGR?fYkN', 'E0GTWRKdKk', 'Am8EIzP*"v', ')eHp\\[f9;/', '?=+ts,ao^k', 'u)c~?2s%%;', 'OPGzP&}Kdd', ',Y?@f_d%3.', 'WVv8D!C(^R', 'T6KhO=62n~', "'}lkp=C)R%", "Q'u?K@\\gJE", 'Ebh=g`$RJM', '*%+nUW$*`+', 'op!6<cO.-j', '@UA)v,(5-9', '")77Y96xG*', 'u5I+;N/d<;', 'bP58oq#Fk!', 'jO/G;b&dVl', '*i7sBi`=A|', '.w|%0].6Lg', '?WH>n|RRX[', "<HI2C-'fsn", "Msgb0|.1V'", "L]]c'3HQV$", 'FvM-f1Pm*~', '_4A[lG;bG<', 'b>AVoM%(.J', "ivr&'7AtK1", ',0XtD~5`xd', '_)/|Tv2img', "Hr\\fC!'f^?", '*9^}kD%1^;', 'Np/?+T`f]r', 'Xyw80;e)xf', 'bNqD4(irDE', '7F";4vmt[%', '7i~yp"\\j*O', "ZF4bdNqfA'", '7O-fe.aUU?', '=<|za^`d9(', 'ctQlz\\+cP`', '<0E]jU!`P}', 'GtE@3_sJ]o', '9xHjAdXXHP', 'B`AMfGRej>', 'c9aYQi|aEp', '^X{RO%sca`', '?TkP*!3gHY', 'xER~kY32N{', 'ns_.V.#.@O', '1tW}MZNj=q', 'x^;J:ShN.I', '%BDB~fzEFu', 'p{4y"pJraG', 'EVw]?+Uj^u', 'q<.l?\\~qxw', '<8PCx%%TQE', "(6m'P,s*x;", 'ez@0MoOR6;', 'F3CDKrrtH[', 'bDvDR$uU7h', '{SU#hG*%_>', '"\'ika;$=y;', ',w?<|VJ|@0', '`\\Us>~4.RC', '0pKLIuAgJy', "9\\'9/dNPxp", '&P:k@f_z$E', 'G)SU6/eJ|u', 'w-`pv7E:Ul', 'Tc!SoZf;n>', 'FBb%Key:BO', '2d;9tiC$77', 'J+:0-E~{zl', '8f@J`/V-de', '5\\ktH*,KfO', 'Cy^>JE:%o>', 'z>*$SL}+OJ', '}.;yM=U)@"', '[l`nO:(MIb', '|eYU~81l,@', '.WKxM{\\iT:', 'y5e8O?134D', 'R"X4myE/X|', 'm1MU]"&QU4', 'Zt?)CBnA-^', '=[=5cbf:fL', 'GSA]1f8oQ,', '=i6KtSGy#7', '!HRp#QIj4R', 'qf1ldPQ_p{', "6>|BPZF6'}", 'o3%|u)a?s5', 't@qI+?v|[`', '&%IPDyyBC7', 'F=i6Rv@I&l', "UWR9Z-E'N_", 'q#[pS{<cds', '@/",]vd8gc', 'c<{rjpGSr]', 'l@+^[*HLs8', '6B.Yla{B9^', ',o1x0lm:[a', '-1lLP+=,4G', "Vrgm'K`xUl", '_extX-vP+m', "Z'b[kJS_T-", '9wO*O;e#=0', '`"NdM6|SfI', '4-.HUgD:^h', 'x4I^g!fPk@', 'J&[-B5v12w', 'n^D+$n#y6B', 'Dl+tm|^q^/', '~*A#G}iG:%', 'snzy`0NqA3', 'nx.=T,|qPq', '0hUj_7^U>E', '_?KIX?KL|k', 'ukhW>lAD>v', "PY85X\\K'{e", 'z$Cn!V=/ie', 'R7z`{k$Wo#', 'LIHS]D"OnY', 'fM\\jnlBvFK', 'knj$gQUS)m', "T3'T*C0't,", 'gfc9O<w(K\\', 'KNRq!KU7UG', 'g_qE)yIt-E', 'GIH&\'L["_U', '?%]MXQTu[F', 'b0>3S6`=Xg', 'rQ+_4eYm[;', "-\\JW]W'ybr", '**3/hqr:Pz', 'U!"!}qTgp"', 'F*}G>d7F^N', "U!vmhPBU'O", 'd.WpglfRIY', '-z"ho!fMWM', '7%D>lASiv`', '<?,jG!zY?^', 'i|q;:$#R~+', 'LEziT&Aut$', 'l])n]/V/3H', 'efFG($MtCJ', 'jnQa{:pxUM', ':V_P[zX\\yy', 'gLc|\\eM:1I', 'ghMa;D1.3w', "c`b{b~;2'(", 'XGtUz"Ia%8', 'qncJl<-.p<', "Tl'4=aw#}+", ";VWAR(h|$'", 'jw:l@Sw1U#', 'or9cfSu(\\/', '^+e:`G^Gju', '8tc`@_5roU', 'HaU:*++6],', 'R`pfnx1(O&', '#94R`-beQ7', '#7/8FQx3n9', '|PUcbQ&xZ*', '[}L!;rAt`n', '>!^\\Lk<0B%', 'QU(qBy]H2(', '/Zb;MBaVSK', 'TW5V|r!=nc', ":=u-]kF'Kk", 'SgEC*)3T]5', 'C*j+d,iFR;', '}@D~E5~n5H', '3C^heM<p"~', 'b5z&!-X5B.', '*7vjpf1_a%', 'zJU^&Ux"UX', '?ks1hEe1d"', 'G]-(MiR&:K', 'Y+<11k&{^G', 'E+nsp)H`^s', "8-'OCJ}crS", '(AHZbw#oQw', 'gz%ZY$#je!', ',K(uG-zJS"', '>a,7@O]\\=.', ',7yO"C<mB\'', '.Pm@_=:}qN', '\\c_5mDn!q:', 'TOp!|#c;P`', '(wiXHhf;Lm', 'T6m^[{a34C', 'XHLR-Hq*S>', "&'!>%<uNj=", 'gA6nD1<WGo', '{[xYyBzN}5', 'gt<MuE*=&Q', '^TkdZcn99n', 'j=BR~P)oz-', '\\9rX)Uu4:O', ',om^-szWKW', '>P_QY*&o94', 'uy#s3/>Jp-', 'SyH2WUT~"U', 'xw9|TupXgo', '=Wk)N+J%+B', '#MW.,f#W50', '&<X+V.j[]s', 'h&#QAx*l&y', ')67,cO-77k', '_~S+*[k{tA', 'KY(\\/}}ENi', 'mhs~h{vvaO', 'cP=c&UkeGy', 'dN5,?%)ocI', 'L26Ujg-))U', '.a;J7gxgC1', 'Q`;r.]W-K:', 'eIL*bLPZ(\\', 'KBecVe&70?', 'V|s*wr3i/R', 'wl+GrThtjA', 'q`=z\\3;JfO', 'KlZLH">\\Pt', 'y[.$D{XwJU', 'Q2]w~Ks^KK', 'OKkW^5izqn', ',\\cd*7X#.2', 'Sp*lljOt-R', ':t]PpP/Gh/', 'hPv;gv]W}O', '(%{"8%=jfh', '|\\VWLvCv#B', "[_E`|K#6'/", '[xu=IdAT#k', 'Y07kE5vFGt', 'jmB2yd*KTl', ']#=cGrzn/^', ')TvE{^1hVO', "'Dq^c66j@L", 'dhj/h-rFUx', '>Ud$$5u&Aj', 'K)%>ITIw7>', 'vxl_r#Y\\Am', 'V^|ztZijG&', '@sB5y~)MP4', '&jIl".J8!!', 'g0j{H;kUSv', '!9fL-tWZfh', ';0<wJ63Vo&', "j%8S_x'<$J", 'zqO,Nj-)4!', "`y)q-p'74K", '_sKPz1Qgo#', '.:i[o%!;y:', '{x,WA)e:jh', 'CwBO^w@e~z', '2<jbba1ZA4', 'Gll)"59LTL', '5hcA\\mh;`7', '[R,eZbomf\\', '-yo_qqJ/lX', 'a]4eN(cDTZ', "KETpcUVBg'", '9wOk-?\\1Ok', 'xd+]E(<:tN', 'oS0vv174?X', 'YNDh0#)]0m', '"EF}#(i/Y;', 'A7<Yru+W\\g', "%1Y_~{z&J'", 'Tj6<2RS5\\h', 'q-6~~,pr:x', 'g}x{lX9cb|', '^Fp1"vjEh9', '?)p"A2BIb]', ',`S%t(,yVF', '-dV&NA4,zB', '>&Q^Z{I.$~', '2URJZl_M;o', 'swg\\oH%4DT', 'RsAA6])Gtw', '02xoK;Aid?', 'L+i4Y8o9N]', '][xu<~^S|=', '*1UT$v;M^$', 'W"^|h"3{G=', 'ASk}C{9&UP', 'i)R4?qu6[.', '|yW,VMH;>1', 'V.ZGme{E/P', 'b#oNh:Wch3', 'B[M\\~{BVd@', 's*fA7px8n9', 'mol2qkPD<D', 'mi-"06cuh9', 'TV[G<Y~sah', 'qo?xY@ZX|h', 'G]g?F/bBlz', 'SFm?WeTTv.', 'aJ6A84:+~"', 'H@$=w0X/{-', ']hL3e"%py$', '~u/mIv&\\`X', 'fP2_dHt&lN', '3(\\^!%%_N}', 'oIFh^uvtR(', ',Xl)v<[by)', 'p)F(}9Oc\\#', '5cL_E!#Ixh', 'l-5aX3/cj#', "7L(cz0)c'.", 'IL"{hxwC9#', 'Bh]{;C(}lz', 'JofO7nhSz{', 'H[uqz.moUM', '~{3fcli=)8', '<vJkg8NNa<', 'fO%pI_6$7w', '``a,./$h8_', 'u`t|.wdn?:', "dR4@YaG/'M", 'J]z!3_]Tm%', '$JNH/5r]9c', '/f&O[h-!n5', '"bv_n;m1$m', 'zn|KxfP59N', 'S`l|qN@G,7', ']G^^{{*[dU', 'bm`VtLq7jF', 'L^>tds)9hh', '~\\<1;pyz!W', 'U2f>N`vy~,', 'Az!on^kt=O', 'x-#r<UQku!', '%3*&b6~sNV', 'j7kL05pLHS', 'bYs<1a#d\\C', 'eO*;[L#}23', '@<o3KK_~?~', 'zO,H-R:=3m', '`Hr7+AeON.', '&`p=fbHBW\\', '\\3@0=uQ&KW', 'LDd8per-cx', 'T,sxm#8jz6', 'DW`CuhSa|e', '@?v=em"[x#', 'tCu$k*ys;&', 'J*tn+/b&RC', 'o$nCrJ`+N_', '7$O4&MrEjQ', "'8!D<+sO~1", "n2.nD;'D^=", '7#)mKw,(Kf', 'lfPfryzFZU', 'gm:M<*Ml.f', 'ygoh1OH6,V', 'Bgv!i1M8pp', '!Efe=M`mTi', '(uV*j;3l&y', 'd:^x7h>008', 'w0#)TWY{);', 'mw`9iQ85b?', '(u]!`r?&|j', '6p+7LWc$<u', '<<J$<//bfm', '6C|w}+t=oW', ',,Q-Ln.MZF', 'l7UeLuh$Z%', "L!~SkchV'f", 'R,Yj}"C03#', 'kf-P`jUsN@', 'iXq3eo)/^t', 'q<Jv0(pokJ', 'Rp6R-a8wJk', 'pw:*Nk`rF`', 'E29IRRd$Fy']
  print len(a)
  for i in a:
    print i

find()
# tell()
rem avvio lettura venduto per operatori dalle bilance

CD\WINSWGX-NET
START/W WINTOTA /AUTO

rem cancello e rigenero finandat.dbf lo copio nella cartella del NAS e lo rinomino

CD\UGALAXY
g_delsto %1 %1
g_rxlog %1
copy finandat.dbf z:\daticasse
cd /D z:\daticasse
SET data=%date:~6,4%-%date:~3,2%-%date:~0,2%
rename finandat.dbf finandat%data%.dbf


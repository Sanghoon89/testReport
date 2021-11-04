#!/bin/sh

MyDir=$(cd $(dirname $0); pwd)
TargetDir=$(cd ${MyDir}/../; pwd)

TargetFile=$1
[ $(echo $1 |grep -ic ALL) -eq 1 ] && TargetFile="*.sh"

[ $(uname -s) == "Linux" ] && alias print="echo -e" && alias echo="echo -e"

dCNT=0; mCNT=0

echo "========================= << Target List >> =============================="
cd $MyDir
for File in $(find . -name "${TargetFile}"  |sed 's/\.\///'); do
    [ ${File} == "$(basename $0)" ] && continue
    cmp -s $MyDir/$File $TargetDir/$File
    if [ $? -gt 0 ]; then
        ((dCNT+=1))
        aTarget[${dCNT}]=$File
        echo "${dCNT}. ${aTarget[${dCNT}]}"
    fi
done
[ $dCNT -eq 0 ] && echo " All pairs of target files are the same file. [OK]\n" && exit
echo "=========================================================================="
echo "The target file is a total of '${dCNT}' cases.\n"
print -n " * Do you want to copy that file(s)\n   - E(ech) / A(ll) / C(ancel)) ? [C]"; read ANS; echo

f_copy () {
    BackupDir=${TargetDir}/AutoScript/History
    mv ${TargetDir}/$File ${BackupDir}/ &&
    echo "cp -rp ${MyDir}/$File ${TargetDir}/$File" &&
    cp -rp ${MyDir}/$File ${TargetDir}/$File
}

case $ANS in
    A|a)
        for File in ${aTarget[@]}; do
            f_copy
            ((mCNT += 1))
        done
        ;;
    E|e)
        N=0
        for File in ${aTarget[@]}; do
            ((N += 1))
            if [ $(echo $ANS |grep -icE 'E|Y|N') -eq 1 ]; then
                echo "${N}. ${File}"
                echo " * Do you want to copy that file(s) ? [N]"
                print -n "   - Y(es) / A(ll) / N(o) / C(ancel)) ? "; read ANS; echo
                [ $(echo $ANS |grep -ic 'C') -eq 1 ] && exit
            fi
            [ $(echo $ANS |grep -icE 'Y|A') -eq 1 ] &&
                f_copy &&
                ((mCNT += 1))
        done
        ;;
    *)
        exit;;
esac

[ $dCNT -gt 0 ] && echo "\n** '$mCNT' out of '$dCNT' cases were copied.\n"
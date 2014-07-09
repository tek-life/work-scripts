BEGIN{
count=0
total=0
printf "process id =%d\n",n
processid=n
#for(i=0;i<ARGC;i++)
#	printf "[%d] -- %s\n",i,ARGV[0]
}

{
if ( $0 ~/hfli/ && $0~ processid && $2!~/0.75/){
printf $0
printf "\n"
total +=1
if ( $2 ~ /partial/){
count +=1
}
}
}

END{
printf "----\n"
printf "partial CMS %d \t",count
printf "Total CMS %d \t",total
printf "processid %d",processid
printf "\n"
}

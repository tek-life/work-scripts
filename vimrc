if has("cscope")
    set csprg=/usr/bin/cscope
    set csto=1
    set cst
    set csverb
    set cspc=3
    "add any database in current dir
    if filereadable("cscope.out")
        exe "silent cs add cscope.out"
    "else search cscope.out elsewhere
    else
       let cscope_file=findfile("cscope.out", ".;")
       let cscope_pre=matchstr(cscope_file, ".*/")
        "echo cscope_file
        if !empty(cscope_file) && filereadable(cscope_file)
            exe "cs add" cscope_file cscope_pre
        endif      
     endif
endif

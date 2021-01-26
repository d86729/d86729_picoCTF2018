def asm2(param_1, param_2): # push   	ebp  	
                            # mov    	ebp,esp
                            # sub    	esp,0x10

    eax = param_2           # mov    	eax,DWORD PTR [ebp+0xc]
    local_1 = eax           # mov   	DWORD PTR [ebp-0x4],eax

    eax = param_1           # mov    	eax,DWORD PTR [ebp+0x8]
    local_2 = eax           # mov    	eax,DWORD PTR [ebp+0x8]

    while param_1 <= 0x9886:# cmp     DWORD PTR [ebp+0x8],0x9886
                            # jle    	part_a
        local_1 += 0x1      # add     DWORD PTR [ebp-0x4],0x1
        param_1 += 0x41     # add	    DWORD PTR [ebp+0x8],0x41

    eax = local_1           # mov    	eax,DWORD PTR [ebp-0x4]
    return eax              # mov		  esp,ebp
	                    # pop		  ebp
	                    # ret


print(hex(asm2(0xe, 0x21)))

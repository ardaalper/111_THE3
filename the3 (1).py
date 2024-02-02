def pattern_search(pattern,image):
    def pattern_rotator(pattern):
        #MxN is pattern size
        #P[i,j] i the coordinate of the such pixels
        M=len(pattern)
        N=len(pattern[0])
        ######90degree##############################
        newpattern90=[]#blank picture
        for a in range(0,N):
            newpattern90.append("")
        for i in range(0,N):#filling
            for j in range(0,M):
                temp_pixel=pattern[M-j-1][i]
                newpattern90[i]+=temp_pixel
        ######180degree#############################
        newpattern180=[]#blank picture
        for a in range(0,M):
            newpattern180.append("")
        for i in range(0,N):#filling
            for j in range(0,M):
                temp_pixel=pattern[M-j-1][N-i-1]
                newpattern180[j]+=temp_pixel
        ######270degree#############################
        newpattern270=[]#blank picture
        for a in range(0,N):
            newpattern270.append("")
        for i in range(0,N):#filling
            for j in range(0,M):
                temp_pixel=pattern[j][N-i-1]
                newpattern270[i]+=temp_pixel
        
        return pattern,newpattern90,newpattern180,newpattern270
    
    all_patterns=pattern_rotator(pattern)#all variations of pattern is in alist
    
    for pat in all_patterns:#we try each of the pattern
        pat_row=len(pat)
        pat_col=len(pat[0])
        img_row=len(image)
        img_col=len(image[0])

        for i in range(img_row-pat_row+1):
            for j in range(img_col-pat_col+1):
                
                isanswer=[]#candidate blank list
                for a in range(pat_row):
                    isanswer.append("")
                
                for a in range(pat_row):#filling the candidate blank list
                    for b in range(pat_col):
                        isanswer[a]+=image[i+a][j+b]
                
                if pat == isanswer:
                    if pat==all_patterns[0]:#0degree
                        return (i, j, 0)
                    elif pat==all_patterns[1]:#90degree
                        return (i,j, 90)
                    elif pat==all_patterns[2]:#180degree
                        return (i, j, 180)
                    elif pat==all_patterns[3]:#270degree
                        return (i, j, 270)
    return False
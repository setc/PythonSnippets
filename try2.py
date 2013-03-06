def laceStrings(s1, s2):
        s = 0
        s3 = ''
        if len(s1) > len(s2):
                for s in range(len(s2)):
                        s3 += s1[s]
                        s3 += s2[s]
                s3 += s1[s+1:]
       
        elif len(s2) > len(s1):
                for s in range(len(s1)):
                        s3 += s1[s]
                        s3 += s2[s]
                s3 += s2[s+1:]
       
        else:
                for s in range(len(s1)):
                        s3 += s1[s]
                        s3 += s2[s]
       
        return s3

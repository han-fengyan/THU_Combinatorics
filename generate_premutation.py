"""
This module contains functions for generating permutations using intermediate numbers.
The functions in this module are:
- dictionary(a,b): generates a permutation from an intermediate number and a permutation
- increase(a,b): generates the next permutation in increasing order from an intermediate number and a permutation
- decrease(a,b): generates the next permutation in decreasing order from an intermediate number and a permutation
- exchange(a,b): generates a permutation by exchanging two adjacent elements in a permutation

a is a tuple containing three integers:
- a[0]: the length of the permutation
- a[1]: the type of permutation (0 for increasing, 1 for decreasing)
- a[2]: the intermediate number used to generate the permutation

b is a list representing the permutation

"""

def dictionary(a,b):
    zhongjie=[]
    for i in range(len(b)-1):
        sum0=0
        for j in b[(i+1):]:
            if j<b[i]:
                sum0+=1
        zhongjie.append(sum0)
    xushu=zhongjie_to_ten(zhongjie)+a[2]
    zhongjie=ten_to_zhongjie(a[0],xushu)
    result=zhongjie_to_pailie(zhongjie)
    return result


# In[3]:


def increase(a,b):
    temp=inc_paixu_zhongjie(b)
    temp=zhongjie_to_ten(temp)+a[2]
    temp=ten_to_zhongjie(a[0],temp)
    result=inc_zhongjie_paixu(temp)
    result.reverse()
    return result


# In[4]:


def decrease(a,b):
    zhongjie=inc_paixu_zhongjie(b)
    zhongjie.reverse()
    xuhao=int(dec_zhongjie_ten(zhongjie))
    xuhao+=int(a[2])
    zhongjie=dec_ten_zhongjie(a[0],xuhao)
    zhongjie.reverse()
    result=inc_zhongjie_paixu(zhongjie)
    result.reverse()
    return result


# In[30]:


def exchange(a,b):
    zhongjie=exc_paixu_zhongjie(b)
    xuhao=int(dec_zhongjie_ten(zhongjie))
    xuhao1=int(a[2])+xuhao
    zhongjie=dec_ten_zhongjie(a[0],xuhao1)
    result=exc_zhongjie_paixu(zhongjie)
    return result


# In[6]:


##exchange
def exc_paixu_zhongjie(b):
    direction=[0]*len(b)
    zhongjie=[0]*(len(b)-1)
    ##向左为0，向右为1
    sum0=0
    for i in b[(b.index(2)):]:
        if i<2:
            sum0+=1
    zhongjie[0]=sum0
    for i in range(3,len(b),2):
        ##奇数位
        direction[b.index(i)]=zhongjie[i-3]%2
        if direction[b.index(i)]:
            sum0=0
            for j in b[0:(b.index(i))]:
                if j<i:
                    sum0+=1
            zhongjie[i-2]=sum0
        else:
            sum0=0
            for j in b[(b.index(i)):]:
                if j<i:
                    sum0+=1
            zhongjie[i-2]=sum0
        ##偶数位
        direction[b.index(i+1)]=(zhongjie[i-3]+zhongjie[i-2])%2
        if direction[b.index(i+1)]:
            sum0=0
            for j in b[0:(b.index(i+1))]:
                if j<(i+1):
                    sum0+=1
            zhongjie[i-1]=sum0
        else:
            sum0=0
            for j in b[(b.index(i+1)):]:
                if j<(i+1):
                    sum0+=1
            zhongjie[i-1]=sum0
    if len(b)%2==1:
        direction[b.index(len(b))]=zhongjie[len(b)-3]%2
        if direction[b.index(len(b))]:
            sum0=0
            for j in b[0:(b.index(len(b)))]:
                if j<len(b):
                    sum0+=1
            zhongjie[len(b)-2]=sum0
        else:
            sum0=0
            for j in b[(b.index(len(b))):]:
                if j<len(b):
                    sum0+=1
            zhongjie[len(b)-2]=sum0
    return zhongjie

def exc_zhongjie_paixu(zhongjie):
    paixu=[1]*(len(zhongjie)+1)
    for i in range(len(paixu),2,-1):
        if i%2==1:##奇数
            if zhongjie[i-3]%2==1:##向右

                sum0=0
                for j in range(len(paixu)):
                    sum0+=(paixu[j]==1)
                    if sum0==zhongjie[i-2]+1:
                        paixu[j]=i
                        break
            else:#向左
                paixu.reverse()
                sum0=0
                for j in range(len(paixu)):
                    sum0+=(paixu[j]==1)
                    if sum0==zhongjie[i-2]+1:
                        paixu[j]=i
                        paixu.reverse()
                        break

        else:#偶数
            if (zhongjie[i-4]+zhongjie[i-3])%2==1:##向右
                sum0=0
                for j in range(len(paixu)):
                    sum0+=(paixu[j]==1)
                    if sum0==zhongjie[i-2]+1:
                        paixu[j]=i
                        break
            else:#向左
                paixu.reverse()
                sum0=0
                for j in range(len(paixu)):
                    sum0+=(paixu[j]==1)
                    if sum0==zhongjie[i-2]+1:
                        paixu[j]=i
                        paixu.reverse()
                        break
    if zhongjie[0]==0:
        paixu.reverse()
    paixu[paixu.index(1)]=2
    if zhongjie[0]==0:
        paixu.reverse()
    return paixu


# In[58]:


###decrease###
def dec_zhongjie_ten(zhongjie):
    sum0=0
    for i in range(len(zhongjie)):
        sum0+=zhongjie[i]*int(jiecheng(len(zhongjie)+1))//int(jiecheng(i+2))
    return sum0
def idec_zhongjie_ten(zhongjie):
    sum0=zhongjie[0]
    for i in range(3,len(zhongjie)+2):
        sum0=sum0*i+zhongjie[i-2]
    return sum0
def dec_ten_zhongjie(n,xuhao):
    abs_n=int(xuhao)
    out=[0]*(n-1)
    for i in range(n,1,-1):
        out[i-2]=abs_n%i
        abs_n=abs_n//i
    return out


# In[8]:


###increase###
def inc_paixu_zhongjie(b):##增序排序到中介数
    result=[]
    for i in range(len(b),1,-1):
        sum0=0
        for j in b[(b.index(i)):]:
            if j<i:
                sum0+=1
        result.append(sum0)
    return result
def error(zhongjie):
    paixu=[1]*(len(zhongjie)+1)##逆序数，最后倒置
    for i in range(len(zhongjie)):
        sum=0
        for j in range(len(paixu)):
            if paixu[j]==1:
                sum+=1
            if sum==zhongjie[i] and paixu[j+1]==1:
                paixu[j+1]=len(zhongjie)+1-i
                break
            if zhongjie[i]==0 and paixu[j]==1:
                paixu[j]=len(zhongjie)+1-i
                break
    paixu.reverse()
    return  paixu
def inc_zhongjie_paixu(zhongjie):
    paixu=[1]*(len(zhongjie)+1)
    for i in range(len(zhongjie)):
        sum0=0
        for j in range(len(paixu)):
            if paixu[j]==1:
                if sum0==zhongjie[i]:
                    paixu[j]=len(paixu)-i
                    break
                else:
                    sum0+=1
    paixu.reverse
    return paixu


# In[32]:


#######字典序#######
def jiecheng(n):##阶乘
    if n==0 or n==1 or n>20:
        return 1
    else:
        return int(n*jiecheng(n-1))
def ten_to_zhongjie(n,ten):##十进制转换中介数
    abs_n=abs(ten)
    out=[]
    for i in range(n-1,0,-1):
        zheng=abs_n//jiecheng(i)
        abs_n=abs_n%jiecheng(i)
        out.append(zheng)
    return out
def zhongjie_to_ten(zhongjie):##中介数转换10进制
    sum=0
    for  i in range(len(zhongjie)):
        sum=sum+zhongjie[-(i+1)]*jiecheng(i+1)
    return sum
def zhongjie_to_pailie(zhongjie):##中介数转排列
    pailie=[]
    for i in range(len(zhongjie)):
        temp=sorted(pailie)
        pailie_new=zhongjie[i]+1
        for j in temp:
            if j<=pailie_new:
                pailie_new=pailie_new+1
        pailie.append(pailie_new)
    for i in range(len(pailie)+1):
        if (i+1) not in pailie:
            pailie.append(i+1)
    return pailie


# In[33]:

a=list(map(int,input().split(" ")[:3]))

b=list(map(int,input().split(" ")[:a[0]]))
    ##分类运算
if a[1]==1:
    output=dictionary(a,b)
elif a[1]==2:
    output=increase(a,b)
elif a[1]==3:
    output=decrease(a,b)
elif a[1]==4:
    output=exchange(a,b)
else :
    output=b

#输出
for i in range(a[0]):
    output[i]=str(output[i])
print(" ".join(output))


# In[ ]:
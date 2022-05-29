#!/usr/bin/env python
# coding: utf-8
q1-
ineuron
ineuron ineuron
ineuron ineuron ineuron
ineuron ineuron ineuron ineuron

q2-
		ineuron
	ineuron		ineuron
ineuron		ineuron		ineuron
	ineuron		ineuron
		ineuron

l=[[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7) ,set([23,4,5,45,4,4,5,45,45,4,5]),
{'k1' :"sudh”, 'k2' : “ineuron”, "k3":"kumar",3:6, 7:8},
["ineuron” , “data science"]]

q3:Try to extract all the List entity
q4: Try to extract all the dict enteties
q5: Try to extract all the tuples entities
q6:Try to extract all the numerical data it may b a part of dict key and values
q7:Try to give sumation of all the numeric data
q8:Try to Filler out all the odd values out all numerLe data which is a part of a List
q9:Try to extract "ineuron” out oF this data
q10:Try to Find out a miner of occurances of all the ata
q11:Try to find out number of keys an dict element
q12:Try to filter our sll the string data
q13:Try to Find out alphanun in data
q14:Try to find out multiplication of all mumeric value in the individual collection inside dataset
q15:Try to unwrap all the collection inside collection and create a flat List,

 

before 29th may 2022 3 PM IST you have to send an answer to me or to shivan
 sudhanshu@ineuron.ai
 shivan@ineuron.ai
# In[43]:


#q1
n = input("Enter number of rows\t")
print("\n")
for i in range(int(n)) :
    for j in range(i+1) :
        print("ineuron" , end="\t")
    print("\n")


# In[72]:


#q2
d = input("Enter odd number of rows\t")
r = int(d)
n = int((r+1)/2)
for i in range(r):
    if i<n:
        for j in range(n-1-i):
            print("      ",end="\t")
        for k in range(i+1):
            if k%2==0 or k==0:
                print("ineuron",end="\t")
            else:
                print("      ",end="\t")
        for l in range(i):
            if i%2==0:
                if l%2==0 or l==0:
                    print("      ",end="\t")
                else:
                    print("ineuron",end="\t")
            else:
                if l%2==0 or l==0:
                    print("ineuron",end="\t")
                else:
                    print("      ",end="\t")
        print("\n")
    if i>=n:
        for j in range(i-n+1):
            print("      ",end="\t")
        for k in range(r-i):
            if k%2==0 or k==0:
                print("ineuron",end="\t")
            else:
                print("      ",end="\t")
        for l in range(r-i):
            if i%2==0:
                if l%2==0 or l==0:
                    print("      ",end="\t")
                else:
                    print("ineuron",end="\t")
            else:
                if l%2==0 or l==0:
                    print("ineuron",end="\t")
                else:
                    print("      ",end="\t")
        print("\n")


# In[74]:


l=[[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7) ,set([23,4,5,45,4,4,5,45,45,4,5]),
{'k1' :"sudh", 'k2' : "ineuron", "k3":"kumar",3:6, 7:8},
["ineuron" , "data science"]]


# In[75]:


l


# In[76]:


#q3
for i in l:
    if type(i)==list:
        print(i)


# In[77]:


#q4
for i in l:
    if type(i)==dict:
        print(i)


# In[78]:


#q5
for i in l:
    if type(i)==tuple:
        print(i)


# In[82]:


#q6
l1 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i:
            if type(j) == int:
                l1.append(j)
    if type(i) == dict:
        for k,v in i.items():
            if type(k) == int:
                l1.append(k)
            if type(v) == int:
                l1.append(v)
        
print(l1)           


# In[84]:


#q7
sum=0
for i in l1:
    sum+=i
sum


# In[87]:


#q8
l2 = []
for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == int:
                if j%2 != 0:
                    l2.append(j)
print(l2)


# In[89]:


#q9
l3 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i:
            if j == "ineuron":
                l3.append(j)
    if type(i) == dict:
        for k,v in i.items():
            if k == "ineuron":
                l3.append(k)
            if v == "ineuron":
                l3.append(v)
        
print(l3)         


# In[96]:


#q10
l5 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i:
            l5.append(j)
    if type(i) == dict:
        for k,v in i.items():
            l5.append(k)
            l5.append(v)
print(l5) 

for i in set(l5):
    print(i,":",l5.count(i))


# In[103]:


#q11
for i in l :
    if type(i) == dict :
        print(i.keys(),"->",len(i),"keys")


# In[105]:


#q12
l6=[]
for i in l5 :
    if type(i) == str:
        l6.append(i)
print(l6)
        


# In[109]:


#q13
for i in l5 :
    if type(i)==str:
        if i.isalnum:
            print(i)
        


# In[113]:


#q14
p1=1
p2=1
p3=1
p4=1

for i in l:
    if type(i) == list: #or type(i) == tuple or type(i) == set:
        for j in i:
            if type(j) == int:
                p1*=j
    if type(i) == tuple:
        for j in i:
            if type(j) == int:
                p2*=j
    if type(i) == set:
        for j in i:
            if type(j) == int:
                p3*=j
    if type(i) == dict:
        for k,v in i.items():
            if type(k) == int:
                p4*=k
            if type(v) == int:
                p4*=v
        
print("p1=",p1,"p2=",p2,"p3=",p3,"p4=",p4)  


# In[114]:


#q15
l8 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i:
            l8.append(j)
    if type(i) == dict:
        for k,v in i.items():
            l8.append(k)
            l8.append(v)
print(l8) 


# In[ ]:





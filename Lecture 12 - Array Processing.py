
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[4]:


points=np.arange(-5,5,0.01)


# In[5]:


dx,dy=np.meshgrid(points,points)


# In[6]:


dx


# In[7]:


dy


# In[8]:


z=(np.sin(dx)+np.sin(dy))
z


# In[10]:


plt.imshow(z)


# In[11]:


plt.imshow(z)
plt.colorbar()

plt.title('Plot for sin(x)+sin(y)')


# In[24]:


#numpy where
A=np.array([100,200,300,400])
B=np.array([1,2,3,4])


# In[25]:


condition=np.array([True,True,False,False])


# In[26]:


answer =[(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)] 


# In[27]:


answer


# In[28]:


answer2=np.where(condition,A, B)


# In[29]:


answer2


# In[30]:


from numpy.random import randn


# In[31]:


arr=randn(5,5)
arr


# In[32]:


np.where(arr<0,0,arr)


# In[34]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr


# In[37]:


arr.sum(0)

arr.sum()
# In[38]:


arr.sum()


# In[39]:


arr.mean()


# In[40]:


arr.std()


# In[41]:


arr.var()


# In[42]:


bool_arr=np.array([True, False, True])


# In[43]:


bool_arr.any()


# In[44]:


bool_arr.all()


# In[46]:


#Sort
arr=randn(5)
arr


# In[48]:


arr.sort()
arr


# In[49]:


countries = np.array(['France','Germany', 'USA','Russia','USA','Mexico','Germany'])


# In[50]:


np.unique(countries)


# In[51]:


np.in1d(['France','USA','Sweden'], countries)


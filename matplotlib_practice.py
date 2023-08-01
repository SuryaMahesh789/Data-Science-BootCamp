import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]


# plt.plot(x,y)
# plt.show()

# plt.plot(x,y,color='green')
# plt.show()


# plt.plot(x,y,color='green',linewidth=5)
# plt.show()


# plt.plot(x,y,color='green',linewidth=5,linestyle='dotted')
# plt.show()

# plt.title('Weather')
# plt.xlabel('Day')
# plt.ylabel('Temperature')
# plt.plot(x,y,color='green',linewidth=5)
# plt.show()


# plt.plot(x,y,'g+')
# plt.show()


# plt.plot(x,y,'+')
# plt.show()


# plot with dashed lines
# plt.plot(x,y,'--')
# plt.show()

# red dashed lines
# plt.plot(x,y,'r--')
# plt.show()


# red diamonds
# plt.plot(x,y,'rD')
# plt.show()

# plot with red stars
# plt.plot(x,y,'r*')
# plt.show()


# plot with red stars and dashed lines
# plt.plot(x,y,'r*--')
# plt.show()


# plot with red stars and dashed lines
# plt.plot(x,y,color='red',marker='*',linestyle='dashed')
# plt.show()

#
# # plot with red stars and dashed lines
# plt.plot(x,y,color='red',marker='*',linestyle='--')
# # plt.show()


# # plot with red plus and dashed lines
# plt.plot(x,y,color='red',marker='+',linestyle='--')
# plt.show()



# plot with red plus and dashed lines
# plt.plot(x,y,color='red',marker='+',linestyle='',markersize=20)
# plt.show()


# alpha is opacity factor
# plt.plot(x,y,color='red',alpha=1)
# plt.show()


# plt.plot(x,y,color='red',alpha=0.5)
# plt.show()


# bar chart


days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]



# plt.title("weather")
# plt.xlabel('Days')
# plt.ylabel('Temperature')
# plt.plot(days,max_t,label='max')
# plt.plot(days,min_t,label='min')
# plt.plot(days,avg_t,label='avg')
# # plt.legend(loc='best')
# plt.legend(loc='best',shadow=True)
# plt.grid()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

company=['GOOGLE','AMAZON','MSFT','FB']
revenue=[90,87,100,120]

ypos=np.arange(len(company))
print(ypos)

# plt.bar(ypos,revenue)
# plt.show()

# plt.bar(company,revenue)
# plt.show()


# plt.xticks(ypos,company)
# plt.ylabel("REVENUE")
# plt.title("US TECH STOCKS")
# plt.bar(ypos,revenue,label="revenue")
# plt.legend(loc="best")
# plt.show()


company=['GOOGLE','AMAZON','MSFT','FB']
revenue=[90,87,100,120]
profits=[40,2,34,12]

# plt.title("US TECH STOCKS")
# plt.xticks(ypos,company)
# plt.ylabel("revenue")
# plt.bar(ypos-0.2,revenue,width=0.4,label="revenue")
# plt.bar(ypos+0.2,profits,width=0.4,label="Profit")
# plt.legend(loc="best")
# plt.show()


blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
# plt.title("Hospital Management")
# plt.hist(blood_sugar)
# plt.show()


# plt.hist(blood_sugar,bins=3,rwidth=0.75)
# plt.show()

#
# plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.75,color="green")
# plt.show()\


men=[1,2,3,4,5,6,7,8,9]
women=[11,12,13,14,15,16,17,18,19]

# plt.title("bloood-sugar level")
# plt.xlabel('sugar range')
# plt.hist([men,women])
# plt.show()


# pie chart

exp_vals=[1400,600,300,410,250]
exp_labels=['Home rent','Phone/Internet Bill','Food Bill','Car','Others']

# plt.title("Expenditure Per Month")
# plt.axis("equal")
# plt.pie(exp_vals,labels=exp_labels)
# plt.show()


# plt.title("Expenditure Per Month")
# plt.axis("equal")
# plt.pie(exp_vals,labels=exp_labels,radius=0.75)
# plt.show()


# to represent perecentage upto 2 decimals
# plt.title("Expenditure Per Month")
# plt.axis("equal")
# plt.pie(exp_vals,labels=exp_labels,radius=0.75,autopct='%.2f%%')
# plt.show()


# percentage with out decimals

plt.title("Expenditure Per Month")
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels,radius=0.75,autopct='%0.0f%%')
plt.show()

from tkinter import *
import numpy as np  
import pandas as pd
from PIL import ImageTk , Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
df_can = pd.read_excel('canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
df_country = list(df_can['OdName'])
print ('Data read into a pandas dataframe!')
years = list(map(str, range(1980, 2014)))    
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) # cleaning data
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True) #renaming columns
df_can['Total'] = df_can.sum(axis=1)    #total column
df_can.set_index('Country', inplace=True) 
df_can.columns = list(map(str, df_can.columns))
def top_five():
    df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True) #axis=0 means rows are sorted!! do remember that
    # get the top 5 entries
    df_top5 = df_can.head()
    # transpose the dataframe
    df_top5 = df_top5[years].transpose()
    df_top5.index = df_top5.index.map(int) # change the index values of df_top5 to type integer for plotting
    df_top5.plot(kind='area', 
                 stacked=False,
                 figsize=(13, 7), 
                 )
    plt.title('Immigration Trend of Top 5 Countries')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.show()
def haiti():    #Insight no.1
    haiti = df_can.loc['Haiti', years]
    haiti.index = haiti.index.map(int) #change the index values of Haiti to type integer for plotting
    haiti.plot(kind='line')
    plt.title('Immigration from Haiti')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    # annotate the 2010 Earthquake. 
    # syntax: plt.text(x, y, label)
    plt.text(2000, 6000, '2010 Earthquake') 
    plt.show()
def country():
    cn = variable.get()
    country = df_can.loc[cn , years]
    #country.index = country.index.map(int)
    country.plot(kind = 'line')
    title = "Immigration from "+cn
    plt.title(title)
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.show()
def iceland():  #insight no.2
    df_iceland = df_can.loc['Iceland' , years]
    df_iceland.plot(kind='bar', figsize=(10, 6), rot=90) 
    plt.xlabel('Year')
    plt.ylabel('Number of Immigrants')
    plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
    plt.annotate('',                      
                 xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',         # will use the coordinate system of the object being annotated 
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
                )
    plt.annotate('2008 - 2011 Financial Crisis', # text to display
                 xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
                 rotation=72.5,                  # based on trial and error to match the arrow
                 va='bottom',                    # want the text to be vertically 'bottom' aligned
                 ha='left',                      # want the text to be horizontally 'left' algned.
                )
    plt.show()
def word_cloud():
    total_immigration = df_can['Total'].sum()
    max_words = 90
    word_string = ''
    for country in df_can.index.values:
        if len(country.split(' ')) == 1:
            repeat_num_times = int(df_can.loc[country, 'Total']/float(total_immigration)*max_words)
            word_string = word_string + ((country + ' ') * repeat_num_times)
    wordcloud = WordCloud(background_color='white').generate(word_string)
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(14)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
def srilanka(): #insight no3
    srilanka = df_can.loc['Sri Lanka', years]
    srilanka.index = srilanka.index.map(int)
    srilanka.plot(kind = 'line')
    plt.title('Immigration from Sri Lanka')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.text (1982,11000,'Battle of Pooneryn')
    plt.show()
def usa():
    usa = df_can.loc['United States of America' , years]
    usa.index = usa.index.map(int)
    usa.plot(kind = 'line')
    plt.title('Immigration from United States of America')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.text(1997 , 10000 , 'Housing Market Crash')
    plt.text(1997 , 9000 , 'Financial Crisis')
    plt.show()
def singapore():
    sing = df_can.loc['Singapore' , years]
    sing.index = sing.index.map(int)
    sing.plot(kind = 'bar')
    plt.title('Immigration from Singapore')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.annotate('Post-Independence Recession', # text to display
                 xy=(11, 1200),                    # start the text at at point (year 2008 , pop 30)
                 rotation=0                 # based on trial and error to match the arrow
                )
    plt.show()
def insights():
    ins = variable1.get()
    if ins == 'Haiti':
        haiti()
    elif ins == 'Iceland':
        iceland()
    elif ins == 'Sri Lanka':
        srilanka()
    elif ins == 'United States of America':
        usa()
    elif ins == 'Singapore':
        singapore()
        
OPTIONS = ["Haiti" , "Iceland" , "Sri Lanka" , "United States of America" , "Singapore"]
gui=Tk()
gui.configure(background = "light green")
gui.title("Python Mini Project")
gui.geometry("700x500")
tit1 = Label(gui , text='Immigration to Canada from 1980 to 2013' , font = 'Helvetica 16 bold italic' , relief = 'groove' , padx = 10 , pady = 10 , cursor = "spider")
tit1.place(x = 150 ,  y = 0)
#Adding Image
path = "un.jpg"
img = ImageTk.PhotoImage(Image.open(path))
Label(gui , image = img).place(x = 0 , y= 50)
#Adding Image
h = Button(gui , text = "Immigration trend of top five countries " , command = top_five , font = 'Helvetica 10 bold')
h.place(x = 100 , y =350)
Label(gui , text='Country Name',font = 'Helvetica 10 bold').place(x = 0 , y = 250)
variable = StringVar(gui)
variable.set(df_country[0])
wwe = OptionMenu(gui , variable , *df_country)
wwe.place(x = 100 , y = 250)
button = Button(gui , text = "Plot" , command = country,font = 'Helvetica 10 bold')
button.place(x = 250 , y = 250)
variable1 = StringVar(gui)
variable1.set(OPTIONS[0])
qqe = OptionMenu(gui , variable1 , *OPTIONS)
qqe.place(x = 100 , y = 400)
Label(gui , text = 'Insights into ' , font = 'Helvetica 10 bold').place(x = 0 , y=400)
btt = Button(gui , text = "Show Insights" , command = insights , font = 'Helvetica 10 bold')
btt.place(x = 275 , y = 400)
wc = Button(gui , text = "Wordcloud" , command = word_cloud,font = 'Helvetica 10 bold')
wc.place(x=100 , y = 300)
gui.mainloop()

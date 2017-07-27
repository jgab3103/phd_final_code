import pandas as pd
import numpy as np
from matplotlib import *
from pylab import *




def createDataSet():
	""" create docs for fnction """
	unitsInQuarterBeat = 480
	secondsInOneMinute = 60

	kjAllTheThingsYouAre = pd.read_json('datasets/keithJarrettAllTheThingsYouAre.json')
	kjAllTheThingsYouAre['Quarter beats per minute'] = 240
	kjAllTheThingsYouAre['Duration of one second'] = (unitsInQuarterBeat * kjAllTheThingsYouAre['Quarter beats per minute']) / secondsInOneMinute
	kjAllTheThingsYouAre['Current location in seconds'] = kjAllTheThingsYouAre["Duration due to tied notes"] / kjAllTheThingsYouAre['Duration of one second']
	kjAllTheThingsYouAre["Current location in seconds"] = kjAllTheThingsYouAre["Current location in seconds"].cumsum()

	kjAutumnLeaves = pd.read_json('datasets/keithJarrettAutumnLeaves.json')
	kjAutumnLeaves['Quarter beats per minute'] = 240
	kjAutumnLeaves['Duration of one second'] = (unitsInQuarterBeat * kjAutumnLeaves['Quarter beats per minute']) / secondsInOneMinute
	kjAutumnLeaves['Current location in seconds'] = kjAutumnLeaves["Duration due to tied notes"] / kjAutumnLeaves['Duration of one second']
	kjAutumnLeaves["Current location in seconds"] = kjAutumnLeaves["Current location in seconds"].cumsum()

	kjGroovinHigh = pd.read_json('datasets/keithJarrettGroovinHigh.json')
	kjGroovinHigh['Quarter beats per minute'] = 240
	kjGroovinHigh['Duration of one second'] = (unitsInQuarterBeat * kjGroovinHigh['Quarter beats per minute']) / secondsInOneMinute
	kjGroovinHigh['Current location in seconds'] = kjGroovinHigh["Duration due to tied notes"] / kjGroovinHigh['Duration of one second']
	kjGroovinHigh["Current location in seconds"] = kjGroovinHigh["Current location in seconds"].cumsum()

	kjDaysOfWineOfRoses = pd.read_json('datasets/keithJarrettDaysOfWineAndRoses.json')
	kjDaysOfWineOfRoses['Quarter beats per minute'] = 240
	kjDaysOfWineOfRoses['Duration of one second'] = (unitsInQuarterBeat * kjDaysOfWineOfRoses['Quarter beats per minute']) / secondsInOneMinute
	kjDaysOfWineOfRoses['Current location in seconds'] = kjDaysOfWineOfRoses["Duration due to tied notes"] / kjDaysOfWineOfRoses['Duration of one second']
	kjDaysOfWineOfRoses["Current location in seconds"] = kjDaysOfWineOfRoses["Current location in seconds"].cumsum()

	kjIfIWereABell = pd.read_json('datasets/keithJarrettIfIWereABell.json')
	kjIfIWereABell['Quarter beats per minute'] = 240
	kjIfIWereABell['Duration of one second'] = (unitsInQuarterBeat * kjIfIWereABell['Quarter beats per minute']) / secondsInOneMinute
	kjIfIWereABell['Current location in seconds'] = kjIfIWereABell["Duration due to tied notes"] / kjIfIWereABell['Duration of one second']
	kjIfIWereABell["Current location in seconds"] = kjIfIWereABell["Current location in seconds"].cumsum()

	kjSomedayMyPrinceWillCome = pd.read_json('datasets/keithJarrettSomedayMyPrinceWillCome.json')
	kjSomedayMyPrinceWillCome['Quarter beats per minute'] = 240
	kjSomedayMyPrinceWillCome['Duration of one second'] = (unitsInQuarterBeat * kjSomedayMyPrinceWillCome['Quarter beats per minute']) / secondsInOneMinute
	kjSomedayMyPrinceWillCome['Current location in seconds'] = kjSomedayMyPrinceWillCome["Duration due to tied notes"] / kjSomedayMyPrinceWillCome['Duration of one second']
	kjSomedayMyPrinceWillCome["Current location in seconds"] = kjSomedayMyPrinceWillCome["Current location in seconds"].cumsum()

	kjStellaBeStarlight = pd.read_json('datasets/keithJarrettStellaByStarlight.json')
	kjStellaBeStarlight['Quarter beats per minute'] = 240
	kjStellaBeStarlight['Duration of one second'] = (unitsInQuarterBeat * kjStellaBeStarlight['Quarter beats per minute']) / secondsInOneMinute
	kjStellaBeStarlight['Current location in seconds'] = kjStellaBeStarlight["Duration due to tied notes"] / kjStellaBeStarlight['Duration of one second']
	kjStellaBeStarlight["Current location in seconds"] = kjStellaBeStarlight["Current location in seconds"].cumsum()

	data = pd.concat([kjAllTheThingsYouAre, 
	              kjAutumnLeaves,
	             kjGroovinHigh,
	             kjDaysOfWineOfRoses,
	             kjIfIWereABell,
	             kjSomedayMyPrinceWillCome,
	             kjStellaBeStarlight])
    
	return data
def calculateDensityOfPlayingPerMeasure(data, title):
    
    fig, axes = plt.subplots(nrows=1, ncols=2)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    
    
    secondYValue = data['Current measure'].max()
    nu = (data['Current measure'] * data['Midi number']).mean() - data['Current measure'].mean() * data['Midi number'].mean()
    de = (data['Current measure'] ** 2).mean() - data['Current measure'].mean() * data["Current measure"].mean()
    slope = nu/de
    intercept = data['Midi number'].mean() - (slope) * data['Current measure'].mean()
    otherY = slope * secondYValue + intercept
    
    data.plot(ax=axes[0], kind="scatter", x = "Current measure", y = "Midi number", title=title)
    axes[0].plot([0,secondYValue], [intercept,otherY])
    
    data['Midi number'].plot(ax=axes[1], kind="density", title="Frequency")
def listAllSolosWithDetail(data):
    x = data.groupby('Composer collection').sum()
    x = data[['Title', 'Composer name', 'Date recorded', 'Composer collection']].drop_duplicates()
    return x
def plotMidiNumbers(data):
    fig, axes = plt.subplots(nrows=3, ncols=2)
    fig.set_figheight(14)
    fig.set_figwidth(15)
    data[data['Title'] == 'All The Things You Are'][['Midi number']].plot(ax=axes[0,0], style='r', label='Series')
    axes[0,0].set_title('All The Things You Are')
    data[data['Title'] == 'Days Of Wine And Roses'][['Midi number']].plot(ax=axes[0,1]) 
    axes[0,1].set_title('Days Of Wine And Roses')
    data[data['Title'] == 'Groovin High'][['Midi number']].plot(ax=axes[1,0])
    axes[1,0].set_title("Groovin High")
    data[data['Title'] == 'If I Were A Bell'][['Midi number']].plot(ax=axes[1,1])
    axes[1,1].set_title("If I Were A Bell")
    data[data['Title'] == 'Someday my prince will come'][['Midi number']].plot(ax=axes[2,0])
    axes[2,0].set_title("Someday my prince will come")
    data[data['Title'] == 'Autumn Leaves'][['Midi number']].plot(ax=axes[2,1])
    axes[2,1].set_title("Autumn Leaves")

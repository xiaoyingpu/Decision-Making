# Decision-Making

## Concepts


- Decision-making and stress
- Implicit bias and IAT 
- Physiological data and machine learning


_Main Idea:_ use physiological data to classify user workload, so as to mitigate the effects of implicit bias in decision-making processes.

## Hypotheses 

- __H0:__ 
- __H1:__
- __H2:__



## Code

- [bucknell-hci/flyloop](https://gitlab.bucknell.edu/bucknell-hci/flyloop)
  - the physiological computing framework that collects, processes and classfifies data.
- [n-back](https://gitlab.bucknell.edu/xp002/n-back)
  - the working memory stressor that involves staring at picture stimuli.
- [empatica_connect](https://gitlab.bucknell.edu/xp002/empatica_connect)  
  - the Android application that
    - get data via bluetooth low energy from Empatica E4
    - send data to FlyLoop via mqtt messages.
- [mouse-tracker-matlab](https://gitlab.bucknell.edu/xp002/mouse-tracker-matlab)
  - MATLAB code from MouseTracker's example folder
  - this repo is not useful; compiling MATLAB into a JAR is not worth the trouble
  - MATLAB code has been manually translated into Java and included in `dm_task` repository.
- [dm_task](https://gitlab.bucknell.edu/xp002/mouse-tracker-matlab)
  - decision-making tasks
    - primary task is to click pictures / make decisions on MouseTracker (see below)
    - secondary task is digit-recall 
  
[__MouseTracker__](http://mousetracker.jbfreeman.net): non-opensource, free software developed by John Freeman.  

## Devices 

- Empatica E4
  - the wrist band
  - crater and USB cord
  - extra electrodes and the red box
  - for physiological data collection of course
- Professor Peck's Android phone
  - always turn on Wi-Fi and Bluetooth
- [Optional] get a Windows computer
  - MouseTracker needs to run on Windows



## Network dependency

- `mqtt.bucknell.edu` (134.82.56.50). Maintained by Professor Marchiori. 
- publish / subscribe 


## Experiment set-up

## More resources

### Presentations

- Susquehanna Valley Undergraduate Research Symposium
  - Oral presentation: ppt 
- Bucknell Engineering Research Symposium
  - Poster presentation: pdf


### Write-ups

- Hypotheses
- Schemas 

### bibtex dump

#### physiological computing overview

#### pretty related

#### stress and other psychology stuff

#### mousetracker

### Annotated bibliography dump

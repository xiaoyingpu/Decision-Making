# Bibliography section

- not all papers are useful
- below are highlights


## the driving paper

_Solovey, Erin T., et al. "Classifying driver workload using physiological and driving performance data: Two field studies." Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, 2014._

- Abstract
   - Cognitive load
   - Inclusion of physiological data leads to higher classification accuracy
   - Classifier used across individuals

- Intro
   - automatic cognitive workload classification
   - machine learning classification results
   - with details of the techniques
   - parameters for recognizing elevated cognitive load
   - comparing parameters for classification (which one is “better”?)
   - model training for across individuals

- Related Work
   - Autonomic nervous system
      - Sympathetic nervous system (SNS)
      - Parasympathetic nervous system (PNS)
   - Electrodermal activity (EDA)
      - SCL: skin conductance level
      - SCR: skin conductance response

> Linear discriminant function?

- Classifying driver data for UI evaluation
   - Preprocessing: manual or automatic cleaning of the input signals
   - Feature generation and feature selection
   - Which classification algorithm to use

- Experimental Framework
   - Machine learning algorithm
   - Window size
   - Overlap of windows
   - Features used

- Secondary Task Procedure
   - n-back (audio) ~ MIT AgeLab Delayed Digit Recall Task (n-back) REF
- Validation:
   - (auditory) perception, cognitive processing involving working memory
   - has been utilized as a calibration task
   - consistent, validated, high dosage of cognitive demand

   - Vehicle Equipment and Physiological Sensors

   - Physiological data ~ 250 Hz
   - EKG
   - Skin conductance (protocol, protocol, protocol….)
       - The thin surface, low-profile design of the electrodermal sensors minimize interference….
- Data Processing
   - Skin conductance
      - Filtered using a wavelet transform to remove high frequency noise [29] ~ GAZE
      - Gross low frequency movement artifact was identified by manual inspection and removed
- Feature Generation
   - Labeled dataset built from synchronized sensor data
   - Sliding window: aggregate attributes over specific time intervals
   - Each feature computed using a fixed-length sliding window operator
       - Features
           - Mean
           - Standard deviation
           - Minimum
           - Maximum
           - First derivative
       - For HR, EDA
       - Sliding window
           - Window size
           - Amount of overlap

- Experiment 1: Automatic classification of elevated workload in individual drivers

   - Procedure
       - Familiarization
       - 24 task periods of 2-back, 30-second ea.
       - 90 second recovery and baseline period
       - Throughout: data were logged
   - Classification approach and results
       - Individual classification method
           - 24 - 30 seconds of elevated cognitive load
           - 24 - 30 seconds of normal cognitive load (middle of recovery and baseline period)
       - (Inner)Ten-fold cross-validation
           - To choose the window size and window overlap TODO
       - bla bla bla
   - DISCUSSION
       - Reasonable accuracy with simple features and classification methods
       - Training time: too long???? (why??????????TODO)

- Experiment 2: Establishing methods across individuals

   - General classifiers: detect elevated cognitive workload without extensive training on individuals
   - Goal: find common features and algorithms that are reliable


=============

## IEEE Computer 

Evan M. Peck, Emily Carlin, Robert Jacob, "Designing Brain-Computer Interfaces for Attention-Aware Systems", Computer, vol.48, no. 10, pp. 34-42, Oct. 2015, doi:10.1109/MC.2015.315


Sioni, Riccardo, and Luca Chittaro. "Stress Detection Using Physiological Sensors." Computer 10 (2015): 26-33.




   
============

## Stress and limited cognitive resource


_Robert, G., and J. Hockey. "Compensatory control in the regulation of human performance under stress and high workload: A cognitive-energetical framework." Biological psychology 45.1 (1997): 73-93._

- Goal:
   - to confirm that cognitive resources are limited, and stress & high workload take up those limited resources
- Evidence:
  - Abstract

>"Regulation of goals and actions” … “allocates resources dynamically."
> The controllers for the resource allocation have "different modes of performance-cost trade-off:

- Performance maintained under stress, at the cost of 

> "increased efforts", and other "behavioral and physiological costs"

- “Performance goals” reduced, with no extra costs

- Introduction:

> “Intimate relationship between behavior and its biological / motivational context"

  - def. Cognitive energetics:
    - computational models of human information processing need biological context of behavior, too.
    - Need energy-based constructs into information processing models

  - def. compensatory control: 
    - accounts for patterns of performance under stress and high workload
  - Energetical processes, information processing models —> generalized control model

- 1.1 Resources and effort
  - def. resources: 
    - has roots in: information processing and energetic theories; dual-task performance
  - Capacity theories
    - common energy sources

__Hindsight:__ paper bit old; still valid?

--------------------------

## Report on implicit bias

_State of the Science: Implicit Bias Review 2015_

- p.9
  - Cognitive control may be impeded by circumstance such as high cognitive load.
- p.19
  - .... research that demonstrates the correlation among high levels of cognitive load,s high stress environments and the reliance on automatic or unconscious processes in which stereotypes and unconscious beliefs are more likely to be activated.

- p.21
  - Implicit association test (IAT)
  - Trauma surgeons work in high-stress, time constrained, and high mental and physical fatigue environments - environments in which implicit bias can impact judgments and decision-making.
    - (Haider et. al., 2014) Haider, Adil H., et al. "Association of unconscious race and social class bias with vignette-based clinical assessments by medical students." JAMA 306.9 (2011): 942-951.
    - In this study, these biases were not statistically significantly associated with clinical decision making.
- p.66
  - Engaging in deliberative processing can help counter implicit biases, particularly during situations in which decision-makers may face time constraint or a weighty cognitive load (4 ref's).

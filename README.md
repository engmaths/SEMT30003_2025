# SEMT30004 Computational Neuroscience

This course is in draft mode. 
Specifics will change. 

## Structure

#### Unit & assessment variants
 - CS minor: *Topics in Computer Science* exam question (lectures & labs weeks 1–8).
 - SEMT: 50% Final (lectures & labs weeks 1–8), 50% extended coursework (weeks 9–11)

#### Every week...
 - **Weeks 1–8 (with reading-week break):** 2×1-hour lectures, 1-hour lab (← ask TAs questions here)
 - **Weeks 9–11:** One 2-hour coursework support session with TAs

Selected past exams are in the [past Exams](Past%20Exams/) folder. Some previous incarnations of this course are on Github: [[2024]](https://github.com/engmaths/SEMT30003_2024) [[2022]](https://github.com/LaurenceA/COMS30017_2022) [[2021]](https://github.com/LaurenceA/COMS30017_2021) [[2018–19]](https://github.com/coms30127/2018_19) [[2013–17]](https://github.com/conorhoughton/COMS30127). 

#### Scheduled topics: 

|                 | Topic  |
| --------------- | ------ |
| **Week 1:**     | Introduction to neuroscience \& other background material  |
| **Week 2:**     | The action potential (spikes)  |
| **Week 3:**     | Synaptic communication   |
| **Week 4:**     | Synaptic plasticity 1: Cerebellum \& perceptron  |
| **Week 5:**     | Synaptic plasticity 2: Hippocampus \& Hopfield   |
|                 | (break for reading week)  |
| **Week 6:**     | Rate models and vision  |
| **Week 7:**     | Statistical models and data analysis  |
| **Weeks 8–10:** | Extended coursework  |
 
#### Textbooks and Reading

Course material will be accompanied by reading or exercises taken from
 - [*Conor Houghton's Coursenotes*](https://github.com/engmaths/SEMT30003_2025/tree/main/Reading/Coursenotes)
 - [*Neuronal Dynamics*](https://github.com/engmaths/SEMT30003_2025/tree/0dcbfcdf57382e98b2054f2414ca6214bb8f4903/Reading/Textbooks) (Gerstner, Kistler, Naud, Paninski)  [[website]](https://neuronaldynamics.epfl.ch/index.html) [[PDF access]](https://www.cambridge.org/core/books/neuronal-dynamics/75375090046733765596191E23B2959D)
 - [*Theoretical Neuroscience*](https://github.com/engmaths/SEMT30003_2025/blob/62506c4a0fe3408e39848cc2b2f8fd9cc7ccbb43/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20neuroscience%20computational%20and%20mathem.pdf) (Abbott, Dayan) [[alt1]](https://drive.google.com/file/d/0B9bX852JMJ__YTYzNWQ0ZmItYmU0MS00NjZmLTk1MTYtZTQ0ZDVlNDMxMDJj/view?resourcekey=0-VbLeRG9RwR4WHuVI5sA1PQ) [[individual chapters]](https://github.com/engmaths/SEMT30003_2025/tree/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters)

Curious students may optionally glance through these texts: 
 - [*Dynamical Systems in Neuroscience*](https://github.com/engmaths/SEMT30003_2025/blob/62506c4a0fe3408e39848cc2b2f8fd9cc7ccbb43/Reading/Textbooks/Dynamical%20Systems%20in%20Neuroscience%20-%20Izhikevich.pdf) (Izhikevich); [[alt1]](https://www.izhikevich.org/publications/dsn.pdf)  [[alt2]](https://labs.ni.gsu.edu/ashilnikov/teaching/fall2008/8515/izhikevich.pdf)  
 - [*Mathematical foundations of neuroscience*](https://github.com/engmaths/SEMT30003_2025/blob/d65197c56d97baa99aa1e281817322a3e5f5f60a/Reading/Textbooks/mathematical%20foundations%20of%20neuroscience-Ermentrout.pdf) (Ermentrout, Terman); [[alt1]](https://neurophysics.ucsd.edu/courses/physics_171/Ermentrout_Therman.pdf) [[alt2]](https://www.seti.net/Neuron%20Lab/NeuronReferences/mathematical%20foundations%20of%20neuroscience-Ermentrout.pdf) 
 - [*Mathematical Physiology 1: Cellular Physiology*](https://github.com/engmaths/SEMT30003_2025/blob/041d4cd1eb05e184b20899216bb514f257e10db5/Reading/Textbooks/Keener%20and%20Sneyd%20Mathematical%20Physiology%201%20Cellular%20Physiology.pdf) (Keener, Sneyd); [[alt1]](http://users.df.uba.ar/silvina/fisica_biologica/biochemical_reactions_Keener_Sneyd_Mathematical_Physiology_I_Cellular_Physiology_2009.pdf) [[alt2]](https://ftp.rush.edu/users/molebio/Bob_Eisenberg/CV%20on%20moleobio-Bob_Eisenberg/__Fragments%20and%20Ideas/Flux%20Ratio/Kenner%20and%20Sneyd%20Independence%20from%20Mathematical%20Physiology.pdf) 
 - *Methods in Neuronal Modelling* (Koch, Segev)
 - [*Spikes*](https://github.com/engmaths/SEMT30003_2025/blob/983a7ca443de65c4e9705fdd2bac9e16d6042cc4/Reading/Textbooks/Spikes.pdf) (Rieke, Warland, van Steveninck, Bialek)
 - [*The Matrix Cookbook*](https://github.com/engmaths/SEMT30003_2025/blob/983a7ca443de65c4e9705fdd2bac9e16d6042cc4/Reading/Textbooks/Petersen%20and%20Pedersen%20-%20The%20Matrix%20Cookbook.pdf) (Petersen and Pedersen)

--------------------------------------------------------------------------------
# Course Content

We will update this section as term progresses. 

Legend for course readings
 - ❗🧠 = These course notes will be on the exam. **If you read nothing else, read these and the annotated lecture slides before the exam!**
 - 📚 = Supplemental reading: These textbook chapters cover course content in a different way. You might find them more accessible.
 - 📜 = Optional enrichment: These readings exceed the technical depth on our exam, but you may find them interesting.

## Week 1
|                 |      |
| --------------- | ---- |
| **► Lecture 1** | Welcome to this course ([draft](Slides/week1/01100_welcome_and_overview.pdf), annotated TBD)
|                 | Overview of selected anatomy ([draft](Slides/week1/01200_brain_anatomy.pdf), annotated TBD)
|                 | Neurons ([draft](week1/01300_neurons.pdf), annotated TBD)
|                 | Action potentials (spikes) ([draft](Slides/week1/01400_action_potential.pdf), annotated TBD)
| *Reading*       |
||❗🧠Coursenotes     [neurons](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.1_neurons.pdf), [cortex](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.4_cortex.pdf), [basal_ganglia](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.5_areas.pdf)
||📚Dayan & Abbott    [1.1: Properties of Neurons (pg. 4-6)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_01_Neural_Encoding_I.pdf)
|                 |      |
| **► Lecture 2** | Nernst potential and membrane voltage ([draft](Slides/week1/01500_Nernst_potential.pdf), annotated TBD)
|                 | The circuit for a passive membrane ([draft](Slides/week1/01600_passive_membrane_circuit.pdf), annotated TBD)
|                 | Differential equations & numerics ([draft](Slides/week1/01700_ODEs.pdf), annotated TBD)
| *Reading*       |
||📚Neuronal Dynamics  [2.1: Equilibrium potential](https://neuronaldynamics.epfl.ch/online/Ch2.S1.html)
||📚Dayan & Abbott    [5.1-5.2: Electrical Properties of Neurons (pg. 153-161)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
|||
|► **Lab 1** | [Welcome, setup, prerequisites, and notation](Labs/lab1) | 
|| *(prerequisite review)* ❗🧠Coursenotes     [maths](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/02.2_maths.pdf), [numerical methods](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/02.3_numerical.pdf), [computing](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/02.1_computing.pdf)
|| *(prerequisite review)* Dayan & Abbott    [Appendices A.3, A.4 (pg. 410-415)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_11_Appendix.pdf)


## Week 2
|                 |      |
| --------------- | ---- |
| **► Lecture 3** | Models ([draft](Slides/week2/02100_models.pdf), annotated TBD)
|                 | LIF ([draft](Slides/week2/02200_LIF.pdf), annotated TBD)
|                 | Ion channels ([draft](Slides/week2/02300_ion_channels_and_voltage_gating.pdf), annotated TBD)
| *Reading*       |
||❗🧠Coursenotes     [bucket equation](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/05.1_bucket_equation.pdf), [integrate and fire](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/05.2_integrate_and_fire.pdf)
||📚Neuronal Dynamics  [1.3 Integrate-And-Fire Models up through 1.3.3](https://neuronaldynamics.epfl.ch/online/Ch1.S3.html)
||📚Dayan & Abbott    [5.3: Single-Compartment Models (pg. 161-162)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
||📚Dayan & Abbott    [5.4: Integrate-and-Fire Models (pg. 162-166)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
||📚Dayan & Abbott    [5.5: Voltage-Dependent Conductances (pg. 166)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
|| 📜 Neuronal Dynamics  [1.4 Limitations of the Leaky Integrate-and-Fire Model](https://neuronaldynamics.epfl.ch/online/Ch1.S4.html)
|| 📜 Neuronal Dynamics  [5.3 Quadratic Integrate and Fire](https://neuronaldynamics.epfl.ch/online/Ch5.S3.html)
|                 |      |
| **► Lecture 4** | The Hodgkin-Huxley Model ([draft](Slides/week2/02400_Hodgkin_Huxley_and_conductance_based_spike_models.pdf), annotated TBD)
|                 | Intracellular electrophysiology and voltage clamp ([draft](Slides/week2/02500_voltage_clamp_and_intracellular_electrophysiology.pdf), annotated TBD)
| *Reading*       | 
||❗🧠Coursenotes      [Hodgkin Huxley](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/07.1_Hodgkin_Huxley.pdf), [recordings: in vitro/vivo electrophysiology (pg 2–4)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.6_recordings.pdf)
||📚Neuronal Dynamics  [2.2: Hodgkin-Huxley Model](https://neuronaldynamics.epfl.ch/online/Ch2.S2.html)
||📚Dayan & Abbott    [5.6: The Hodgkin-Huxley Model (pg. 173-175)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
||📚Dayan & Abbott    [5.7: Modeling Channels (pg. 175)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
|||
|► **Lab 2** | [Simulate a Leaky Integrate and Fire (LIF) neuron](Labs/lab2) | 

## Week 3
|                 |      |
| --------------- | ---- |
| **► Lecture 5** | Synapses overview
|                 | Short-term plasticity
|                 | Ionotropic receptors & PSPs
|                 | Types of synapses and neurotransmitters
| *Reading*       |
||❗🧠Coursenotes     [synapses](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.2_synapses.pdf), [synaptic dynamics](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/06.1_synaptic_dynamics.pdf), [types](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/01.3_types.pdf)
||📚Neuronal Dynamics [3.1 Synapses](https://neuronaldynamics.epfl.ch/online/Ch3.S1.html)
||📚Dayan & Abbott   [5.8: Synaptic Conductances (pg. 178-188)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
|                 |      |
| **► Lecture 6** | Modelling a synapse
|                 | Synaptic and dendritic integration
|                 | Multi-compartment models and the cable equation
| *Reading*       |
||📚Dayan & Abbott [5.9: Synapses on Integrate-and-Fire Neurons (pg. 188-191)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_05_Model_Neurons_I.pdf)
||📚Dayan & Abbott [6.3-6.4: The Cable Equation, Multi-compartment Models (pg. 203-224)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_06_Model_Neurons_II.pdf)
||📚Neuronal Dynamics [3.2.1 Spatial Structure](https://neuronaldynamics.epfl.ch/online/Ch3.S2.html) (skip 3.2.2, 3.2.3)
||📚Neuronal Dynamics [3.3 Spatial Structure: Axons](https://neuronaldynamics.epfl.ch/online/Ch3.S3.html) (skip 3.3.2)
|||
|► **Lab 3** | [Explore the Hodgkin–Huxley action potential model](Labs/lab3) | 

## Week 4
|                 |      |
| --------------- | ---- |
| **► Lecture 7** | Neuroplasticity overview
|                 | Hebbian learning
|                 | McCulloch–Pitts neurons
| *Reading*       |
||❗🧠Coursenotes     [synaptic_plasticity](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/06.2_synaptic_plasticity.pdf), [mp_neurons](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/03.1_mp_neurons.pdf)
||📚Neuronal Dynamics [19.1 Hebb rule and experiments](https://neuronaldynamics.epfl.ch/online/Ch19.S1.html)
||📚Dayan & Abbott   [8.1: Introduction to Plasticity (pg. 281-284)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_08_Plasticity_and_Learning.pdf)
||📚Dayan & Abbott   [8.2: Synaptic Plasticity Rules (pg. 284-293)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_08_Plasticity_and_Learning.pdf)
|                 |      |
| **► Lecture 8** | Cerebellum
|                 | The delta rule
|                 | The perceptron
| *Reading*       |
||❗🧠Coursenotes [cerebellum](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/03.5_cerebellum.pdf), [perceptron](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/03.4_perceptron.pdf)
||📚Dayan & Abbott [8.4: Supervised Learning (pg. 313-326)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_08_Plasticity_and_Learning.pdf)
|||
|► **Lab 4** | [Simulate a phenomenological model of a chemical synapse](Labs/lab4)|

## Week 5
|                 |      |
| --------------- | ---- |
| **► Lecture 9** | Hippocampus overview
|                 | Navigation
|                 | Memory and the trisynaptic circuit
| *Reading*       |
||❗🧠Coursenotes     [hippocampus](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/03.3_hippocampus.pdf)
||📚Neuronal Dynamics [17.1.1 Recall, recognition](https://neuronaldynamics.epfl.ch/online/Ch17.S1.html)
||📚Neuronal Dynamics [17.1.2 Neuronal assemblies](https://neuronaldynamics.epfl.ch/online/Ch17.S1.html)
||📜Neuronal Dynamics [17.1.3 Working memory](https://neuronaldynamics.epfl.ch/online/Ch17.S1.html)
|                 |      |
| **► Lecture 10**  | Pattern separation and dentate gyrus
|                 | Hopfield networks
|                 | Stable Hebbian learning rules
| *Reading*       |
||❗🧠Coursenotes [hopfield](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/03.2_hopfield.pdf)
||📚Neuronal Dynamics [17.2 Hopfield Model](https://neuronaldynamics.epfl.ch/online/Ch17.S2.html)
||📚Neuronal Dynamics [19.2.1/2 Hebb's Rule & STDP](https://neuronaldynamics.epfl.ch/online/Ch19.S2.html)
|| 📜 Neuronal Dynamics [19.4 Reward-based learning](https://neuronaldynamics.epfl.ch/online/Ch19.S4.html)
||📚Dayan & Abbott [7.4: Network Stability & Associative Memory (pg. 260-265)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_07_Network_Models.pdf)
||📚Dayan & Abbott [8.3: Synaptic normalization (pg. 289-291)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_08_Plasticity_and_Learning.pdf)
|||
|► **Lab 5** | [McCulloch–Pitts neurons and perceptron](Labs/lab5)|


## Week 6
|                 |      |
| --------------- | ---- |
| **► Lecture 11**  | rate models of tuning
|                 | vision I: overview
|                 | vision II: retina
|                 | vision III: topographic maps
| *Reading*       |
||📚Neuronal Dynamics [7.6 The Problem of Neural Coding (through 7.6.2)](https://neuronaldynamics.epfl.ch/online/Ch7.S6.html)
||📚Neuronal Dynamics [12.1 Columnar organization](https://neuronaldynamics.epfl.ch/online/Ch12.S1.html)
||📚Dayan & Abbott [1.2-1.3: Firing Rates (pg. 8-24)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_01_Neural_Encoding_I.pdf)
||📚Dayan & Abbott [2.3, 2.6: Early Visual System, Retinal/LGN Receptive Fields (pg. 51, 77)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_02_Neural_Encoding_II.pdf)
|                 |      |
| **► Lecture 12**  | vision IV: cortical hierarchy
|                 | vision V: sparse coding
|                 | V1 laminar structure and the cortical microcircuit
| *Reading*       |
||❗🧠Coursenotes [vision](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Coursenotes/04.2_vision.pdf)
||📚Dayan & Abbott [2.7: Constructing V1 Receptive Fields (pg. 79-81)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_02_Neural_Encoding_II.pdf)
||📚Dayan & Abbott [10.4: Discussion (on sparse coding) (pg. 389-394)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_10_Representational_Learning.pdf)
|||
|► **Lab 6** | [Hopfield networks](Labs/lab6)|

## Week 7
|                 |      |
| --------------- | ---- |
|**► Lecture 13** | Wilson–Cowan models
|                 | Neural fields
|                 | Continuous attractors
| *Reading*       |
||📚Neuronal Dynamics [Ch 18 Cortical Field Models](https://neuronaldynamics.epfl.ch/online/Ch18.html) (notation differs)
||📚Neuronal Dynamics [18.3 Bump attractors](https://neuronaldynamics.epfl.ch/online/Ch18.S3.html)
||📚Dayan & Abbott [7.2: Firing-Rate Models (pg. 231)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_07_Network_Models.pdf)
||📚Dayan & Abbott [7.4: Recurrent Networks (pg. 247-252)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_07_Network_Models.pdf)
|| 📜Dayan & Abbott  [7.5: Excitatory-Inhibitory Networks (pg. 265)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_07_Network_Models.pdf)
|                 |      |
| **► Lecture 14**  | Extracellular recording
|                 | Statistical analysis of spiking data
| *Reading*       |
||📚Neuronal Dynamics  [11.2 Encoding Models in Systems Neuroscience](https://neuronaldynamics.epfl.ch/online/Ch11.S2.html)
||📚Dayan & Abbott    [1.4: Spike-Train Statistics (pg. 24-34)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_01_Neural_Encoding_I.pdf)
|                 | [2.2, 2.4: Estimating Firing Rates, Reverse-Correlation (pg. 45-51, 60-74)](https://github.com/engmaths/SEMT30003_2025/blob/main/Reading/Textbooks/Dayan%20and%20Abbott%20-%202001%20-%20Theoretical%20Neuroscience%20chapters/Dayan_and_Abbot_02_Neural_Encoding_II.pdf)
|||
|► **Lab 7** | There is no lab 7, but but these [demo notebooks](Labs/lab7) may interest you.|











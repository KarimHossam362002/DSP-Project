# Digital Signal Processing (DSP) Project

## Course Project Overview
This project explores fundamental concepts of Digital Signal Processing (DSP), from basic signal representation to advanced frequency domain operations. By completing this project, you will develop a comprehensive understanding of signal processing techniques used in real-world applications.

---

## Project Milestones

### **Milestone 1: Signal Representation, Sampling, and Quantization**
#### Goal:
Understand how to create, sample, and quantize signals as the foundation for all subsequent processing.

#### Tasks:
1. **Generate and Plot Signals**:
   - **Sinusoidal Wave**: Visualize continuous and discrete sinusoidal waves to understand periodic signals.
   - **Square Wave**: Compare square waves with sinusoidal waves, understanding their application in digital systems.
   - **Real-world Signals**: Import and plot real-world data from external files.
   - **Custom Equations**: Generate and plot signals based on mathematical equations. *(Task not completed yet.)*

2. **Sampling**:
   - Apply a specified sampling rate to continuous signals, illustrating aliasing and the impact of sampling.

3. **Quantization**:
   - Quantize sampled signals using specified quantization levels, exploring how resolution reduction introduces quantization noise.

#### Outcome:
A set of signals ready for enhancement and noise reduction in **Milestone 2**.

---

### **Milestone 2: Signal Enhancement through Smoothing and Noise Reduction**
#### Goal:
Improve signal quality by reducing noise and enhancing smoothness.

#### Tasks:
1. **Moving Average Filter (Smoothing)**:
   - Apply a moving average filter to reduce high-frequency noise.

2. **Noise Reduction**:
   - Use techniques like low-pass filtering to produce cleaner signals.

#### Outcome:
Enhanced signals prepared for convolution and correlation in **Milestone 3**.

---

### **Milestone 3: Signal Manipulation with Convolution and Correlation**
#### Goal:
Combine and compare signals using convolution and correlation.

#### Tasks:
1. **Convolution**:
   - Perform convolution between two signals to understand filtering and signal combination.

2. **Correlation**:
   - Calculate the correlation between two signals to measure similarity, useful for pattern recognition and signal matching.

#### Outcome:
Processed signals for frequency domain filtering in **Milestone 4**.

---

### **Milestone 4: Frequency Domain Filtering**
#### Goal:
Analyze and shape signals using frequency domain filters.

#### Tasks:
1. **Frequency Domain Filters**:
   - **Low Pass Filter**: Retain low frequencies, removing high-frequency noise. *(Cutoff frequency: 5 Hz)*
   - **High Pass Filter**: Preserve high frequencies, removing low-frequency drift. *(Cutoff frequency: 5 Hz)*
   - **Band Pass Filter**: Allow frequencies between 3 Hz and 8 Hz, attenuating others.
   - **Band Reject Filter**: Attenuate frequencies between 3 Hz and 8 Hz, allowing others to pass.

#### Outcome:
Mastery of filtering techniques essential for advanced DSP operations.

---

## Conclusion
This project provides hands-on experience with DSP techniques like signal generation, sampling, quantization, smoothing, noise reduction, and filtering. These foundational skills are valuable for real-world applications such as communications, audio processing, and image analysis.

---

## Project Structure
- **Milestone1/**: Signal representation, sampling, and quantization code.
- **Milestone2/**: Signal enhancement and noise reduction implementations.
- **Milestone3/**: Convolution and correlation operations.
- **Milestone4/**: Frequency domain filtering scripts.

---

## How to Run the Project
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/dsp-project.git
   cd dsp-project
2. Install dependencies:
   ```bash
   pip install numpy,matplotlib,scipy
3. Run individual milestones:
   ```bash
   python Milestone1/TASK#_NAME.py
   python Milestone2/TASK#_NAME.py    
   python Milestone3/TASK#_NAME.py
   python Milestone4/TASK#_NAME.py


### Instructions:
- Replace `https://github.com/your-repo/dsp-project.git` with your GitHub repository link.
- Customize sections as needed to suit your project!

##Feel free to contribute by submitting pull requests or reporting issues!

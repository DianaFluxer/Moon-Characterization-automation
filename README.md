# Moon-Characterization-Automation
Auto-Alignment and Measurement Workflow Code

## Overview

This project provides an **automated sample alignment and measurement workflow** designed for integrated optical and electrical testing of the **Moon SLM structures** in a **16 × 16 pixel configuration**.  
It combines **motorized stage control**, **camera-based alignment**, **optical characterization**, and **electrical characterization** within one coordinated system.  

---

### **Workflow Stages**

1. **Auto-Alignment (Stage 1)**  
   - Uses **Newport motorized actuators** and a **camera** to locate and align the sample to predefined reference points.  
   - Supports both **manual (operator-assisted)** alignment for initial calibration and **automatic (template matching)** alignment modes.  
   - Calculates an **affine transformation** to correct for stage offsets, sample rotation, and tilt before measurements begin.  

2. **Absorption Measurement (Stage 2)**  
   - Activates the **LED illumination source** by opening the shutter and measures the **spectral response** of the LED reflected from a gold surface to save calibration data.  
   - Moves to the first pixel in the coordinate system and collects the **absorption curve** for each **bias voltage** and **base temperature (T)**.  

3. **Reflectivity and Absolute Power Measurement (Stage 3)**  
   - Switches to a **single-mode laser** for precise reflectivity measurements.  
   - Records reflected intensity at defined coordinates for each **voltage** and **input power**, by rotating the **half-wave plate** in the setup.  
   - Measures forward current in the **p–n junction** under illumination to evaluate reflectivity response.  

4. **Electrical Characterization (Stage 4)**  
   - Shuts off all light sources.  
   - Performs **I–V (current–voltage)** measurements on the same sample positions as the optical tests.  

5. **Data Integration (Stage 5)**  
   - All results (alignment data, absorption, reflectivity, I–V) are stored in a **single database** for unified access and traceability.  
   - Data are appended to a **master database** using **QCoDeS**.  
   - Each record includes timestamp, spatial coordinates, measurement parameters, and results to ensure consistent data correlation.  

---

### **Automation Loop**
After completing all measurements for one pixel, the system repeats the **alignment and measurement sequence** for the next pixel coordinate until the entire **16 × 16 pixel array** has been characterized.
  
Repeats alignemnt and emusremnt for net pixel coordinates

### **Purpose**
- Ensure reproducible alignment across optical and electrical experiments.  
- Enable fully automated, position-registered multi-modal measurements.  
- Provide a single, structured data pipeline from calibration to analysis.  

# Moon-Characterization-automation
Auto-Alignment and Measurement Workflow Code
## 🧩 Overview

This project provides an **automated sample alignment and measurement workflow** designed for integrated optical and electrical testing.  
It combines **motorized stage control**, **camera-based alignment**, **optical measurements**, and **electrical characterization** within one coordinated system.  

### **Workflow Stages**

1. **Auto-Alignment (Stage 1)**  
   - Uses Newport motorized actuators and a camera to locate and align the sample to predefined reference points.  
   - Supports both **manual** (operator-assisted) and **automatic** (template matching) alignment modes.  
   - Calculates an **affine transformation** to correct for stage offsets, sample rotation, and tilt before measurements begin.  

2. **Optical Absorption Measurement (Stage 2)**  
   - Activates an **LED illumination source** and measures transmitted intensity or spectral response.  
   - Computes absorption or transmission characteristics at aligned sample points.  

3. **Reflectivity Measurement (Stage 3)**  
   - Switches to a **single-mode laser** for precise reflectivity measurements.  
   - Records reflected intensity at defined coordinates using the same spatial calibration from alignment.  

4. **Electrical Characterization (Stage 4)**  
   - Performs **I–V (current–voltage)** measurements on the same sample positions as optical tests.  
   - Correlates optical and electrical properties point-by-point for comprehensive analysis.  

5. **Data Integration (Stage 5)**  
   - All results (alignment data, absorption, reflectivity, I–V) are stored in a **single database** for unified access and traceability.  
   - Each record includes timestamp, spatial coordinates, measurement parameters, and results to ensure consistent data correlation.  

### **Purpose**
- Ensure reproducible alignment across optical and electrical experiments.  
- Enable fully automated, position-registered multi-modal measurements.  
- Provide a single, structured data pipeline from calibration to analysis.  

## Demo Screenshot
# Driver State Estimation for Adaptive Vehicle Safety Control

## Overview

This project focuses on estimating driver fatigue and attention states using behavioral data such as eye movement, steering input, and vehicle dynamics.
The goal is to improve driving safety by enabling adaptive vehicle control based on real-time driver conditions.

## Background

Human factors contribute significantly to traffic accidents.
Conventional vehicle control systems are designed under uniform assumptions, without considering the driver's real-time condition.
This project aims to bridge the gap between human state understanding and vehicle control.

## Method

* Behavioral data simulation (eye movement, steering variance, speed variation)
* Feature engineering from multi-modal data
* Machine learning model: Random Forest
* Binary classification of driver fatigue state

## Result

The model demonstrates that combining multiple behavioral features enables effective estimation of driver fatigue states.
This suggests the feasibility of real-time driver monitoring systems.

## Application

* Driver monitoring systems (DMS)
* Warning alerts for fatigue detection
* Adaptive vehicle control (e.g., deceleration support)

## Tech Stack

* Python
* pandas / numpy
* scikit-learn
* Streamlit

## Demo

This project includes an interactive dashboard built with Streamlit.
Users can simulate driver conditions and observe fatigue predictions in real time.

## Future Work

* Integration of real-world driving data
* Time-series modeling (LSTM)
* Personalization for individual driver differences
* Real-time implementation

## Author

Kazuki Kubo

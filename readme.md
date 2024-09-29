# Grader Guru

An AI-powered grading system for evaluating handwritten answer sheets, including both textual content and diagrams.

## Overview

Grader Guru is an advanced automated grading system that leverages Large Language Models (LLMs) and Computer Vision techniques to evaluate handwritten student submissions. It provides accurate scoring for both textual answers and diagrams, streamlining the grading process for educators.

## Features

- **AI-Powered Grading**: Utilizes LLMs to evaluate handwritten answers against model responses.
- **Diagram Evaluation**: Integrates YOLOv5 and CRAFT for converting diagrams to text, enabling comprehensive assessment of visual components.
- **Scalable Backend**: Implements a FastAPI backend with Langchain for efficient and responsive processing.

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Computer Vision (CV)
- Langchain
- FastAPI
- YOLOv5
- CRAFT (Character Region Awareness for Text Detection)

## Installation

```bash
git clone https://github.com/yourusername/grader-guru.git
cd grader-guru
pip install -r requirements.txt


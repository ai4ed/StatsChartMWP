# StatsChartMWP
![MWP](https://img.shields.io/badge/Task-Math_Word_Problems-green)
![Mathematical Reasoning](https://img.shields.io/badge/Task-Mathematical_Reasoning-green) 
![Multimodal Reasoning](https://img.shields.io/badge/Task-Multi--Modal-green) 

![GPT-4](https://img.shields.io/badge/Model-GPT--4-red) 
![GPT-4V](https://img.shields.io/badge/Model-GPT--4V-red)
![GPT-4o](https://img.shields.io/badge/Model-GPT--4o-red)

<!-- 🌟  This is the official repository for the paper "[StatsChartMWP: A Dataset for Evaluating Multimodal Mathematical Reasoning Abilities on Math Word Problems with Statistical Charts](https://arxiv.org/pdf/xxx.pdf)" -->

This is the official repository for the paper "StatsChartMWP: A Dataset for Evaluating Multimodal Mathematical Reasoning Abilities on Math Word Problems with Statistical Charts", the paper link is coming soon.

 <!-- [[📖 Paper](https://arxiv.org/pdf/xxx.pdf)] [[🤗 Huggingface Dataset](https://huggingface.co/datasets/xxx)] -->
 



## 🏆 Leaderboard

The leaderboard is continuously being updated. If you have any new results to contribute, please feel free to reach out to us.

| **#** | **Model** | **Method**| **Date** | **ALL** | **Bar** | **Hist** | **Line** | **Line-f** | **Scatter** | **D-axis** | **P-bar** | **Pie** | **Table** | **Comp** | **Radar** |
| ----------- | ---------------------- | ------------------------ | -------------- | ------------- | ------------- | -------------- | --------------- | --------------- | -------------- | ------------- | --------------- | --------------- | ------------- | --------------- | -------------- |
| 1 | GPT-4o | LMM | 2024-06-04 | 55.62 | 65.53 | 23.87 | 58.08 | 43.51 | 43.12 | 51.56 | 36.36 | 71.39 | 79.69 | 49.94 | 41.67 | 
| 2 | GPT4(GPT-4o) | LLM | 2024-06-04 | 46.95 | 59.98 | 13.30 | 52.72 | 35.98 | 27.50 | 45.31 | 27.27 | 59.19 | 71.85 | 38.82 | 20.83 | 
| 3 | GPT-4V | LMM | 2024-06-04 | 34.28 | 38.57 | 12.10 | 40.48 | 28.87 | 30.00 | 39.06 | 18.18 | 38.25 | 55.67 | 27.89 | 33.33 |
| 4 | GPT4(GPT-4V) | LLM | 2024-06-04 | 31.47 | 38.11 | 8.61 | 39.12 | 22.18 | 20.62 | 35.94 | 4.55 | 34.71 | 52.46 | 24.36 | 20.83 | 
| 5 | Qwen-VL-MAX | LMM | 2024-06-04 | 30.24 | 37.40 | 10.19 | 29.51 | 19.25 | 20.00 | 29.69 | 18.18 | 37.86 | 54.74 | 16.91 | 33.33 | 
| 6 | InternVL-1.5 | LMM | 2024-06-04 | 23.26 | 34.69 | 6.98 | 29.42 | 15.48 | 21.88| 35.94| 4.55 | 23.89 | 31.36 | 15.89 | 16.67| 
| 7 | InterVL-Chat-V1-2-Plus | LMM | 2024-06-04 | 22.16 | 31.46 | 7.19 | 27.13 | 14.23 | 15 | 28.12 | 9.09 | 24.19 | 31.43 | 15.44 | 20.83 | 
| 8 | Qwen-VL-PLUS | LMM | 2024-06-04 | 19.68 | 24.85 | 7.47 | 22.28 | 15.06 | 13.12 | 31.25 | 9.09 | 19.27 | 33.14 | 13.01 | 12.50 | 
| 9 | InternLM_2_VL_7B | LMM | 2024-06-04 | 17.13 | 24.36 | 5.78 | 23.81 | 13.81 | 16.88 | 25 | 18.18 | 19.17 | 19.81 | 12 | 16.67 | 
| 10 | LLaVA-NeXT-34B | LMM | 2024-06-04 | 15.67 | 20.96 | 5.45 | 23.13 | 13.39 | 20 | 25 | 4.55 | 14.06 | 19.24 | 12.44 | 20.83 | 
| 11 | DeepSeek-VL-7B-Chat | LMM | 2024-06-04 | 13.2 |16.06 |4.63 |	21.43 |11.72 |12.5 |28.12 |	4.55 |	14.16 |15.47 |9.78 |	8.33 |
| 12 | Qwen-VL | LMM | 2024-06-04 | 10.97 | 13.25 | 5.01 | 14.63 | 11.3 | 11.25 | 28.12 | 9.09 | 9.83 | 13.61 | 9.67 | 20.83 | 
| 13 | HPT | LMM | 2024-06-04 | 10.10 | 9.91 | 5.07 | 17.77 | 9.62 | 10.62 | 26.56 | 9.09 | 7.18 | 10.62 | 11.56 | 29.17 | 




## 📐 StatsChartMWP Dataset

The StatsChartMWP dataset is designed as a benchmark to develop AI models capable of understanding multimodal information present in math word problems with statistical charts. Our dataset incorporates a variety of chart forms, presenting a broad visual spectrum and mathematical knowledge competencies and each item originates from real-world educational contexts, encompassing challenges formulated by mathematics educators, genuine student inquiries, and historical examination questions. The StatsChartMWP dataset encompasses 8,514 unique MWPs with statistical charts. The StatsChartMWP dataset contains 11 different types of statistical charts, including bar/line/line-function/dual-axis/pie/composite/radar/histograms/scatter/percentage-bar/tables. A comparative example between our dataset and ChartQA and FigureQA is shown below.

![domains](assets/figures/ours_compare_with_others.png)

The **StatsChartMWP** dataset json file and images are provided in [`data`]. 
<!-- Images you can download from the [🤗 Huggingface](https://huggingface.co/datasets/xxx). -->
<!-- For more details, You can refer to our paper [`here`](https://arxiv.org/pdf/xxx.pdf) -->


## 🌟 CoTAR

### Introduction
We introduce CoTAR, a data augmentation strategy that utilizes CoT augmented reasoning to alleviate the cross-modal alignment between representations of visual mediums of artificial figures and technical language and equations. Specifically, instead of directly using the concise textual solutions of the MWPs, we use the state-of-the-art LLM, so convert them into detailed step-by-step explanations in a CoT-alike format to improve their logical clarity. Furthermore, each step is made up of a short step summary that explicitly states the purpose of this step and a concrete reasoning response. The step summary serves as a guiding directive for the logical analysis or computation required in the current step, while the concrete reasoning response provides a detailed explanation of the process undertaken in response to the step summary. The architecture of our method illustrated in follow:

<p align="center">
    <img src="assets/figures/architecture.png" width="100%"> <br>
  Overview of our method for mathematical solution augmentation. (a) is the input question. (b) is the original solution of the question. (c) is the augmentation solution of our method. (d) is the accuracy of open-source InternVL-Chat-V1-2-Plus, finetuned with (b) and (c) solution, respectively.
</p>

We conducted fine-tuning on [`InternVL-Chat-V1-2-Plus`](https://github.com/OpenGVLab/InternVL). By employing both problem-original solution pairs and problem-augmented solution pairs on our proprietary training dataset, we achieved a 3.13\% improvement in algorithmic accuracy.



### Quick Start

#### Finetune
Finetune the InternVL-Chat-V1-2-Plus, you can see the official GitHub repository of [`InternVL-Chat-V1-2-Plus`](https://github.com/OpenGVLab/InternVL).


#### CoTAR
the prompt of CoTAR is provided in [`prompts`](https://github.com/ai4ed/StatsChartMWP/tree/main/prompts). You can run the main code to get the CoTAR solution data.
```shell
python main.py
```



## License

[![CC0 license](https://img.shields.io/badge/CC0-1.0-blue.svg)](https://lbesson.mit-license.org/)

This work is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)


<!-- ## 📝 Citation

If you find this datasets useful in your research, please consider citing this BibTex:

```
@misc{xxx
}
``` -->


## Related Work

Explore our additional research on **Vision-Language Large Models**, focusing on multi-modal LLMs and mathematical reasoning:

- **[ChartQA]** [ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning](https://github.com/vis-nlp/ChartQA)
- **[TABMWP]** [DYNAMIC PROMPT LEARNING VIA POLICY GRADIENT FOR SEMI-STRUCTURED MATHEMATICAL REASONING](https://github.com/lupantech/PromptPG)
- **[MathVista]** [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://github.com/lupantech/MathVista)
- **[MathVerse]** [MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](https://github.com/ZrrSkywalker/MathVerse)
- **[MATH-Vision]** [Measuring Multimodal Mathematical Reasoning with the MATH-Vision Dataset](https://github.com/mathvision-cuhk/MathVision)
- **[OlympiadBench]** [OlympiadBench: A Challenging Benchmark for Promoting AGI with Olympiad-Level Bilingual Multimodal Scientific Problems](https://github.com/OpenBMB/OlympiadBench)
- **[InternVL]** [InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://github.com/OpenGVLab/InternVL)
- **[LLaVA]** [LLaVA: Large Language and Vision Assistant](https://github.com/haotian-liu/LLaVA)



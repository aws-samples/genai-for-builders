---
title: "Generative AI for Builders on Amazon SageMaker"
weight: 0
---

## Overview

The purpose of this document is to outline the desired state of key customer journeys for builders looking to leverage Generative AI models on SageMaker. The builders we are targeting are the traditional persona served by SageMaker, Data Scientists and ML Engineers. However, the Jobs-to-be-Done (JTBD) are different from the traditional JTBD of SageMaker, namely Prepare, Build, Train and Deploy. These JTBD are still relevant for predictive AI customers, as well as model producers of Generative AI models, who build their own model from scratch. However, this document focused on Generative AI model consumers, who we believe will form a large and growing part of the customer base of SageMaker. These customers use pre-built Generative AI models vs building these models themselves from scratch. The JTBD of Data Scientists and ML Engineers for these customers can be summarized into 2 pillars.

 ![](/static/pillars.png) 

**Pillar 1**: Enterprise grade Generative AI Model Hub with complete toolset for model consumers (Data Scientists and MLEs) JTBD: Filter/Search => Evaluate and Select => Customize => Deploy. The JTBD in this pillar are covered in Journeys 1, 3, 4, and 6 of this document and corresponding parts of Appendix A for roadmap.

**Pillar 2**: Industrialize end-to-end Generative AI model deployment JTBD: a/MLOps orchestration of jobs in Pillar 1 (Journey 5) b/Monitoring of inputs and outputs of deployed models (Journey 2) c/Experiment on Evaluate + Customize (Journey 4.5). 

## Workshop Scenario ##

Naxt Corp. is a large financial services institution. Naxt wants to be the industry leader in driving innovative changes in process through technology, and to that end, they want to leverage Generative AI in all of their processes. They have previously done a PoC of using Generative AI models for a few use cases using OpenAI and Anthropic models and Langchain (please note, this journey was outside of SageMaker, likely using OpenAI or Plato. Consider this Journey 0 and in future we will evaluate whether to extend SageMaker capabilities to enable this journey). Based on the PoC, they have identified 2 business problems which they will target with Generative AI initially, and they want to use the “cheapest model that gets the job done effectively.” Being a large financial services institution, they are only allowed to use enterprise grade software and models. The first use case is summarizing all past conversations with High Net Worth (HNW) individuals to provide to Investment Advisors, who can then utilize these to rapidly shortlist HNW individuals to reach out to, and easily come up to speed on past interactions with them. The second use case is to build a chatbot using Generative AI models that can answer questions about internal processes like ordering a laptop, or getting an office space allocated accurately (and politely, keeping a professional tone that is representative of communications within Naxt Corp.).

## Personas: Data Scientist, ML Engineer ##

 **Kaitlin** is an experienced, mid-career data scientist who has specialized specifically on large language models (LLMs) and Computer Vision (CV) use cases. She works for Naxt Corp., a large financial services institution, and as part of her job, she regularly uses AWS services. At present she has been tasked with helping optimize some of the current processes at Naxt using Generative AI, and she had led the PoC process for evaluating which tasks/processes can benefit from Generative AI. She has also been asked to be frugal, and given limited resources for this project which includes herself and an ML Engineer (MLE). Hence building a foundational model (FM) from scratch is out of question. Instead, she plans to use one of the existing FMs available in various model hubs. At the same time, she is a builder, and Naxt is a company of builders, who prefer to have some control to set up and configure infrastructure optimized performance and cost. Having said that, with the support of only one MLE, she does not have the bandwidth to manage the infrastructure on an ongoing basis. She searched for model repositories, and landed at the Hugging Face website. Her company’s strict enterprise security and compliance requirements prevent her from using open-source model hubs or platforms. From Hugging Face, she was routed to Amazon SageMaker Jumpstart Model Hub for an enterprise grade Generative AI model hub and asked to log in with her AWS credentials. Being an AWS service, it met all her criteria for security and compliance, and she can see that Jumpstart has a large collection of Generative AI models she plans to try out for her use case. She has played around with SageMaker Studio before and has Domains set up, and can navigate to SageMaker Jumpstart model hub right away. However, before picking SageMaker as the platform of choice, she consults with her MLE Brandon, who is responsible for deploying and maintaining any AI/ML based solution.

 **Brandon** is an experienced ML engineer who has deployed popular open-source tools and built custom tooling where needed to automate the entire machine learning lifecycle in the past. While he has basic knowledge of ML concepts, his focus is on packaging and deploying models for development and production. In addition, he builds and maintains the infrastructure and tools to do so. He has a good understanding of what it takes to operationalize a system for production use cases. He’s familiar with Python, Java, and Go. He has setup CI/CD pipelines using Git and Jenkins in the past. He interfaces with application software developers who in turn build ML powered applications that rely on the models he deploys. In previous projects he has worked with a range of AWS services in the past, including S3, Lambda, and EC2. As a result, he has experience using AWS tooling for setting up automated deployments such as Service Quotas, CloudFormation and Cloud Development Kit. Brandon also has extensive experience deploying ML workflows, including selecting the right instance type to host models. Brandon has previously used SageMaker and likes its ease of use and is ready to get started when Kaitlin comes to him with the idea of exploring SageMaker as an option to pick a model and use it.

 ## Key Customer Journeys ##

 Each of these journeys below correspond to one or more Jobs-to-be-Done (JTBD) of the 3 pillars for Generative AI model consumers referred earlier in this section. There are other journeys in the Generative AI domain, like that of an application developer or that of a model producer which we do not cover in this workshop.

- **Journey 1 - Filter and Deploy: Come to Jumpstart => Filter/Search for Model => Deploy to Inference:** This journey is effectively two journeys corresponding to two JTBD, 1/ Filter/Search and 2/ Deploy. We have merged the two into a single journey because there are circumstances where customers have a strong idea of which model they want, and do not go through Evaluate and Customize phases (Journey 3 and 4) before they Deploy the model. This journey reflects such a situation.

- **Journey 2 - Monitor: Come to Jumpstart => Filter/Search => Deploy to Inference => Monitor Outputs:** This journey is additive to Journey 1 above and corresponds the JTBD of Monitor in Pillar 2.

- **Journey 3 - Evaluate and Select: Come to JumpStart => Evaluate and Select Model (Margaret) => [If model meets all criteria => Deploy to Inference => Monitor Outputs (Journey 1 and 2)] => [If not => Customize (Journey 4)]:** Journey 3 focuses on rigorous evaluation and selection process for models in Jumpstart using SageMaker Clarify Model Evaluation, and corresponds to the JTBD of Evaluate and Select in Pillar 1. SageMaker Clarify Model Evaluation deploys Inference endpoints automatically as part of an evaluation job. After Journey 3 completes, Kaitlin will use Journey 1 to deploy the model if the model passes her evaluation criteria. If it does not pass then Kaitlin will use Journey 4 described later in this document for customization.

- **Journey 4 - Customize (Fine-tune): Come to Jumpstart => Evaluate and Select Model \[Margaret\] => Fine Tune => Evaluate  Model \[Margaret\] => Deploy to Inference => Monitor Outputs:** Journey 4 focuses on fine-tuning of models in Jumpstart, and corresponds to the JTBD of Customize in Pillar 1.

- **Journey 5 - Orchestrate with MLOps: Come to Jumpstart => Evaluate models and Select model [Margaret]=> Fine Tune [Training] => Deploy in Inference [Inference] => Monitor Outputs [SageMaker Model Monitor] => Automate with MLOps:** This journey is about automating Journey 1-4 with MLOps and corresponds to JTBD of MLOps orchestration in Pillar 2.

- **Journey 6 - Collect HIL data for Customization: Come to Jumpstart => Evaluate models and Select model => Collect additional data for Instruction Tuning [HIL] => Fine Tune => Evaluate => Deploy Model => Monitor Outputs:** This journey focuses on the Human in Loop (HIL) data collection for Instruction Tuning, which is the term used for fine tuning Generative AI models with human input and feedback. Today, the most commonly used Instruction Tuning techniques for Generative AI models are Supervised Fine Tuning (SFT) and Reinforcement Learning with Human Feedback (RLHF). In this journey we focus on SFT. This journey corresponds to JTBD of Customization providing workflows and workforce for HIL data collection for fine tuning

## Cost

By preforming evaluation jobs on models in your account, you will incur costs based on the type of job, model, and instance type selected. If you are running a model on an instance, this model will continue to incur cost as long as it is active.

## Duration

2 hours.

## Cleanup

Make sure to turn off any model instances you have created during this lab in order to not incur unnecessary cost.
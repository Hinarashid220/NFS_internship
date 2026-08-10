# Chain-of-Thought (CoT) & Persona Prompting Experiment

## Overview
This experiment demonstrates the impact of combining **Chain-of-Thought (CoT) prompting** with **Persona/Role prompting**, compared against a standard direct prompt, when solving a multi-step financial reasoning problem. The goal is to show how prompt design affects not just the *quality* of an AI response, but its **structure, transparency, and reliability**.

---

## Objective
To evaluate whether adding a professional persona and an explicit step-by-step reasoning instruction improves:
- The accuracy of multi-step calculations
- The clarity and verifiability of the response
- The overall professional tone and usability of the output

---

## Scenario / Problem Statement
> A small online shop sells custom mugs for $15 each. The fixed monthly operational cost is $300, and each mug costs $5 to produce. In August, they ran a discount promotion: if a customer bought 3 or more mugs, they got $5 off the total order. A total of 10 customers bought 3 mugs each, and 5 customers bought 1 mug each. Did the shop make a profit or a loss in August, and by how much?

---

## Experiment Runs

### Run 1: Standard Prompt (Without CoT or Persona)
- **Prompt:** The problem statement was asked directly, with no additional instructions.
- **Result Summary:** The model provided a quick, direct response. While it attempted the calculation, it lacked clear line-item breakdowns, making the math difficult to verify at a glance. Order-level discount logic (a $5 discount per *order*, not per mug) is easy to misapply in a single-pass answer.

### Run 2: Persona + Chain-of-Thought Prompt
- **Prompt:**
  ```
  You are a senior financial analyst. Think step-by-step before answering.
  [Problem Statement]
  ```
- **Result Summary:** The model explicitly broke the solution into sequential categories: Total Mugs Sold, Gross Revenue, Applied Discounts, Production Costs, Fixed Costs, and Net Profit/Loss — each shown as a distinct, auditable step.

---

## Worked Solution (Reference Answer)
This is the correct step-by-step breakdown that a well-structured CoT response should arrive at:

| Step | Calculation | Result |
| :--- | :--- | :--- |
| Total mugs sold | (10 × 3) + (5 × 1) | 35 mugs |
| Gross revenue (before discount) | 35 × $15 | $525 |
| Total discount applied | 10 orders × $5 off | −$50 |
| Net revenue | $525 − $50 | $475 |
| Production cost | 35 × $5 | $175 |
| Fixed operational cost | — | $300 |
| **Total costs** | $175 + $300 | **$475** |
| **Net result** | $475 − $475 | **$0 (Break-even)** |

**Conclusion:** The shop neither made a profit nor a loss in August — it broke even exactly. This makes the scenario a particularly good CoT test case: a rushed, non-stepwise answer can easily misapply the discount (e.g., applying it per mug instead of per order) and land on an incorrect profit or loss figure instead of the true break-even result.

---

## Before vs. After Comparison

| Metric | Run 1 (Standard Prompt) | Run 2 (Persona + CoT Prompt) |
| :--- | :--- | :--- |
| **Structure** | Unstructured narrative text | Formatted breakdown with headings & bullet points |
| **Clarity** | Intermediate steps were skipped or combined | Every calculation step is explicitly listed |
| **Tone & Depth** | Basic conversational tone | Professional financial summary tone |
| **Accuracy Risk** | Higher — discount logic can be misapplied silently | Lower — each rule is applied and shown separately |
| **Verifiability** | Hard to audit without re-deriving the math | Easy to check each line against the source data |

---

## Explanation & Analysis
In the standard prompt run, the model attempted to calculate the answer directly in one pass, which increases the likelihood of skipping intermediate steps or misinterpreting rules like order-level discounts (a common failure point in this scenario). Adding the persona of a **senior financial analyst** instructed the AI to adopt a structured, professional framework, organizing the data into distinct operational categories (Revenue, Discounts, Variable Costs, and Fixed Costs). Instructing the AI to **"think step-by-step"** forced it to process each calculation sequentially before stating the final result, producing a response that was more transparent, easier to audit, and less prone to silent calculation errors.

---

## Key Takeaways
- **Persona prompting** shapes tone, framing, and the categories used to organize an answer — it makes the model "think" like a domain expert.
- **CoT prompting** shapes reasoning *process* — it reduces the chance of skipped or merged steps in multi-step problems.
- Combined, they produce outputs that are not just more readable, but more **verifiable**, which matters most in domains like finance where a wrong intermediate step (e.g., discount logic) can silently flip the final conclusion.
- This scenario's break-even result is a useful stress test: a shallow answer might round or approximate its way to a "small profit" or "small loss," while a stepwise answer correctly identifies the exact $0 outcome.

---

## Author
**Hina Rashid**
Prepared as part of Generative AI and Prompt Engineering coursework/tasks.

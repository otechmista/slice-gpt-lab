# Loss and Backpropagation: How the Model Learns from Mistakes

The model makes a guess. The guess is wrong. The model adjusts. Repeat millions of times.

That's training, at a high level. But how does the model actually adjust? That's what **loss** and **backpropagation** are for.

## Where This Lives

```txt
app/loss.py
app/train.py
```

## What Is Loss?

Loss is a number that measures how wrong the model's prediction was.

The model produces logits — a score for every possible next character. The correct next character is known (it's in the training data). **Cross-entropy loss** compares those scores against the correct answer:

- If the model gave a high score to the correct character: **low loss** (good job)
- If the model gave a low score to the correct character: **high loss** (bad guess)

Loss is a single number. Lower is better. The goal of training is to make this number go down.

## A Scoring Analogy

Imagine a multiple-choice quiz where you must rank your confidence in each answer from 0 to 100. You spread your confidence across all choices. The scoring penalizes you more harshly the more confidence you placed on wrong answers.

Cross-entropy works the same way: it rewards the model for putting high probability on the right character, and penalizes it for spreading probability to wrong ones.

## What Is Backpropagation?

After computing the loss, we need to answer one question:

> Which parameters caused this error, and by how much?

**Backpropagation** traces the loss backwards through the entire network — from the output projection, through the transformer blocks, through the embeddings — and calculates a **gradient** for every single parameter.

A gradient tells us: "if you increase this weight slightly, does the loss go up or down, and by how much?"

Then the optimizer uses those gradients to update the weights:

```txt
weight = weight - learning_rate × gradient
```

A small `learning_rate` (like `0.003`) means we adjust weights gently. Too large and training becomes unstable. Too small and it learns too slowly.

## The Optimizer: AdamW

This project uses **AdamW** — a popular optimizer that improves on basic gradient descent by keeping track of momentum and adapting the learning rate per parameter. You don't need to understand all its math right now. The key idea is:

> AdamW takes gradients and figures out smart weight updates.

## NaN: When Training Goes Wrong

Sometimes the loss becomes `NaN` (Not a Number). This happens when numbers overflow or explode during computation. The training loop stops immediately if this happens.

A `NaN` loss is a sign of numerical instability — usually from a learning rate that's too high or a poorly configured model.

## What You Should Be Able to Explain

- What loss measures
- Why lower loss means better predictions
- What a gradient is
- What backpropagation does
- Why the learning rate matters

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Forward Pass](07_forward_pass.md) turns token sequences into logits.

Next: [Training Loop](09_training_loop.md) puts dataset, model, loss, optimizer, and checkpointing into one loop.

<!-- COURSE_THREAD_END -->
